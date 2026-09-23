from __future__ import annotations

from typing import Any
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
from ..errors.create_monitor_error import CreateMonitorErrorBody, create_monitor_error_mapper
from ..errors.delete_monitor_error import DeleteMonitorErrorBody, delete_monitor_error_mapper
from ..errors.get_monitor_error import GetMonitorErrorBody, get_monitor_error_mapper
from ..errors.list_monitors_error import ListMonitorsErrorBody, list_monitors_error_mapper
from ..errors.update_monitor_error import UpdateMonitorErrorBody, update_monitor_error_mapper
from ..models.create_monitor_request import CreateMonitorRequest, CreateMonitorRequestDict
from ..models.create_monitor_response import CreateMonitorResponse
from ..models.get_monitor_response import GetMonitorResponse
from ..models.list_monitors_response import ListMonitorsResponse
from ..models.update_monitor_request import UpdateMonitorRequest, UpdateMonitorRequestDict
from ..models.update_monitor_response import UpdateMonitorResponse
from ..server.server import Server


class Monitors:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MonitorsWithRawResponse(client, server, auth)

    def create_monitor(
        self,
        body: CreateMonitorRequest | CreateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMonitorResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created. ``webhook_secret`` is returned once and never again.

        Raises:
            ApiError: Missing or malformed fields. Invalid or missing API key. That name is already taken in this org.
                ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.create_monitor(body, request_options=request_options).unwrap()

    def delete_monitor(self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deleted. Every record becomes invisible at once.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.delete_monitor(monitor_id, request_options=request_options).unwrap()

    def get_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetMonitorResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The monitor.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.get_monitor(monitor_id, request_options=request_options).unwrap()

    def list_monitors(
        self,
        *,
        name: str | None = None,
        status: str | None = None,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMonitorsResponse:
        """Send a ``GET`` request.

        Args:
            name: Matches a monitor whose name is exactly this.
            status: One of ``active``, ``paused``, ``disabled``. ``deleted`` is not a filter: a deleted monitor is
                invisible.
            since: Exclusive lower bound: the ``monitor_id`` of a monitor to start after.
            before: Exclusive upper bound. The list is newest first, so page forward with the ``monitor_id`` of the last
                monitor on the previous page.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The org's monitors.

        Raises:
            ApiError: Invalid or missing API key. ``error`` is ``ErrorEnvelope | RawError``."""
        return self._with_raw_response.list_monitors(
            name=name, status=status, since=since, before=before, limit=limit, request_options=request_options
        ).unwrap()

    def update_monitor(
        self,
        monitor_id: str,
        body: UpdateMonitorRequest | UpdateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMonitorResponse:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated.

        Raises:
            ApiError: No such monitor in this org. That name is already taken in this org. ``error`` is ``ErrorEnvelope
                | RawError``."""
        return self._with_raw_response.update_monitor(monitor_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MonitorsWithRawResponse:
        return self._with_raw_response


class AsyncMonitors:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMonitorsWithRawResponse(client, server, auth)

    async def create_monitor(
        self,
        body: CreateMonitorRequest | CreateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMonitorResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created. ``webhook_secret`` is returned once and never again.

        Raises:
            ApiError: Missing or malformed fields. Invalid or missing API key. That name is already taken in this org.
                ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.create_monitor(body, request_options=request_options)).unwrap()

    async def delete_monitor(self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deleted. Every record becomes invisible at once.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.delete_monitor(monitor_id, request_options=request_options)).unwrap()

    async def get_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetMonitorResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The monitor.

        Raises:
            ApiError: No such monitor in this org. ``error`` is ``ErrorEnvelope | RawError``."""
        return (await self._with_raw_response.get_monitor(monitor_id, request_options=request_options)).unwrap()

    async def list_monitors(
        self,
        *,
        name: str | None = None,
        status: str | None = None,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMonitorsResponse:
        """Send a ``GET`` request.

        Args:
            name: Matches a monitor whose name is exactly this.
            status: One of ``active``, ``paused``, ``disabled``. ``deleted`` is not a filter: a deleted monitor is
                invisible.
            since: Exclusive lower bound: the ``monitor_id`` of a monitor to start after.
            before: Exclusive upper bound. The list is newest first, so page forward with the ``monitor_id`` of the last
                monitor on the previous page.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The org's monitors.

        Raises:
            ApiError: Invalid or missing API key. ``error`` is ``ErrorEnvelope | RawError``."""
        return (
            await self._with_raw_response.list_monitors(
                name=name, status=status, since=since, before=before, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def update_monitor(
        self,
        monitor_id: str,
        body: UpdateMonitorRequest | UpdateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMonitorResponse:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated.

        Raises:
            ApiError: No such monitor in this org. That name is already taken in this org. ``error`` is ``ErrorEnvelope
                | RawError``."""
        return (
            await self._with_raw_response.update_monitor(monitor_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMonitorsWithRawResponse:
        return self._with_raw_response


class MonitorsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_monitor(
        self,
        body: CreateMonitorRequest | CreateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMonitorResponse, CreateMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/monitors"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMonitorRequest | CreateMonitorRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateMonitorResponse],
            error_mapper=create_monitor_error_mapper,
            request_options=request_options,
        )

    def delete_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteMonitorErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=delete_monitor_error_mapper,
            request_options=request_options,
        )

    def get_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetMonitorResponse, GetMonitorErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetMonitorResponse],
            error_mapper=get_monitor_error_mapper,
            request_options=request_options,
        )

    def list_monitors(
        self,
        *,
        name: str | None = None,
        status: str | None = None,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMonitorsResponse, ListMonitorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            name: Matches a monitor whose name is exactly this.
            status: One of ``active``, ``paused``, ``disabled``. ``deleted`` is not a filter: a deleted monitor is
                invisible.
            since: Exclusive lower bound: the ``monitor_id`` of a monitor to start after.
            before: Exclusive upper bound. The list is newest first, so page forward with the ``monitor_id`` of the last
                monitor on the previous page.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors"),
            query_params=[
                param[str | None]("name", name),
                param[str | None]("status", status),
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListMonitorsResponse],
            error_mapper=list_monitors_error_mapper,
            request_options=request_options,
        )

    def update_monitor(
        self,
        monitor_id: str,
        body: UpdateMonitorRequest | UpdateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMonitorResponse, UpdateMonitorErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMonitorRequest | UpdateMonitorRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UpdateMonitorResponse],
            error_mapper=update_monitor_error_mapper,
            request_options=request_options,
        )


class AsyncMonitorsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_monitor(
        self,
        body: CreateMonitorRequest | CreateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMonitorResponse, CreateMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/monitors"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMonitorRequest | CreateMonitorRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateMonitorResponse],
            error_mapper=create_monitor_error_mapper,
            request_options=request_options,
        )

    async def delete_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteMonitorErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=delete_monitor_error_mapper,
            request_options=request_options,
        )

    async def get_monitor(
        self, monitor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetMonitorResponse, GetMonitorErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetMonitorResponse],
            error_mapper=get_monitor_error_mapper,
            request_options=request_options,
        )

    async def list_monitors(
        self,
        *,
        name: str | None = None,
        status: str | None = None,
        since: str | None = None,
        before: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMonitorsResponse, ListMonitorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            name: Matches a monitor whose name is exactly this.
            status: One of ``active``, ``paused``, ``disabled``. ``deleted`` is not a filter: a deleted monitor is
                invisible.
            since: Exclusive lower bound: the ``monitor_id`` of a monitor to start after.
            before: Exclusive upper bound. The list is newest first, so page forward with the ``monitor_id`` of the last
                monitor on the previous page.
            limit: Defaults to 100, at most 1,000. A short page is normal: a page ends at ``limit`` or at the byte
                budget, whichever binds first.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/monitors"),
            query_params=[
                param[str | None]("name", name),
                param[str | None]("status", status),
                param[str | None]("since", since),
                param[str | None]("before", before),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListMonitorsResponse],
            error_mapper=list_monitors_error_mapper,
            request_options=request_options,
        )

    async def update_monitor(
        self,
        monitor_id: str,
        body: UpdateMonitorRequest | UpdateMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMonitorResponse, UpdateMonitorErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/monitors/{monitor_id}"),
            path_params=[param[str]("monitor_id", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMonitorRequest | UpdateMonitorRequestDict](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UpdateMonitorResponse],
            error_mapper=update_monitor_error_mapper,
            request_options=request_options,
        )
