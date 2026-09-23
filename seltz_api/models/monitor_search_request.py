from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .search_request import SearchRequest, SearchRequestDict


class MonitorSearchRequest(SdkBaseModel):
    """A search request stored on a monitor, with its server-assigned id."""

    consecutive_failures: int = 0
    """Consecutive failed runs for this request."""

    last_success_at: OptionalNullable[str] = UNSET
    request: OptionalNullable[SearchRequest] = UNSET
    request_id: str = ""


class MonitorSearchRequestDict(TypedDict):
    consecutive_failures: NotRequired[int]
    last_success_at: NotRequired[str | None]
    request: NotRequired[SearchRequestDict | None]
    request_id: NotRequired[str]
