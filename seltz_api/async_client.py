from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.agent import AsyncAgent
from .apis.answer import AsyncAnswer
from .apis.fetch import AsyncFetch
from .apis.monitors import AsyncMonitors
from .apis.records import AsyncRecords
from .apis.runs import AsyncRuns
from .apis.search import AsyncSearch
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSeltzApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)


class AsyncSeltzApiClient(BaseSeltzApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "SeltzApiClient/1.9.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.9.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("x-api-key", api_key_auth) if api_key_auth is not None else no_auth
        )

    @cached_property
    def agent(self) -> AsyncAgent:
        return AsyncAgent(self._raw_client, self._server, self._auth)

    @cached_property
    def answer(self) -> AsyncAnswer:
        return AsyncAnswer(self._raw_client, self._server, self._auth)

    @cached_property
    def fetch(self) -> AsyncFetch:
        return AsyncFetch(self._raw_client, self._server, self._auth)

    @cached_property
    def monitors(self) -> AsyncMonitors:
        return AsyncMonitors(self._raw_client, self._server, self._auth)

    @cached_property
    def records(self) -> AsyncRecords:
        return AsyncRecords(self._raw_client, self._server, self._auth)

    @cached_property
    def runs(self) -> AsyncRuns:
        return AsyncRuns(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSeltzApiClient
