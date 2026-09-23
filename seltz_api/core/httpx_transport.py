"""httpx-backed transports -- the default implementations of the two transport protocols.

The sync and async adapters live together because they are peers differing only in ``await``, the
same reason :class:`RawClient` and :class:`AsyncRawClient` share a module. Everything httpx-specific
is confined here: swapping HTTP libraries means writing one more module like this one, not touching
anything else.

File ownership is written down here and nowhere else: every handle this module opens for a body --
a ``Path`` in a multipart part or a raw body, and the temp file an async part is spilled to -- is
registered on the send's ``ExitStack``, so it is closed when the send returns or raises,
deterministically and never by a finalizer. A handle the caller opened is passed through untouched
and never closed."""

from __future__ import annotations

import asyncio
import inspect
import io
import os
import ssl
from collections.abc import AsyncIterable, AsyncIterator, Callable, Iterable, Iterator, Mapping
from contextlib import ExitStack, suppress
from dataclasses import dataclass, replace
from pathlib import Path
from tempfile import mkstemp
from typing import Any

import httpx
from typing_extensions import TypeIs

from ._internal.content_disposition import render_content_disposition
from .bodies import (
    BinaryBody,
    FormBody,
    JsonBody,
    MultipartBody,
    MultipartFile,
    MultipartPart,
    MultipartText,
    RequestBody,
    TextBody,
)
from .files import AsyncBinaryContent, AsyncBinaryReader, BinaryReader
from .transport import (
    AsyncHttpClient,
    AsyncStreamedResponse,
    HttpClient,
    HttpRequest,
    HttpResponse,
    StreamedResponse,
)

_DEFAULT_TIMEOUT = 30.0

_CHUNK_SIZE = 65_536
"""httpx's own multipart chunk size (``FileField.CHUNK_SIZE``), matched for the raw-body readers."""

_ASYNC_SOURCE_ON_SYNC_CLIENT = (
    "an async byte source cannot be sent by the sync client -- pass bytes, a Path, "
    "a binary reader or an Iterator[bytes], or use the async client"
)
"""What both sync legs raise for an async arm no type checker caught -- a raw body and a multipart
part give the same answer to the same mistake.

Only the message is shared. Each ``if`` stays written out at its own site, because it is what
narrows the union away from the async arms; behind a helper, neither leg could prove its return
type."""


def _is_async_reader(content: object) -> TypeIs[AsyncBinaryReader]:
    """Whether ``content`` is a reader whose ``read`` must be awaited.

    ``isinstance`` alone cannot tell the two reader protocols apart -- ``runtime_checkable``
    checks only that ``read`` exists -- so the async arm is decided by whether ``read`` is a
    coroutine function. ``TypeIs`` rather than ``TypeGuard``: the negative branch must narrow
    too, or the sync adapter could not prove its return type."""
    return isinstance(content, AsyncBinaryReader) and inspect.iscoroutinefunction(getattr(type(content), "read", None))


def _require_binary_reader(reader: BinaryReader) -> None:
    """Reject a text-mode handle before its first chunk reaches the wire.

    ``read(0)`` returns ``b""`` for a binary handle and ``""`` for a text one, without consuming
    anything -- a one-sided check: only ``str`` raises (``RawIOBase`` may legally return ``None``).

    Raises:
        TypeError: If ``reader`` was opened in text mode."""
    if isinstance(reader.read(0), str):
        raise TypeError("a text-mode file cannot carry binary content -- open it in binary mode ('rb')")


def _reports_its_own_length(reader: BinaryReader) -> bool:
    """Whether the library's length peek would describe what ``read`` will yield.

    It peeks with ``fstat(fileno())``, else a seek to the end -- both of which measure the stream's
    own extent. That is the body only when the reader does not transform what it reads: a buffered
    reader straight over a file, or an in-memory buffer. A decompressing reader answers with its
    *compressed* size, and wrapping one changes nothing, because the raw layer is still the
    transformer.

    ``BufferedRandom`` belongs here beside ``BufferedReader``: it is what ``os.fdopen(fd, "w+b")``
    returns, so :func:`_spilled`'s drained part stays measured.

    A positive list, so a reader this does not recognise is chunked rather than mis-measured."""
    if isinstance(reader, io.BytesIO):
        return True
    return isinstance(reader, (io.BufferedReader, io.BufferedRandom)) and isinstance(
        getattr(reader, "raw", None), io.FileIO
    )


def _is_at_start(reader: BinaryReader) -> bool:
    """Whether nothing has been read yet, so the stream's extent is also what remains.

    The peek reports the whole extent and never the remainder, so a handle already positioned
    mid-file would be over-declared. ``tell`` is not part of the protocol and raises on a stream
    that is fd-backed but not seekable; either is the same answer as *cannot prove it*."""
    tell = getattr(reader, "tell", None)
    if tell is None:
        return False
    try:
        return bool(tell() == 0)
    except OSError:
        return False


def _sync_content(content: AsyncBinaryContent, stack: ExitStack) -> bytes | BinaryReader | Iterable[bytes]:
    """Adapt a raw-body descriptor for the sync client, opening what needs opening onto ``stack``.

    Takes the full async union because that is ``BinaryBody.content``'s type -- the *static* gate
    is the emitted endpoint signature, which offers the sync client only the sync arms. The
    rejection below is the runtime backstop for a caller no checker saw, replacing the opaque
    stream-type error the underlying library would raise mid-send.

    A reader is handed on **only when the library can size it correctly**. The peek behind that
    ``Content-Length`` measures the descriptor's extent, not what ``read`` will yield from here, and
    the two diverge for a transforming reader and for one starting mid-file -- so the body would go
    out under a length that does not match it. :func:`_reports_its_own_length` and
    :func:`_is_at_start` are the two halves of *provable*; everything else is chunked, which is also
    what a reader carrying nothing but ``read`` needs, since the library's ``content=`` gate is
    ``isinstance(..., Iterable)`` and would refuse it outright.

    Raises:
        TypeError: If ``content`` is an async arm, or a reader opened in text mode."""

    def chunks(reader: BinaryReader) -> Iterator[bytes]:
        while chunk := reader.read(_CHUNK_SIZE):
            yield chunk

    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return stack.enter_context(content.open("rb"))
    if _is_async_reader(content) or isinstance(content, AsyncIterable):
        raise TypeError(_ASYNC_SOURCE_ON_SYNC_CLIENT)
    if isinstance(content, BinaryReader):
        _require_binary_reader(content)
        if _reports_its_own_length(content) and _is_at_start(content):
            return content
        return chunks(content)
    return content


async def _awaited_chunks(reader: AsyncBinaryReader) -> AsyncIterator[bytes]:
    """Read an async reader to exhaustion in ``_CHUNK_SIZE`` windows.

    Module-level rather than nested because it has two callers, and they want the same windows for
    opposite reasons: a raw body streams them straight to the transport, and a multipart part writes
    them to a spill file first."""
    while chunk := await reader.read(_CHUNK_SIZE):
        yield chunk


async def _aiter(chunks: AsyncIterable[bytes]) -> AsyncIterator[bytes]:
    """Iterate an async iterable, so a caller's own chunk sizes reach :func:`_spilled` unchanged.

    Only :func:`_drained` needs this: an ``AsyncIterable`` is not an ``AsyncIterator``, and
    ``_spilled`` takes the narrower type so both of its callers hand it the same shape."""
    async for chunk in chunks:
        yield chunk


def _async_content(content: AsyncBinaryContent, stack: ExitStack) -> bytes | AsyncIterable[bytes]:
    """Adapt a raw-body descriptor to the async byte stream the async client demands.

    Sync arms read through a worker thread so a large upload from a slow disk does not park the
    event loop; the two async arms are consumed natively. A ``Path`` is opened here, eagerly, onto
    ``stack`` -- a momentary open on the loop, exactly as the multipart leg's ``_open`` does -- so
    a mid-send failure closes it on the stack's unwind rather than at a finalizer.

    The arm order is load-bearing: readers before iterables (a file handle iterates by *lines*),
    the async-reader guard before ``AsyncIterable`` (an async file is async-iterable by lines),
    and ``bytes`` before everything (it is an ``Iterable[int]``).

    Raises:
        TypeError: If ``content`` is a reader opened in text mode."""

    async def threaded_chunks(reader: BinaryReader) -> AsyncIterator[bytes]:
        # Every read in a worker thread: the non-blocking property of the async raw-body leg.
        while chunk := await asyncio.to_thread(reader.read, _CHUNK_SIZE):
            yield chunk

    async def iterable_chunks(chunks: Iterable[bytes]) -> AsyncIterator[bytes]:
        # Pulled on the loop: a caller's generator is the caller's own code; one that must not
        # block the loop is passed as an AsyncIterable instead.
        for chunk in chunks:
            yield chunk

    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return threaded_chunks(stack.enter_context(content.open("rb")))
    if _is_async_reader(content):
        return _awaited_chunks(content)
    if isinstance(content, BinaryReader):
        _require_binary_reader(content)
        return threaded_chunks(content)
    if isinstance(content, AsyncIterable):
        return content
    return iterable_chunks(content)


