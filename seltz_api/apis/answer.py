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
from ..errors.answer_error import AnswerErrorBody, answer_error_mapper
from ..models.answer_http_request import AnswerHttpRequest, AnswerHttpRequestDict
from ..models.answer_http_response import AnswerHttpResponse
from ..server.server import Server


class Answer:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AnswerWithRawResponse(client, server, auth)

    def answer(
        self, body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnswerHttpResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Answer for the query. When ``stream = false`` the body is a JSON ``AnswerHttpResponse``; when ``stream =
            true`` it is a ``text/event-stream`` of OpenAI-style chunks.

        Raises:
            ApiError: Missing or malformed request fields. Invalid or missing API key. Insufficient credits. Endpoint
                not found, or a scope that matches nothing. Wrong method for this endpoint. The answer did not complete
                in time. Request body is too large. ``Content-Type`` is not ``application/json``. Rate limit exceeded.
                Wait before retrying. Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.answer(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AnswerWithRawResponse:
        return self._with_raw_response


class AsyncAnswer:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAnswerWithRawResponse(client, server, auth)

    async def answer(
        self, body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnswerHttpResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Answer for the query. When ``stream = false`` the body is a JSON ``AnswerHttpResponse``; when ``stream =
            true`` it is a ``text/event-stream`` of OpenAI-style chunks.

        Raises:
            ApiError: Missing or malformed request fields. Invalid or missing API key. Insufficient credits. Endpoint
                not found, or a scope that matches nothing. Wrong method for this endpoint. The answer did not complete
                in time. Request body is too large. ``Content-Type`` is not ``application/json``. Rate limit exceeded.
                Wait before retrying. Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.answer(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAnswerWithRawResponse:
        return self._with_raw_response


class AnswerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def answer(
        self, body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnswerHttpResponse, AnswerErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/answer"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AnswerHttpRequest | AnswerHttpRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AnswerHttpResponse],
            error_mapper=answer_error_mapper,
            request_options=request_options,
        )


class AsyncAnswerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def answer(
        self, body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnswerHttpResponse, AnswerErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/answer"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AnswerHttpRequest | AnswerHttpRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AnswerHttpResponse],
            error_mapper=answer_error_mapper,
            request_options=request_options,
        )
