from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.list_records_error import ListRecordsErrorBody, list_records_error_mapper
from ..errors.list_run_records_error import ListRunRecordsErrorBody, list_run_records_error_mapper
from ..models.list_records_response import ListRecordsResponse
from ..models.list_run_records_response import ListRunRecordsResponse
from ..server.server import Server


class Records:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RecordsWithRawResponse(client, server, auth)

    def list_records(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordsResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of records.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_records(
            monitor_id,
            since=since,
            before=before,
            limit=limit,
            include_content=include_content,
            request_options=request_options,
        ).unwrap()

    def list_run_records(
        self,
        monitor_id: str,
        run_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRunRecordsResponse:
        """Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound,
        not a dense sequence.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of that run's records.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_run_records(
            monitor_id,
            run_id,
            since=since,
            before=before,
            limit=limit,
            include_content=include_content,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> RecordsWithRawResponse:
        return self._with_raw_response


class AsyncRecords:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRecordsWithRawResponse(client, server, auth)

    async def list_records(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRecordsResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of records.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_records(
                monitor_id,
                since=since,
                before=before,
                limit=limit,
                include_content=include_content,
                request_options=request_options,
            )
        ).unwrap()

    async def list_run_records(
        self,
        monitor_id: str,
        run_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRunRecordsResponse:
        """Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound,
        not a dense sequence.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A page of that run's records.

        Raises:
            ApiError: No such run on this monitor. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_run_records(
                monitor_id,
                run_id,
                since=since,
                before=before,
                limit=limit,
                include_content=include_content,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRecordsWithRawResponse:
        return self._with_raw_response


class RecordsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_records(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordsResponse, ListRecordsErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/records"),
            path_params=[param[str]("monitor_id", monitor_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[bool | None]("include_content", include_content),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRecordsResponse],
            error_mapper=list_records_error_mapper,
            request_options=request_options,
        )

    def list_run_records(
        self,
        monitor_id: str,
        run_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRunRecordsResponse, ListRunRecordsErrorBody]:
        """Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound,
        not a dense sequence.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}/records"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[bool | None]("include_content", include_content),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunRecordsResponse],
            error_mapper=list_run_records_error_mapper,
            request_options=request_options,
        )


class AsyncRecordsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_records(
        self,
        monitor_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRecordsResponse, ListRecordsErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/records"),
            path_params=[param[str]("monitor_id", monitor_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[bool | None]("include_content", include_content),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRecordsResponse],
            error_mapper=list_records_error_mapper,
            request_options=request_options,
        )

    async def list_run_records(
        self,
        monitor_id: str,
        run_id: str,
        *,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        include_content: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRunRecordsResponse, ListRunRecordsErrorBody]:
        """Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound,
        not a dense sequence.

        Args:
            monitor_id: Value sent with the request.
            run_id: Value sent with the request.
            since: Exclusive lower bound on ``record_id``.
            before: Exclusive upper bound on ``record_id``.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            include_content: Include each record's document content. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}/runs/{run_id}/records"),
            path_params=[param[str]("monitor_id", monitor_id), param[str]("run_id", run_id)],
            query_params=[
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
                param[bool | None]("include_content", include_content),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListRunRecordsResponse],
            error_mapper=list_run_records_error_mapper,
            request_options=request_options,
        )
