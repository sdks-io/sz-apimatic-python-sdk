"""Turning wire bytes into typed values: response decoding and error-body mapping.

One verb per act, and they are not interchangeable. ``decode`` turns a 2xx body into its typed
payload: it is the method a :class:`ResponseDecoder` carries, built by the ``*_decoder``
factories for an endpoint that has not sent its request yet, and run in one step by the
``decode_*`` helpers for a response already in hand -- ``decode_json[t](response)`` is
``json_decoder[t].decode(response)``.

``map`` is the error path's act, because there the work is **selection**: an :class:`ErrorMapper`
picks the documented schema for a response's status, and each generated error module's ``match``
on ``response.status_code`` is that mapping written out.

The decoders below resolve their adapter through :func:`adapter_for`, the single cache the request
path (``json_body``, ``param``) draws from too.

Every factory here takes its target type in its subscript, as a ``TypeForm[T]`` (PEP 747) rather
than a ``type[T]``. That is what keeps ``T`` precise for the type expressions no class can stand in
for -- a union alias, an ``Annotated`` wire-format alias, a ``list[...]``/``dict[...]`` wrapper --
and so what lets a type checker compare an endpoint's *declared* payload type against the type it
actually parses. A ``type[T]``-plus-``object`` overload pair cannot: given a declared type the
precise overload does not fit, inference falls through to the ``object`` one, yields ``Any``, and
the disagreement has nowhere left to surface.

Not every decoder is subscripted: :data:`empty_response` is a shared singleton for an operation
with no 2xx body, mirroring :data:`raw_error_response` on the error side, and :data:`file_decoder`
is one for an operation whose body is a file. None of the three has a type to name. Between them,
every argument ``execute`` and ``stream`` need is always written out, so a payload type is never
left to be inferred from the surrounding declaration.

There are two decoder families, told apart by what they receive. A :class:`ResponseDecoder` takes a
buffered :class:`HttpResponse` whose ``content`` is already in memory; a :class:`StreamDecoder`
takes the still-open :class:`StreamedResponse` and hands the connection to the value it builds. So a
streamed payload cannot be produced by the buffered protocol at all, which is why ``stream`` names
its decoder from the second family."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, Generic, Protocol, TypeVar

from pydantic import TypeAdapter
from typing_extensions import TypeForm

from .adapters import adapter_for
from .file_responses import AsyncFileResponse, FileResponse
from .results import RawError
from .transport import AsyncStreamedResponse, HttpResponse, StreamedResponse

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
E_co = TypeVar("E_co", covariant=True)


class ResponseDecoder(Protocol[T_co]):
    """Decodes a 2xx response into the operation's typed success payload."""

    def decode(self, response: HttpResponse) -> T_co: ...


class ErrorMapper(Protocol[E_co]):
    """Maps a non-2xx response to the operation's typed error body -- a union of the
    documented error schemas, or ``RawError`` for an unmapped status."""

    def map(self, response: HttpResponse) -> E_co: ...


class StreamDecoder(Protocol[T_co]):
    """Builds a 2xx payload from a body that has not been read.

    The lazy counterpart of :class:`ResponseDecoder`, and a sibling rather than a subtype: that one
    receives a buffered :class:`HttpResponse` whose ``content`` is already in memory, this one
    receives the open :class:`StreamedResponse` and hands the connection to the value it returns.

    ``decode`` is synchronous in both flavours -- building the payload never touches the wire, and
    the awaiting happens when a caller consumes it."""

    def decode(self, streamed: StreamedResponse, url: str) -> T_co: ...


class AsyncStreamDecoder(Protocol[T_co]):
    """Builds a 2xx payload from an unread async body; the twin of :class:`StreamDecoder`.

    A twin rather than one protocol over both streamed types, because the two are what make the
    flavours non-interchangeable: an argument position is contravariant, so a decoder over an
    :class:`AsyncStreamedResponse` cannot satisfy :class:`StreamDecoder`, and the sync seam can
    never be handed the async decoder."""

    def decode(self, streamed: AsyncStreamedResponse, url: str) -> T_co: ...


@dataclass(frozen=True, slots=True)
class JsonDecoder(Generic[T]):
    """Decodes a JSON body (object, array or scalar) through ``adapter``."""

    adapter: TypeAdapter[T]

    def decode(self, response: HttpResponse) -> T:
        return self.adapter.validate_python(response.json())


@dataclass(frozen=True, slots=True)
class TextDecoder(Generic[T]):
    """Decodes a plain-text body through ``adapter``."""

    adapter: TypeAdapter[T]

    def decode(self, response: HttpResponse) -> T:
        return self.adapter.validate_python(response.text(errors="strict"))


class _JsonDecoderFactory:
    """``json_decoder[T]`` -- build a decoder that reads a JSON body as the subscripted type.

    The subscript is a ``TypeForm``, so a runtime union alias (``Person``, which is
    ``Employee | Boss``) is as acceptable as a concrete class and ``T`` is precise for either.
    That precision is what makes an endpoint's declared payload type checkable against what it
    decodes. And because the factory declares no ``__call__``, the type cannot be omitted
    (``[operator]``); its runtime ``__call__`` is checker-invisible and only guides."""

    def __getitem__(self, declared: TypeForm[T]) -> ResponseDecoder[T]:
        return JsonDecoder(adapter_for(declared))

    if not TYPE_CHECKING:

        def __call__(self, *args, **kwargs):
            raise TypeError(
                "json_decoder is not called -- subscript it with the payload type: "
                "decoder=json_decoder[T], e.g. json_decoder[Person]"
            )