class _ChunkReader:
    """A read-only view over an iterable of chunks -- the shape the multipart encoder demands.

    The encoder can pull a part from ``bytes`` or from anything with a synchronous ``read``, and
    from nothing else, so an iterable reaches it through this and not at all otherwise.

    One of the encoder's two adapters, and the cheap one. This arm needs only a *shape* -- the
    chunks can be pulled synchronously, they simply do not arrive behind a ``read`` -- so a view
    suffices and nothing is copied or stored. Its sibling :func:`_spilled` answers the same demand
    for a source that must be **awaited**, which no view can bridge, and pays a temp file for it.
    The full statement of the httpx constraint both exist for is on ``_spilled``.

    It carries nothing but ``read``, deliberately. No ``seek``, so ``FileField.render_data`` skips
    the rewind it performs on a real handle; no ``fileno`` and no ``tell``, so the part reports no
    length and the whole body goes out chunked. An iterable is single-use, and a view that cannot
    rewind is what makes that visible rather than silently re-sending nothing.

    Owns nothing and closes nothing: the iterable is the caller's, exactly as a reader is."""

    __slots__ = ("_buffer", "_chunks")

    def __init__(self, chunks: Iterable[bytes]) -> None:
        self._chunks = iter(chunks)
        self._buffer = bytearray()

    def read(self, size: int = -1, /) -> bytes:
        """Return up to ``size`` bytes, or everything remaining when ``size`` is negative.

        Args:
            size: How many bytes to take; negative reads the iterable to exhaustion.

        Returns:
            The bytes taken, empty once the iterable is exhausted."""
        while size < 0 or len(self._buffer) < size:
            # ``next(..., None)`` rather than a falsy test: a generator may legally yield b"" in the
            # middle of a stream, and reading that as EOF would truncate the upload.
            chunk = next(self._chunks, None)
            if chunk is None:
                break
            self._buffer.extend(chunk)
        taken = bytes(self._buffer) if size < 0 else bytes(self._buffer[:size])
        del self._buffer[: len(taken)]
        return taken


class _UnsizedReader:
    """A caller's reader with its length claim withheld -- everything else passes through.

    Withholding ``fileno`` and ``tell`` makes the encoder's length peek answer ``None``, so the part
    claims no length and the body frames itself chunked. That peek measures the descriptor rather
    than the bytes ``read`` will produce, and the two diverge for a transforming reader; chunked is
    correct where a wrong length is not.

    ``seek`` is forwarded, unlike :class:`_ChunkReader`'s deliberate omission: ``render_data``
    rewinds a part before every render, and that rewind is what makes a caller's seekable handle
    re-sendable. A reader that cannot seek raises ``io.UnsupportedOperation``, which the encoder
    already catches -- the same answer a pipe gives.

    Owns nothing and closes nothing: the reader is the caller's."""

    __slots__ = ("_reader",)

    def __init__(self, reader: BinaryReader) -> None:
        self._reader = reader

    def read(self, size: int = -1, /) -> bytes:
        """Read from the wrapped reader, unchanged.

        Args:
            size: How many bytes to take; negative reads to exhaustion.

        Returns:
            Whatever the wrapped reader returned."""
        return self._reader.read(size)

    def seek(self, offset: int, whence: int = 0, /) -> int:
        """Reposition the wrapped reader, or refuse as a non-seekable stream does.

        Args:
            offset: Passed through unchanged.
            whence: Passed through unchanged.

        Returns:
            The wrapped reader's new absolute position.

        Raises:
            io.UnsupportedOperation: If the wrapped reader cannot seek."""
        seek = getattr(self._reader, "seek", None)
        if seek is None:
            raise io.UnsupportedOperation("underlying reader is not seekable")
        return int(seek(offset, whence))


