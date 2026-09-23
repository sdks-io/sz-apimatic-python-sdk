from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.run_state2 import RunState2, RunState2OrStr
from .monitor import Monitor, MonitorDict


class GetMonitorResponse(SdkBaseModel):
    monitor: OptionalNullable[Monitor] = UNSET
    run_state: RunState2OrStr = RunState2.IDLE


class GetMonitorResponseDict(TypedDict):
    monitor: NotRequired[MonitorDict | None]
    run_state: RunState2OrStr
