from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.monitor_status import MonitorStatusOrStr
from .search_request import SearchRequest, SearchRequestDict
from .webhook1 import Webhook1, Webhook1Dict


class UpdateMonitorRequest(SdkBaseModel):
    cadence: str
    api_key: OptionalNullable[str] = UNSET
    monitor_id: str = ""
    name: OptionalNullable[str] = UNSET
    search_requests: Optional[list[SearchRequest]] = UNSET
    """Replaces the list wholesale when set. An empty list is read as "not set" and keeps the current requests. A
    request keeps its id and its health when every field of its body is unchanged."""

    status: Optional[MonitorStatusOrStr] = UNSET
    webhook: OptionalNullable[Webhook1] = UNSET


class UpdateMonitorRequestDict(TypedDict):
    cadence: str
    api_key: NotRequired[str | None]
    monitor_id: NotRequired[str]
    name: NotRequired[str | None]
    search_requests: NotRequired[list[SearchRequestDict]]
    status: NotRequired[MonitorStatusOrStr]
    webhook: NotRequired[Webhook1Dict | None]