class _TextDecoderFactory:
    """``text_decoder[T]`` -- build a decoder reading a plain-text body; see ``json_decoder``."""

    def __getitem__(self, declared: TypeForm[T]) -> ResponseDecoder[T]:
        return TextDecoder(adapter_for(declared))

    if not TYPE_CHECKING:

        def __call__(self, *args, **kwargs):
            raise TypeError(
                "text_decoder is not called -- subscript it with the payload type: "
                "decoder=text_decoder[T], e.g. text_decoder[int]"
            )


class _DecodeJsonFactory:
    """``decode_json[T](response)`` -- decode a JSON body as the subscripted type, now.

    The result is typed as the subscripted type whatever shape it takes -- a concrete class, a
    union such as ``Accountant | Manager``, an ``Annotated`` alias -- so a generated error mapper
    returns its documented body union directly, with no ``cast`` standing in for what the type
    system now carries itself."""

    def __getitem__(self, declared: TypeForm[T]) -> Callable[[HttpResponse], T]:
        return JsonDecoder(adapter_for(declared)).decode

    if not TYPE_CHECKING:

        def __call__(self, *args, **kwargs):
            raise TypeError(
                "decode_json is not called directly -- name the body type in its subscript: decode_json[T](response)"
            )


class _DecodeTextFactory:
    """``decode_text[T](response)`` -- decode a plain-text body, now; see ``decode_json``.

    Also callable bare -- ``decode_text(response)`` -- which is the ``str`` default the retired
    two-member overload existed to carry: the default lives on ``__call__`` and a named type can
    only take the subscript path, so a mismatch has nowhere to fall through to."""

    def __getitem__(self, declared: TypeForm[T]) -> Callable[[HttpResponse], T]:
        return TextDecoder(adapter_for(declared)).decode

    def __call__(self, response: HttpResponse) -> str:
        return self[str](response)


json_decoder: Final = _JsonDecoderFactory()
text_decoder: Final = _TextDecoderFactory()
decode_json: Final = _DecodeJsonFactory()
decode_text: Final = _DecodeTextFactory()


@dataclass(frozen=True, slots=True)
class EmptyResponse:
    """Response decoder for an operation whose 2xx body is empty.

    The success-side counterpart of :class:`RawErrorResponse`, and the reason ``decoder`` is a
    required argument rather than an optional one: an operation that returns no content says so by
    naming this, instead of by leaving the argument out. Presence is auditable where absence is
    not -- a missing ``decoder=`` could be a no-content operation or a generator that dropped the
    line, and only one of those should compile.

    Naming it is also what keeps the payload type honest. ``T`` is solved from this argument, so the
    operation can declare ``ApiResult[None, E]`` and nothing else. Were the argument omitted
    instead, ``T`` would be solved from the declared type, and an operation that parses nothing
    could claim any payload it liked and hand back ``None`` at runtime -- the last place a declared
    type could go unstated, now that each factory makes its own subscript mandatory.

    Not subscripted, and not a factory: there is no type to name. ``json_decoder[None]`` would still
    parse the body and raise on an empty one, which is the opposite of what this does.

    Carries nothing SDK-specific, so it lives here rather than in the generated error layer, and is
    shared by every such operation."""

    def decode(self, response: HttpResponse) -> None:
        return None


empty_response: Final[ResponseDecoder[None]] = EmptyResponse()


@dataclass(frozen=True, slots=True)
class RawErrorResponse:
    """Error mapper for an operation that declares no error schemas.

    Deliberately has **no** ``match`` on the status code: the absence is the
    signal. Where an operation's spec documents error responses, its own mapper
    in the generated error layer selects a schema per status; where it documents
    none there is nothing to select, so every non-2xx response maps to the same
    :class:`RawError` -- status plus the undecoded body, decoded on demand.

    Carries nothing SDK-specific, so it lives here rather than in the generated
    error layer, and is shared by every such operation."""

    def map(self, response: HttpResponse) -> RawError:
        return RawError(response)


raw_error_response: Final[ErrorMapper[RawError]] = RawErrorResponse()


@dataclass(frozen=True, slots=True)
class FileDecoder:
    """Stream decoder for an operation whose 2xx body is a file.

    Not subscripted, and not a factory: a file bypasses the model layer, so there is no adapter to
    name -- the same absence that leaves ``file_part`` unsubscripted on the request side.

    Naming it is what keeps the payload solved from an *argument* rather than from the seam's own
    return type, which is what lets a second streamed payload shape join ``stream`` instead of
    forking it. ``url`` is carried in because a :class:`StreamedResponse` does not know it and the
    payload reports it when abandoned."""

    def decode(self, streamed: StreamedResponse, url: str) -> FileResponse:
        return FileResponse(streamed, url)


file_decoder: Final[StreamDecoder[FileResponse]] = FileDecoder()


@dataclass(frozen=True, slots=True)
class AsyncFileDecoder:
    """Stream decoder for an operation whose 2xx body is a file; the twin of :class:`FileDecoder`."""

    def decode(self, streamed: AsyncStreamedResponse, url: str) -> AsyncFileResponse:
        return AsyncFileResponse(streamed, url)


async_file_decoder: Final[AsyncStreamDecoder[AsyncFileResponse]] = AsyncFileDecoder()
