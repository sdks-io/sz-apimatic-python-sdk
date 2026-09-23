from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.run_status import RunStatus, RunStatusOrStr


class Run(SdkBaseModel):
    completed_at: OptionalNullable[str] = UNSET
    first_record_id: str = "0"
    """The lowest ``record_id`` this run produced. Records are not contiguous; use ``record_count`` for the count."""

    last_record_id: str = "0"
    """The highest ``record_id`` this run produced. Records are not contiguous; use ``record_count`` for the count."""

    monitor_id: str = ""
    record_count: int = 0
    requests_failed: int = 0
    requests_ok: int = 0
    requests_total: int = 0
    run_id: str = "0"
    started_at: OptionalNullable[str] = UNSET
    status: RunStatusOrStr = RunStatus.COMPLETED
    status_reason: str = ""
    """Prose for a human, empty when completed."""


class RunDict(TypedDict):
    completed_at: NotRequired[str | None]
    first_record_id: NotRequired[str]
    last_record_id: NotRequired[str]
    monitor_id: NotRequired[str]
    record_count: NotRequired[int]
    requests_failed: NotRequired[int]
    requests_ok: NotRequired[int]
    requests_total: NotRequired[int]
    run_id: NotRequired[str]
    started_at: NotRequired[str | None]
    status: RunStatusOrStr
    status_reason: NotRequired[str]
