from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .record import Record, RecordDict


class ListRecordsResponse(SdkBaseModel):
    has_more: bool = False
    r"""True when limit or the byte budget cut the page short. Page forward with since = records\[last\].record_id."""

    records: Optional[list[Record]] = UNSET
    """Oldest first. A short page is normal: a page ends at limit or at a byte budget, whichever binds first."""


class ListRecordsResponseDict(TypedDict):
    has_more: NotRequired[bool]
    records: NotRequired[list[RecordDict]]
