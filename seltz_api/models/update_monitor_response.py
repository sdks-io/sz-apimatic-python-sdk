from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .monitor import Monitor, MonitorDict


class UpdateMonitorResponse(SdkBaseModel):
    monitor: OptionalNullable[Monitor] = UNSET


class UpdateMonitorResponseDict(TypedDict):
    monitor: NotRequired[MonitorDict | None]
