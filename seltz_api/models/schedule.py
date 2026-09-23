from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Schedule(SdkBaseModel):
    cadence: str


class ScheduleDict(TypedDict):
    cadence: str