def _open(content: AsyncBinaryContent, stack: ExitStack) -> bytes | BinaryReader:
    """Resolve a multipart part's content descriptor, opening what needs opening onto ``stack``.

    The one place the ownership rule is written down in code: a ``Path``'s handle is the SDK's,
    registered on the stack and closed when the send returns or raises; a caller's handle is
    returned untouched and never closed, and an iterable is wrapped, never consumed here.

    The arm order is ``_sync_content``'s, for the same reasons: ``bytes`` first (it is an
    ``Iterable[int]``), the async guard before the reader check (``runtime_checkable`` cannot tell
    the two reader protocols apart), readers before iterables (a file handle iterates by *lines*).
    On the async leg the async guard is unreachable -- :func:`_drained_parts` has already spilled
    those arms to a file, because the encoder cannot await.

    Raises:
        TypeError: If ``content`` is an async arm, or a reader opened in text mode."""
    if isinstance(content, (bytes, bytearray)):
        return bytes(content)
    if isinstance(content, Path):
        return stack.enter_context(content.open("rb"))
    if _is_async_reader(content) or isinstance(content, AsyncIterable):
        raise TypeError(_ASYNC_SOURCE_ON_SYNC_CLIENT)
    if isinstance(content, BinaryReader):
        _require_binary_reader(content)
        return content if _reports_its_own_length(content) else _UnsizedReader(content)
    return _ChunkReader(content)


async def _spilled(chunks: AsyncIterator[bytes], stack: ExitStack) -> BinaryReader:
    """Write an async source to a temp file the multipart encoder can read synchronously.

    **The limitation this exists for, at source (httpx 0.28.1).** ``MultipartStream.__aiter__`` is
    ``for chunk in self.iter_chunks(): yield chunk`` -- an ``async`` generator delegating to a
    *synchronous* one -- and ``FileField.render_data`` pulls each part with a plain
    ``self.file.read(CHUNK_SIZE)``. There is no ``await`` anywhere in ``_multipart.py``. So the
    encoder asks for bytes with a function call, and an awaitable source can only answer with one,
    and the two cannot meet: **both** async arms are affected, ``AsyncBinaryReader`` and
    ``AsyncIterable[bytes]`` alike, and neither can be driven from inside the encode at any cost.
    Draining first is not an optimisation, it is the only way either arm reaches the wire.

    A temp file is where it drains *to* because the encoder's demand is a synchronous ``read``, and
    that is the cheapest thing that offers one without holding the payload: each chunk is written
    straight out and dropped, so **nothing accumulates** -- the alternative that kept the bytes in
    the process peaked at twice the payload, measured (ADR-0051).

    **What bounds the residency is the chunk size, and only one arm's is the SDK's.**
    :func:`_awaited_chunks` reads a reader in ``_CHUNK_SIZE`` windows, so that arm is bounded here
    by construction. :func:`_aiter` forwards an ``AsyncIterable``'s own chunks unchanged, because
    re-slicing a ``bytes`` the caller already built would add a copy rather than remove one -- so
    there the peak is the caller's largest ``yield``, whatever that is, and a caller who yields
    their whole payload at once has already made it resident before this is reached. Either way
    this function's own overhead is one chunk, never the total.

    **The sibling limitation, so the two are not confused.** A *sync* ``Iterator[bytes]`` in a part
    hits the same ``read``-only demand from the other direction -- it can be pulled synchronously
    but carries no ``read`` at all -- and is answered by :class:`_ChunkReader`, a view rather than a
    file, because there is nothing to await and so nothing to drain. Same encoder constraint, two
    adapters, and which one applies is decided by whether the source needs an ``await``.

    Owning the encoder would retire both adapters and the loop-blocking with them. It was designed
    and declined: ``core/`` is vendored per SDK, so a bug in it ships everywhere and is fixable only
    by re-vendoring, and RFC 7578 escaping is the refusal that stops a CR/LF in a filename splicing
    a header into the body. If httpx ever grows an ``__aiter__`` that awaits, consume it -- do not
    write one (ADR-0051, ADR-0024).

    Why not the two other things that offer a synchronous ``read``. Accumulating into ``bytes`` is
    the defect this replaced -- it peaked at twice the source, once for the chunk list and once for
    the join. A ``SpooledTemporaryFile``'s ``fileno()`` forces a rollover to disk (measured), so it
    would reach disk for a ten-byte part *and* answer the encoder's length probe only by doing so;
    a plain temp file is smaller and needs no threshold to tune. Being a real file is also what
    keeps the part **sized**: the encoder reaches ``fstat`` through it, so this arm still contributes
    a ``Content-Length`` exactly as the resident ``bytes`` did, and stays re-sendable because it is
    seekable.

    A caller whose async source is a local file should hand over the ``Path`` instead: this arm
    then costs two reads and a write to move bytes that were already on disk in the right shape.
    Said in ``files.py``'s module docstring, where a caller reads it.

    Built from ``mkstemp`` rather than ``TemporaryFile`` so the object handed on is the same on
    every platform. ``TemporaryFile`` is an alias for ``NamedTemporaryFile`` wherever an open file
    cannot be unlinked -- Windows -- and that returns a wrapper proxying ``read`` through
    ``__getattr__``. A ``runtime_checkable`` protocol tests the *class*, so the wrapper does not
    satisfy :class:`BinaryReader`, and the part would fall through to the chunk-reader arm and go
    out chunked. Normalised here rather than branched on later.

    **Unlinked immediately where the platform allows it.** A POSIX file survives its own directory
    entry as long as a descriptor is open, so removing the name now leaves the content reachable
    through the handle and reclaimed by the kernel when the handle closes -- *including* if the
    process is killed, which is the one exit an ``ExitStack`` cannot unwind. Windows refuses to
    unlink an open file, so there the removal is deferred onto the stack instead. Probed rather than
    branched on ``os.name``: the question is what this filesystem permits, and the answer decides
    only *when* the name goes away.

    Args:
        chunks: The async source, normalised to an iterator of byte windows.
        stack: The send's exit stack, which closes the file -- and deletes it, where it could not be
            deleted up front -- when the send returns or raises.

    Returns:
        The file, positioned at 0 and ready for the encoder's own reads."""
    descriptor, path = mkstemp()
    # Registration order is the whole of the cleanup contract, and it reads backwards: an
    # ``ExitStack`` unwinds last-registered-first, so the removal goes on *before* the handle in
    # order to run *after* it. ``missing_ok`` is what lets the same callback stand whether or not
    # the immediate unlink below already won.
    stack.callback(Path(path).unlink, missing_ok=True)
    spill = stack.enter_context(os.fdopen(descriptor, "w+b"))
    with suppress(OSError):
        os.unlink(path)
    async for chunk in chunks:
        spill.write(chunk)
    spill.seek(0)
    return spill


