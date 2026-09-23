from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.agent import Agent
from .apis.answer import Answer
from .apis.fetch import Fetch
from .apis.monitors import Monitors
from .apis.records import Records
from .apis.runs import Runs
from .apis.search import Search
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSeltzApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)


class SeltzApiClient(BaseSeltzApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "SeltzApiClient/1.9.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.9.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("x-api-key", api_key_auth) if api_key_auth is not None else no_auth
        )

    @cached_property
    def agent(self) -> Agent:
        return Agent(self._raw_client, self._server, self._auth)

    @cached_property
    def answer(self) -> Answer:
        return Answer(self._raw_client, self._server, self._auth)

    @cached_property
    def fetch(self) -> Fetch:
        return Fetch(self._raw_client, self._server, self._auth)

    @cached_property
    def monitors(self) -> Monitors:
        return Monitors(self._raw_client, self._server, self._auth)

    @cached_property
    def records(self) -> Records:
        return Records(self._raw_client, self._server, self._auth)

    @cached_property
    def runs(self) -> Runs:
        return Runs(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SeltzApiClient
