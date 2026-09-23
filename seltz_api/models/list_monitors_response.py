from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monitor import Monitor, MonitorDict


class ListMonitorsResponse(SdkBaseModel):
    has_more: bool = False
    r"""True when limit or the byte budget cut the page short. Page forward with before =
    monitors\[last\].monitor_id."""

    monitors: Optional[list[Monitor]] = UNSET
    """Newest first. A short page is normal: a page ends at limit or at a byte budget, whichever binds first. A monitor
    carries its whole request list, so a count alone cannot bound the response."""


class ListMonitorsResponseDict(TypedDict):
    has_more: NotRequired[bool]
    monitors: NotRequired[list[MonitorDict]]
