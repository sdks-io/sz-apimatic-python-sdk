from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.monitor_status2 import MonitorStatus2OrStr
from .search_request import SearchRequest, SearchRequestDict
from .webhook import Webhook, WebhookDict


class CreateMonitorRequest(SdkBaseModel):
    cadence: str
    api_key: OptionalNullable[str] = UNSET
    name: str = ""
    """Unique per org among live monitors; a deleted monitor's name becomes available again. At most 512 bytes of
    UTF-8."""

    search_requests: Optional[list[SearchRequest]] = UNSET
    """At least one, at most 1000. Every request runs on every run. A request with an ``api_key`` set, a blank
    ``query``, or a body identical to another in the list is rejected."""

    status: Optional[MonitorStatus2OrStr] = UNSET
    webhook: OptionalNullable[Webhook] = UNSET


class CreateMonitorRequestDict(TypedDict):
    cadence: str
    api_key: NotRequired[str | None]
    name: NotRequired[str]
    search_requests: NotRequired[list[SearchRequestDict]]
    status: NotRequired[MonitorStatus2OrStr]
    webhook: NotRequired[WebhookDict | None]
