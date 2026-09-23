from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.fetch_error import FetchErrorBody, fetch_error_mapper
from ..models.fetch_request import FetchRequest, FetchRequestDict
from ..models.fetch_response import FetchResponse
from ..server.server import Server


class Fetch:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FetchWithRawResponse(client, server, auth)

    def fetch(
        self, body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> FetchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            One result per requested URL. A failure to fetch a page is still a 200, with that result's ``status =
            "error"``.

        Raises:
            ApiError: Malformed body, an out-of-bounds or duplicated ``urls`` entry, or an unavailable ``formats`` or
                ``tier`` value. Unrecognized fields are ignored. Invalid or missing API key. Insufficient credits. Rate
                limited. Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.fetch(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> FetchWithRawResponse:
        return self._with_raw_response


class AsyncFetch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFetchWithRawResponse(client, server, auth)

    async def fetch(
        self, body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> FetchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            One result per requested URL. A failure to fetch a page is still a 200, with that result's ``status =
            "error"``.

        Raises:
            ApiError: Malformed body, an out-of-bounds or duplicated ``urls`` entry, or an unavailable ``formats`` or
                ``tier`` value. Unrecognized fields are ignored. Invalid or missing API key. Insufficient credits. Rate
                limited. Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.fetch(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncFetchWithRawResponse:
        return self._with_raw_response


class FetchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fetch(
        self, body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FetchResponse, FetchErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/fetch"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FetchRequest | FetchRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[FetchResponse],
            error_mapper=fetch_error_mapper,
            request_options=request_options,
        )


class AsyncFetchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fetch(
        self, body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FetchResponse, FetchErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/fetch"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FetchRequest | FetchRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[FetchResponse],
            error_mapper=fetch_error_mapper,
            request_options=request_options,
        )
