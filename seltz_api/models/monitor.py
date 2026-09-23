from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.monitor_status import MonitorStatus, MonitorStatusOrStr
from .monitor_search_request import MonitorSearchRequest, MonitorSearchRequestDict
from .webhook import Webhook, WebhookDict


class Monitor(SdkBaseModel):
    cadence: str
    created_at: OptionalNullable[str] = UNSET
    monitor_id: str = ""
    name: str = ""
    search_requests: Optional[list[MonitorSearchRequest]] = UNSET
    status: MonitorStatusOrStr = MonitorStatus.ACTIVE
    updated_at: OptionalNullable[str] = UNSET
    webhook: OptionalNullable[Webhook] = UNSET


class MonitorDict(TypedDict):
    cadence: str
    created_at: NotRequired[str | None]
    monitor_id: NotRequired[str]
    name: NotRequired[str]
    search_requests: NotRequired[list[MonitorSearchRequestDict]]
    status: MonitorStatusOrStr
    updated_at: NotRequired[str | None]
    webhook: NotRequired[WebhookDict | None]
