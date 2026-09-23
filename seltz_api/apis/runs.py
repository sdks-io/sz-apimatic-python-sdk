from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_run_error import GetRunErrorBody, get_run_error_mapper
from ..errors.list_run_requests_error import ListRunRequestsErrorBody, list_run_requests_error_mapper
from ..errors.list_runs_error import ListRunsErrorBody, list_runs_error_mapper
from ..models.get_run_response import GetRunResponse
from ..models.list_run_requests_response import ListRunRequestsResponse
from ..models.list_runs_response import ListRunsResponse
from ..server.server import Server


class Runs:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RunsWithRawResponse(client, server, auth)

    def get_run(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetRunResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run. Carries no records and no breakdown.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.get_run(monitor_id, run_id, request_options=request_options).unwrap()

    def list_run_requests(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListRunRequestsResponse:
        """The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a
        stream of positives, and absence cannot be inferred from presences.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            That run's per-request outcomes.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_run_requests(monitor_id, run_id, request_options=request_options).unwrap()

    def list_runs(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRunsResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``run_id``.
            before: Exclusive upper bound on ``run_id``.
            limit: Defaults to 100, at most 1,000.
            sort: ``desc`` (the default, newest first) or ``asc``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of runs.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_runs(
            monitor_id, since=since, before=before, limit=limit, sort=sort, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> RunsWithRawResponse:
        return self._with_raw_response


class AsyncRuns:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRunsWithRawResponse(client, server, auth)

    async def get_run(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetRunResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The run. Carries no records and no breakdown.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.get_run(monitor_id, run_id, request_options=request_options)).unwrap()

    async def list_run_requests(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListRunRequestsResponse:
        """The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a
        stream of positives, and absence cannot be inferred from presences.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            That run's per-request outcomes.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_run_requests(monitor_id, run_id, request_options=request_options)
        ).unwrap()

    async def list_runs(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRunsResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``run_id``.
            before: Exclusive upper bound on ``run_id``.
            limit: Defaults to 100, at most 1,000.
            sort: ``desc`` (the default, newest first) or ``asc``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of runs.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_runs(
                monitor_id, since=since, before=before, limit=limit, sort=sort, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRunsWithRawResponse:
        return self._with_raw_response


class RunsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_run(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetRunResponse, GetRunErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetRunResponse],
            error_mapper=get_run_error_mapper,
            request_options=request_options,
        )

    def list_run_requests(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListRunRequestsResponse, ListRunRequestsErrorBody]:
        """The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a
        stream of positives, and absence cannot be inferred from presences.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}/requests"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunRequestsResponse],
            error_mapper=list_run_requests_error_mapper,
            request_options=request_options,
        )

    def list_runs(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRunsResponse, ListRunsErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``run_id``.
            before: Exclusive upper bound on ``run_id``.
            limit: Defaults to 100, at most 1,000.
            sort: ``desc`` (the default, newest first) or ``asc``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs"),
            path_params=[param[str]("monitor_id", monitor_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[str | None]("sort", sort),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunsResponse],
            error_mapper=list_runs_error_mapper,
            request_options=request_options,
        )


class AsyncRunsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_run(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetRunResponse, GetRunErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetRunResponse],
            error_mapper=get_run_error_mapper,
            request_options=request_options,
        )

    async def list_run_requests(
        self, monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListRunRequestsResponse, ListRunRequestsErrorBody]:
        """The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a
        stream of positives, and absence cannot be inferred from presences.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}/requests"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunRequestsResponse],
            error_mapper=list_run_requests_error_mapper,
            request_options=request_options,
        )

    async def list_runs(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        sort: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRunsResponse, ListRunsErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``run_id``.
            before: Exclusive upper bound on ``run_id``.
            limit: Defaults to 100, at most 1,000.
            sort: ``desc`` (the default, newest first) or ``asc``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs"),
            path_params=[param[str]("monitor_id", monitor_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[str | None]("sort", sort),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunsResponse],
            error_mapper=list_runs_error_mapper,
            request_options=request_options,
        )
