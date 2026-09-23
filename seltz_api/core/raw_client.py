"""The seams every endpoint crosses: build a request, send it, shape a result.

One pipeline, two flavors. :class:`BaseRawClient` holds the halves that do not depend on
concurrency -- resolving the API-wide, endpoint and caller parameter layers into a URL and headers,
and deciding whether a status code makes a :class:`Success` or a :class:`Failure` -- and each
concrete client adds only the transport-touching seams: ``execute`` for a buffered response,
``stream`` for one whose body stays unread. Both flavors spell both seams identically, so which
flavor is in play is carried by the client a caller holds rather than by a suffix on the method.

The two live in one module, with no ``async_raw_client.py`` beside it, because they are a peer pair:
the two lines they differ by -- resolving the auth scheme and sending -- are visible on one screen,
which is what keeps the sync and async paths from drifting apart."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from ._internal.headers import resolve_headers
from ._internal.urls import build_url, resolve_params
from .auth import AsyncAuthScheme, AuthParams, AuthScheme, invalidate, no_auth, resolve_auth
from .bodies import RequestBody
from .decoding import AsyncStreamDecoder, ErrorMapper, ResponseDecoder, StreamDecoder
from .params import Param, UrlTemplate
from .request_options import RequestOptions, RequestOptionsOrDict
from .results import ApiResult, Failure, Success
from .transport import (
    AsyncHttpClient,
    AsyncStreamedResponse,
    HttpClient,
    HttpRequest,
    HttpResponse,
    StreamedResponse,
)

T = TypeVar("T")
E = TypeVar("E")
TransportT = TypeVar("TransportT", bound=HttpClient | AsyncHttpClient)


@dataclass(frozen=True, slots=True)
class BaseRawClient(Generic[TransportT]):
    """Shared request-building and result-shaping for the raw clients.

    Holds the one transport its concurrency flavor can actually use -- the type
    parameter is what makes :class:`RawClient` provably sync and
    :class:`AsyncRawClient` provably async, so neither can be handed the other's
    transport. Subclasses add only the ``execute`` and ``stream`` seams, which differ
    solely by how they resolve the auth scheme and by ``send`` vs ``await …send``; the
    pipeline below is not duplicated and the sync/async boundary is never crossed.

    The three ``global_*`` fields carry the parameters the API applies to *every*
    request. They are derived from the API description, not from a caller: whoever
    generates this SDK writes them here, and an API that declares none leaves them
    empty. Each is combined with a single call's own parameters by the matching
    ``resolve_*`` function, so this class decides nothing about precedence -- it only
    says which two sides go in. All three are the same shape -- a sequence of
    parameters, each naming the type it was declared as -- which is what lets one
    ``param`` factory serve every location a request parameter can occupy, and what
    makes a wrongly-typed API-wide header a build failure rather than a wire bug.

    A single call's ``request_options`` is the third source: not what the API
    prescribes and not what the endpoint declares, but what the caller asked for this
    once. It is validated here, at the one place a request is built, so no emitted
    endpoint ever inspects an option.

    Authentication is a fourth source, and the full order for both headers and query parameters is::

        global_*  ->  the endpoint's own  ->  auth  ->  the caller's extra_headers

    Auth outranks the endpoint's own parameters because an operation parameter must not be able to
    clobber a credential, and loses to ``extra_headers`` because that is how a caller deliberately
    overrides one -- or blanks it, for a call meant to go out anonymous. Note that ``_build_request``
    takes already-resolved :class:`~.auth.AuthParams`, not a scheme: resolving a scheme may require
    I/O, so it happens in ``execute``, which is the one place the two flavors already differ.

    A **401 invalidates whatever the scheme cached**, so a credential the server revoked ahead of its
    own expiry is re-obtained on the next call rather than resent until it times out. For every scheme
    that holds a constant this is one ``isinstance`` and nothing more. The failing request is
    deliberately **not** retried: a caller sees one 401 and then recovery, which keeps this seam free
    of the retry policy ADR-0001 rules out. Like scheme resolution, it lives in ``execute`` --
    ``_build_result`` is a ``staticmethod`` that never sees the scheme."""

    http_client: TransportT
    global_headers: Sequence[Param[Any]] = ()
    global_query_params: Sequence[Param[Any]] = ()
    global_path_params: Sequence[Param[Any]] = ()

    def _build_request(
        self,
        *,
        http_method: str,
        url_template: UrlTemplate,
        path_params: Sequence[Param[Any]] | None,
        query_params: Sequence[Param[Any]] | None,
        headers: Sequence[Param[Any]] | None,
        body: RequestBody | None,
        auth: AuthParams,
        request_options: RequestOptionsOrDict | None,
    ) -> HttpRequest:
        options = RequestOptions.coerce(request_options)
        return HttpRequest(
            method=http_method,
            url=build_url(
                url_template,
                path_params=resolve_params(self.global_path_params, path_params),
                query_params=resolve_params(self.global_query_params, (*(query_params or ()), *auth.query_params)),
            ),
            headers=resolve_headers(
                self.global_headers,
                (*(headers or ()), *auth.request_headers()),
                extra_headers=options.extra_headers,
            ),
            body=body,
            timeout=options.timeout,
        )

    @staticmethod
    def _build_result(
        response: HttpResponse,
        *,
        decoder: ResponseDecoder[T],
        error_mapper: ErrorMapper[E],
    ) -> ApiResult[T, E]:
        """Shape a response into a result. 2xx succeeds, everything else fails.

        Every operation names a decoder -- an empty 2xx body is ``empty_response``, not an omitted
        argument -- so there is no "was one supplied?" branch here, and no empty-body special case
        either. ``T`` therefore means what it says: a declared ``ApiResult[T, E]`` yields a ``T``,
        and no cast or ``Any`` stands between the two.

        An operation that declares a payload and receives no body raises out of its decoder rather
        than quietly succeeding with ``None``, which is the rule every other
        response-deserialization failure already follows.

        Args:
            response: The response as the transport returned it.
            decoder: The operation's 2xx decoder; ``empty_response`` when it declares no body.
            error_mapper: The operation's error mapper; ``raw_error_response`` when it declares
                no error schemas.

        Returns:
            A :class:`Success` for a 2xx status, otherwise a :class:`Failure`.

        Raises:
            ValueError: If the body does not deserialize. A deserialization failure is not an API
                error, so it propagates in both response modes rather than becoming a failure."""
        if 200 <= response.status_code < 300:
            return Success(payload=decoder.decode(response), response=response)

        return Failure(error=error_mapper.map(response), response=response)


def _head_response(streamed: StreamedResponse | AsyncStreamedResponse) -> HttpResponse:
    # status/headers are synchronous properties on both streamed protocols, so one helper serves
    # both flavours. content stays b"": on a streamed success the body IS the payload.
    return HttpResponse(status_code=streamed.status_code, headers=dict(streamed.headers), content=b"")


@dataclass(frozen=True, slots=True)
class RawClient(BaseRawClient[HttpClient]):
    """Synchronous raw client: builds the request, sends it, shapes the result."""

    def execute(
        self,
        *,
        http_method: str,
        url_template: UrlTemplate,
        path_params: Sequence[Param[Any]] | None = None,
        query_params: Sequence[Param[Any]] | None = None,
        headers: Sequence[Param[Any]] | None = None,
        body: RequestBody | None = None,
        auth_scheme: AuthScheme = no_auth,
        decoder: ResponseDecoder[T],
        error_mapper: ErrorMapper[E],
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[T, E]:
        request = self._build_request(
            http_method=http_method,
            url_template=url_template,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            body=body,
            auth=auth_scheme.apply(),
            request_options=request_options,
        )
        response = self.http_client.send(request)
        if response.status_code == 401:
            invalidate(auth_scheme)
        return self._build_result(response, decoder=decoder, error_mapper=error_mapper)

    def stream(
        self,
        *,
        http_method: str,
        url_template: UrlTemplate,
        path_params: Sequence[Param[Any]] | None = None,
        query_params: Sequence[Param[Any]] | None = None,
        headers: Sequence[Param[Any]] | None = None,
        body: RequestBody | None = None,
        auth_scheme: AuthScheme = no_auth,
        decoder: StreamDecoder[T],
        error_mapper: ErrorMapper[E],
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[T, E]:
        """Send a request and return its body unread.

        The ``decoder`` receives the body **unread**, unlike a :class:`ResponseDecoder`, and the
        payload it builds owns the connection from that moment. A file names ``file_decoder``,
        which carries no subscript because a file bypasses the model layer; a payload type that
        varies per operation names it in a subscript, exactly as ``json_decoder[T]`` does. Either
        way ``T`` is solved from an argument, never from the declared return type.

        A non-2xx body is read in full and the connection released *before* the mapper runs, so an
        error schema deserializes exactly as it does on the buffered path and a :class:`Failure`
        never carries a lifetime obligation -- even when the error decoder itself raises. A
        :class:`Success` owns the connection through its payload; see *File lifetime* in
        docs/plans/file-handling.md.

        Args:
            http_method: The HTTP verb to send.
            url_template: The unresolved URL for the configured environment.
            path_params: The endpoint's path parameters, if any.
            query_params: The endpoint's query parameters, if any.
            headers: The endpoint's header parameters, if any.
            body: The request body, already wire-ready, or ``None``.
            auth_scheme: The scheme the operation declares; ``no_auth`` when it declares none.
            decoder: The operation's streamed-payload decoder; ``file_decoder`` for a file.
            error_mapper: The operation's error mapper; ``raw_error_response`` when it declares
                no error schemas.
            request_options: The caller's per-call overrides, if any.

        Returns:
            A :class:`Success` carrying the payload built over the unread body for a 2xx status,
            otherwise a :class:`Failure` carrying the decoded error body."""
        request = self._build_request(
            http_method=http_method,
            url_template=url_template,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            body=body,
            auth=auth_scheme.apply(),
            request_options=request_options,
        )
        streamed = self.http_client.stream(request)
        try:
            if streamed.status_code == 401:
                invalidate(auth_scheme)
            if 200 <= streamed.status_code < 300:
                # The 2xx return exits the try without running else: the connection now belongs to
                # the payload the decoder builds. A decoder that raises instead is caught below, which
                # is why nothing on this line has to be total.
                return Success(payload=decoder.decode(streamed, request.url), response=_head_response(streamed))
            # Buffered once, then shared by both Failure fields -- re-reading a consumed stream
            # raises, and read is what both releases the connection and preserves the bytes.
            buffered = HttpResponse(
                status_code=streamed.status_code,
                headers=dict(streamed.headers),
                content=streamed.read(),
            )
        except BaseException:
            streamed.close()
            raise
        else:
            streamed.close()
        # Mapped AFTER the close, so a decoder raise cannot leak -- a Failure never holds a
        # connection.
        return Failure(error=error_mapper.map(buffered), response=buffered)


@dataclass(frozen=True, slots=True)
class AsyncRawClient(BaseRawClient[AsyncHttpClient]):
    """Asynchronous raw client.

    The method is named ``execute``, not ``execute_async``: sync and async peers
    carry identical names throughout this SDK, and the transport already makes the
    flavor unambiguous."""

    async def execute(
        self,
        *,
        http_method: str,
        url_template: UrlTemplate,
        path_params: Sequence[Param[Any]] | None = None,
        query_params: Sequence[Param[Any]] | None = None,
        headers: Sequence[Param[Any]] | None = None,
        body: RequestBody | None = None,
        auth_scheme: AsyncAuthScheme = no_auth,
        decoder: ResponseDecoder[T],
        error_mapper: ErrorMapper[E],
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[T, E]:
        request = self._build_request(
            http_method=http_method,
            url_template=url_template,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            body=body,
            auth=await resolve_auth(auth_scheme),
            request_options=request_options,
        )
        response = await self.http_client.send(request)
        if response.status_code == 401:
            invalidate(auth_scheme)
        return self._build_result(response, decoder=decoder, error_mapper=error_mapper)

    async def stream(
        self,
        *,
        http_method: str,
        url_template: UrlTemplate,
        path_params: Sequence[Param[Any]] | None = None,
        query_params: Sequence[Param[Any]] | None = None,
        headers: Sequence[Param[Any]] | None = None,
        body: RequestBody | None = None,
        auth_scheme: AsyncAuthScheme = no_auth,
        decoder: AsyncStreamDecoder[T],
        error_mapper: ErrorMapper[E],
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[T, E]:
        """Send a request and return its body unread; the awaited twin of ``RawClient.stream``.

        The same contract, with the same two-line delta ``execute`` already has: the auth scheme
        is resolved rather than applied, and the transport is awaited.

        Args:
            http_method: The HTTP verb to send.
            url_template: The unresolved URL for the configured environment.
            path_params: The endpoint's path parameters, if any.
            query_params: The endpoint's query parameters, if any.
            headers: The endpoint's header parameters, if any.
            body: The request body, already wire-ready, or ``None``.
            auth_scheme: The scheme the operation declares; ``no_auth`` when it declares none.
            decoder: The operation's streamed-payload decoder; ``async_file_decoder`` for a file.
            error_mapper: The operation's error mapper; ``raw_error_response`` when it declares
                no error schemas.
            request_options: The caller's per-call overrides, if any.

        Returns:
            A :class:`Success` carrying the payload built over the unread body for a 2xx status,
            otherwise a :class:`Failure` carrying the decoded error body."""
        request = self._build_request(
            http_method=http_method,
            url_template=url_template,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            body=body,
            auth=await resolve_auth(auth_scheme),
            request_options=request_options,
        )
        streamed = await self.http_client.stream(request)
        try:
            if streamed.status_code == 401:
                invalidate(auth_scheme)
            if 200 <= streamed.status_code < 300:
                # The 2xx return exits the try without running else: the connection now belongs to
                # the payload the decoder builds. A decoder that raises instead is caught below, which
                # is why nothing on this line has to be total.
                return Success(payload=decoder.decode(streamed, request.url), response=_head_response(streamed))
            # Buffered once, then shared by both Failure fields -- re-reading a consumed stream
            # raises, and aread is what both releases the connection and preserves the bytes.
            buffered = HttpResponse(
                status_code=streamed.status_code,
                headers=dict(streamed.headers),
                content=await streamed.aread(),
            )
        except BaseException:
            await streamed.aclose()
            raise
        else:
            await streamed.aclose()
        # Mapped AFTER the close, so a decoder raise cannot leak -- a Failure never holds a
        # connection.
        return Failure(error=error_mapper.map(buffered), response=buffered)


RawClientT = TypeVar("RawClientT", bound=RawClient | AsyncRawClient)
"""Fixes which raw client a generic holder carries -- ``RawClient`` or ``AsyncRawClient``.

Bounded by the two concrete clients rather than by ``BaseRawClient[Any]``: the base defines only
the request/result pipeline, not ``execute``, so the looser bound could not prove that a holder's
``self._client.execute(...)`` exists -- it type-checked only because each subclass substitutes a
concrete argument. This bound also removes the ``Any``."""