async def _drained(part: MultipartPart, stack: ExitStack) -> MultipartPart:
    """Spill one part's content to a temp file if it is an async source, else hand it back unchanged.

    Args:
        part: The part to resolve.
        stack: The send's exit stack, owning any file opened for this part.

    Returns:
        The part, or a copy of it reading from the file its source was drained into."""
    if not isinstance(part, MultipartFile):
        return part
    if _is_async_reader(part.content):
        return replace(part, content=await _spilled(_awaited_chunks(part.content), stack))
    if isinstance(part.content, AsyncIterable):
        return replace(part, content=await _spilled(_aiter(part.content), stack))
    return part


async def _drained_parts(body: RequestBody | None, stack: ExitStack) -> RequestBody | None:
    """Resolve any async part content before the multipart body is encoded.

    The encoder pulls every part from a synchronous chunk generator in both flavours, so an
    awaitable source cannot be driven from inside it. Draining it here is what makes the arm work;
    :func:`_spilled` is what keeps it bounded. The loop stays free during the drain -- the source is
    awaited natively -- and is then occupied by the encode itself, which is httpx's synchronous
    generator and the one cost this leg still pays.

    Runs **inside** the send's ``ExitStack``, necessarily: it opens a file per async part, and those
    must unwind with everything else the send opened.

    Returns the body **unchanged** when nothing was drained, which is every multipart request whose
    parts are all sync arms.

    Args:
        body: The request's body, of any shape.
        stack: The send's exit stack.

    Returns:
        The body, or a multipart body whose async parts now read from a file."""
    if not isinstance(body, MultipartBody):
        return body
    parts = [await _drained(part, stack) for part in body.parts]
    # Identity, not equality: ``_drained`` hands an untouched part straight back, so ``is`` asks
    # exactly what this needs to know and cannot be answered by a part that merely compares equal.
    return body if all(new is old for new, old in zip(parts, body.parts, strict=True)) else MultipartBody(parts)


