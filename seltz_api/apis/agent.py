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
from ..errors.cancel_agent_run_error import CancelAgentRunErrorBody, cancel_agent_run_error_mapper
from ..errors.create_agent_run_error import CreateAgentRunErrorBody, create_agent_run_error_mapper
from ..errors.get_agent_run_error import GetAgentRunErrorBody, get_agent_run_error_mapper
from ..errors.list_agent_runs_error import ListAgentRunsErrorBody, list_agent_runs_error_mapper
from ..models.agent_run import AgentRun
from ..models.create_agent_run_request import CreateAgentRunRequest, CreateAgentRunRequestDict
from ..models.list_agent_runs_response import ListAgentRunsResponse
from ..server.server import Server


class Agent:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AgentWithRawResponse(client, server, auth)

    def cancel_agent_run(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun:
        """Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe
        to retry.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run.

        Raises:
            ApiError: Invalid or missing API key. No such run in this org. Unexpected server error. ``error`` is
                ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.cancel_agent_run(id, request_options=request_options).unwrap()

    def create_agent_run(
        self,
        body: CreateAgentRunRequest | CreateAgentRunRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentRun:
        """Returns the new run in ``pending`` state. Poll it by id until ``status`` reaches a terminal state.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The new run, in ``pending`` state.

        Raises:
            ApiError: Malformed body, unknown field, unknown ``effort``, or a rejected ``output_schema``. Invalid or
                missing API key. Insufficient credits. Unexpected server error. ``error`` is ``ErrorEnvelope |
                RawError``."""
        return self._with_raw_response.create_agent_run(body, request_options=request_options).unwrap()

    def get_agent_run(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun:
        """Poll until ``status`` reaches a terminal state.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run.

        Raises:
            ApiError: Invalid or missing API key. No such run in this org. Unexpected server error. ``error`` is
                ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.get_agent_run(id, request_options=request_options).unwrap()

    def list_agent_runs(
        self, *, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentRunsResponse:
        """The organization's runs, newest first. Pass one page's ``next`` as the following request's ``after``.

        Args:
            limit: Page size, 1-100. Defaults to 20.
            after: Pagination cursor: the previous page's ``next``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            One page of runs, newest first.

        Raises:
            ApiError: Malformed or unknown query parameter. Invalid or missing API key. Unknown ``after`` cursor.
                Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_agent_runs(
            limit=limit, after=after, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AgentWithRawResponse:
        return self._with_raw_response


class AsyncAgent:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAgentWithRawResponse(client, server, auth)

    async def cancel_agent_run(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun:
        """Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe
        to retry.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run.

        Raises:
            ApiError: Invalid or missing API key. No such run in this org. Unexpected server error. ``error`` is
                ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.cancel_agent_run(id, request_options=request_options)).unwrap()

    async def create_agent_run(
        self,
        body: CreateAgentRunRequest | CreateAgentRunRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentRun:
        """Returns the new run in ``pending`` state. Poll it by id until ``status`` reaches a terminal state.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The new run, in ``pending`` state.

        Raises:
            ApiError: Malformed body, unknown field, unknown ``effort``, or a rejected ``output_schema``. Invalid or
                missing API key. Insufficient credits. Unexpected server error. ``error`` is ``ErrorEnvelope |
                RawError``."""
        return (await self._with_raw_response.create_agent_run(body, request_options=request_options)).unwrap()

    async def get_agent_run(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun:
        """Poll until ``status`` reaches a terminal state.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run.

        Raises:
            ApiError: Invalid or missing API key. No such run in this org. Unexpected server error. ``error`` is
                ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.get_agent_run(id, request_options=request_options)).unwrap()

    async def list_agent_runs(
        self, *, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentRunsResponse:
        """The organization's runs, newest first. Pass one page's ``next`` as the following request's ``after``.

        Args:
            limit: Page size, 1-100. Defaults to 20.
            after: Pagination cursor: the previous page's ``next``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            One page of runs, newest first.

        Raises:
            ApiError: Malformed or unknown query parameter. Invalid or missing API key. Unknown ``after`` cursor.
                Unexpected server error. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_agent_runs(limit=limit, after=after, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAgentWithRawResponse:
        return self._with_raw_response


class AgentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_agent_run(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentRun, CancelAgentRunErrorBody]:
        """Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe
        to retry.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/agent/runs/{id}/cancel"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=cancel_agent_run_error_mapper,
            request_options=request_options,
        )

    def create_agent_run(
        self,
        body: CreateAgentRunRequest | CreateAgentRunRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentRun, CreateAgentRunErrorBody]:
        """Returns the new run in ``pending`` state. Poll it by id until ``status`` reaches a terminal state.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/agent/runs"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentRunRequest | CreateAgentRunRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=create_agent_run_error_mapper,
            request_options=request_options,
        )

    def get_agent_run(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentRun, GetAgentRunErrorBody]:
        """Poll until ``status`` reaches a terminal state.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/runs/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=get_agent_run_error_mapper,
            request_options=request_options,
        )

    def list_agent_runs(
        self, *, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentRunsResponse, ListAgentRunsErrorBody]:
        """The organization's runs, newest first. Pass one page's ``next`` as the following request's ``after``.

        Args:
            limit: Page size, 1-100. Defaults to 20.
            after: Pagination cursor: the previous page's ``next``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/runs"),
            query_params=[param[int | None]("limit", limit), param[str | None]("after", after)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListAgentRunsResponse],
            error_mapper=list_agent_runs_error_mapper,
            request_options=request_options,
        )


class AsyncAgentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_agent_run(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentRun, CancelAgentRunErrorBody]:
        """Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe
        to retry.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/agent/runs/{id}/cancel"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=cancel_agent_run_error_mapper,
            request_options=request_options,
        )

    async def create_agent_run(
        self,
        body: CreateAgentRunRequest | CreateAgentRunRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentRun, CreateAgentRunErrorBody]:
        """Returns the new run in ``pending`` state. Poll it by id until ``status`` reaches a terminal state.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/agent/runs"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentRunRequest | CreateAgentRunRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=create_agent_run_error_mapper,
            request_options=request_options,
        )

    async def get_agent_run(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentRun, GetAgentRunErrorBody]:
        """Poll until ``status`` reaches a terminal state.

        Args:
            id: The run id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/runs/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentRun],
            error_mapper=get_agent_run_error_mapper,
            request_options=request_options,
        )

    async def list_agent_runs(
        self, *, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentRunsResponse, ListAgentRunsErrorBody]:
        """The organization's runs, newest first. Pass one page's ``next`` as the following request's ``after``.

        Args:
            limit: Page size, 1-100. Defaults to 20.
            after: Pagination cursor: the previous page's ``next``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/runs"),
            query_params=[param[int | None]("limit", limit), param[str | None]("after", after)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListAgentRunsResponse],
            error_mapper=list_agent_runs_error_mapper,
            request_options=request_options,
        )
