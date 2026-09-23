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
from ..errors.search_error import SearchErrorBody, search_error_mapper
from ..models.search_request import SearchRequest, SearchRequestDict
from ..models.search_response import SearchResponse
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server, auth)

    def search(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Search completed. Returns matched documents.

        Raises:
            ApiError: Missing or malformed request fields. Invalid or missing API key. Insufficient credits. Endpoint
                not found, or a scope that matches nothing. Wrong method for this endpoint. Request body is too large.
                Rate limit exceeded. Wait before retrying. Unexpected server error. ``error`` is ``ErrorEnvelope |
                RawError``."""
        return self._with_raw_response.search(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server, auth)

    async def search(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Search completed. Returns matched documents.

        Raises:
            ApiError: Missing or malformed request fields. Invalid or missing API key. Insufficient credits. Endpoint
                not found, or a scope that matches nothing. Wrong method for this endpoint. Request body is too large.
                Rate limit exceeded. Wait before retrying. Unexpected server error. ``error`` is ``ErrorEnvelope |
                RawError``."""
        return (await self._with_raw_response.search(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchResponse, SearchErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchRequest | SearchRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SearchResponse],
            error_mapper=search_error_mapper,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchResponse, SearchErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchRequest | SearchRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SearchResponse],
            error_mapper=search_error_mapper,
            request_options=request_options,
        )