def _httpx_part(part: MultipartPart, stack: ExitStack) -> tuple[str, Any]:
    """Render one part in httpx's ``files=`` tuple spelling.

    Text parts go through the *file* spelling -- ``(None, text)``, a part with no filename --
    rather than through ``data=``, because httpx chooses the encoding on the **truthiness** of
    ``files``: an operation declaring ``multipart/form-data`` with no binary part would otherwise
    be sent as ``application/x-www-form-urlencoded``. The rendered bytes are identical either way,
    repeated keys and name escaping included, so the invariant costs nothing."""
    match part:
        case MultipartText(name, text, None):
            return (name, (None, text))
        case MultipartText(name, text, media_type):
            return (name, (None, text, media_type))
        case MultipartFile(name, content, filename, media_type):
            return (name, (filename, _open(content, stack), media_type))


def _body_kwargs(
    body: RequestBody | None,
    headers: Mapping[str, str],
    stack: ExitStack,
    *,
    binary_content: Callable[[AsyncBinaryContent, ExitStack], object],
) -> dict[str, Any]:
    """Map the request's body -- and the headers that describe it -- onto httpx's keywords.

    This ``match`` is the only place the body union is interpreted, and it is exhaustive by
    construction: adding a body shape without handling it here is a type error.

    Nothing here spells a media type, a charset or a filename. A body that has one carries it,
    written at the endpoint from the operation's content key, and it is merged **underneath** the
    request's own headers so a caller's ``extra_headers`` still wins -- the precedence httpx gives
    its own derived headers. A text body is encoded with the charset it declares and labelled with
    that same field, so the bytes and the label cannot disagree. A raw body that has a name -- given
    or derived, the factory having already settled which -- takes a second derived header, its
    ``Content-Disposition``, on that same precedence, and the nameless arm beneath it carries none
    rather than an empty one. That pair is ordered name-first because
    ``str()`` is what narrows the name for the renderer; the arm below is total over
    :class:`BinaryBody`, which is what keeps this ``match`` exhaustive. The two arms that carry no
    media type are the two whose media type belongs to the encoder: url-encoded is fixed by the
    ``data=`` keyword, and multipart's boundary exists only once httpx has minted it. That is why
    headers travel out of this function rather than beside it.

    ``binary_content`` is the one flavour-differing arm, passed as data with no default so each
    transport must name its own adapter -- ``_sync_content`` or ``_async_content``. One shared
    match rather than two sibling copies: this module is hand-written, where five duplicated arms
    to differ in one is drift risk rather than generator output.

    Args:
        body: The body being mapped -- the request's own, or the one :func:`_drained_parts`
            resolved from it.
        headers: The request's headers, which every arm carries through and two arms extend.
        stack: The send's exit stack, onto which any handle opened for this body is registered.
        binary_content: The flavour's raw-body adapter.

    Returns:
        The httpx keyword arguments carrying this body, ``headers`` among them."""
    match body:
        case None:
            return {"headers": headers}
        case JsonBody(None, media_type):
            # ``json=None`` is indistinguishable to httpx from no ``json`` argument at all, so the
            # body would vanish rather than going out as the four bytes the caller asked for.
            # ``content=`` is the only keyword that will carry them.
            return {"headers": {"content-type": media_type, **headers}, "content": b"null"}
        case JsonBody(value, media_type):
            return {"headers": {"content-type": media_type, **headers}, "json": value}
        case FormBody(fields):
            return {"headers": headers, "data": fields}
        case MultipartBody(parts):
            return {"headers": headers, "files": [_httpx_part(part, stack) for part in parts]}
        case BinaryBody(content, str() as filename, media_type):
            return {
                "headers": {
                    "content-type": media_type,
                    "content-disposition": render_content_disposition(filename),
                    **headers,
                },
                "content": binary_content(content, stack),
            }
        case BinaryBody(content, _, media_type):
            return {
                "headers": {"content-type": media_type, **headers},
                "content": binary_content(content, stack),
            }
        case TextBody(text, media_type, charset):
            return {
                "headers": {"content-type": f"{media_type}; charset={charset}", **headers},
                "content": text.encode(charset),
            }


def _timeout_kwargs(request: HttpRequest) -> dict[str, Any]:
    """Map a per-request timeout onto httpx's keyword, or contribute nothing.

    Omitting is deliberate rather than passing ``timeout=None``: to httpx that means *no timeout at
    all*, not *use the client's own*, so an absent override must not reach the call.

    Args:
        request: The request whose ``timeout`` is being mapped.

    Returns:
        ``{"timeout": ...}`` when the request set one, otherwise an empty mapping."""
    return {} if request.timeout is None else {"timeout": httpx.Timeout(request.timeout)}


@dataclass(frozen=True, slots=True)
class _HttpxStreamedResponse:
    """A thin veneer meeting :class:`StreamedResponse` over the library's own response.

    httpx lowercases header names on iteration, so ``headers`` meets the protocols' casing
    obligation by construction; ``read`` is the library's own, which both buffers the body and
    releases the connection -- the exact obligation the protocol states."""

    _response: httpx.Response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return dict(self._response.headers)

    def iter_bytes(self, chunk_size: int) -> Iterator[bytes]:
        return self._response.iter_bytes(chunk_size)

    def read(self) -> bytes:
        return self._response.read()

    def close(self) -> None:
        self._response.close()


@dataclass(frozen=True, slots=True)
class _AsyncHttpxStreamedResponse:
    """The awaited twin of :class:`_HttpxStreamedResponse`, meeting :class:`AsyncStreamedResponse`."""

    _response: httpx.Response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> Mapping[str, str]:
        return dict(self._response.headers)

    def aiter_bytes(self, chunk_size: int) -> AsyncIterator[bytes]:
        return self._response.aiter_bytes(chunk_size)

    async def aread(self) -> bytes:
        return await self._response.aread()

    async def aclose(self) -> None:
        await self._response.aclose()


class HttpxClient(HttpClient):
    """Sync transport backed by httpx.

    Uses connection pooling via a single ``httpx.Client``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.Client(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    def send(self, request: HttpRequest) -> HttpResponse:
        # The stack owns every handle opened for this body; a buffered send has fully consumed the
        # body by the time the response returns, so closing on exit is correct -- and an exception
        # mid-send closes on the unwind.
        with ExitStack() as stack:
            response = self._client.request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request.body, request.headers, stack, binary_content=_sync_content),
            )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
        )

    def stream(self, request: HttpRequest) -> StreamedResponse:
        # The stack closes once the head has arrived -- which is after the request body has been
        # sent in full, so closing there is correct, not early. The *response* body is pending;
        # the returned wrapper owns that connection until it is closed.
        with ExitStack() as stack:
            httpx_request = self._client.build_request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(request.body, request.headers, stack, binary_content=_sync_content),
            )
            response = self._client.send(httpx_request, stream=True)
        return _HttpxStreamedResponse(response)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._client.close()


class AsyncHttpxClient(AsyncHttpClient):
    """Async transport backed by httpx.

    Uses connection pooling via a single ``httpx.AsyncClient``, and returns buffered responses.

    Requests honour the standard proxy and TLS environment variables -- ``HTTP_PROXY`` /
    ``HTTPS_PROXY`` / ``ALL_PROXY`` / ``NO_PROXY`` (consulted only when ``proxy_url`` is unset) and
    ``SSL_CERT_FILE`` / ``SSL_CERT_DIR`` (the trust store). That is the underlying library's default
    rather than a decision made here, and it is stated because it is request behaviour the
    environment can change; a caller needing it off supplies a transport of their own.

    ``verify`` takes an ``ssl.SSLContext`` as well as a bool: a private CA bundle or a client
    certificate is configured by building one (``ssl.create_default_context(cafile=...)``), which is
    the one spelling the pinned library still supports for either."""

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        proxy_url: str | None = None,
        verify: ssl.SSLContext | bool = True,
    ) -> None:
        self._client = httpx.AsyncClient(
            proxy=proxy_url,
            timeout=httpx.Timeout(timeout),
            verify=verify,
        )
        self._closed = False

    async def send(self, request: HttpRequest) -> HttpResponse:
        with ExitStack() as stack:
            # Inside the stack, necessarily: the pre-pass opens a spill file per async part, and
            # those unwind with everything else this send opened.
            body = await _drained_parts(request.body, stack)
            response = await self._client.request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(body, request.headers, stack, binary_content=_async_content),
            )

        return HttpResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            content=response.content,
        )

    async def stream(self, request: HttpRequest) -> AsyncStreamedResponse:
        with ExitStack() as stack:
            body = await _drained_parts(request.body, stack)
            httpx_request = self._client.build_request(
                method=request.method,
                url=request.url,
                **_timeout_kwargs(request),
                **_body_kwargs(body, request.headers, stack, binary_content=_async_content),
            )
            response = await self._client.send(httpx_request, stream=True)
        return _AsyncHttpxStreamedResponse(response)

    async def aclose(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self._client.aclose()
