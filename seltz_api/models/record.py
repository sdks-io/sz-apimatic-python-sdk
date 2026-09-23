from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.record_type import RecordType, RecordTypeOrStr
from .search_record import SearchRecord, SearchRecordDict


class Record(SdkBaseModel):
    search_result: SearchRecord
    first_seen_at: OptionalNullable[str] = UNSET
    record_id: str = "0"
    run_id: str = "0"
    type_: RecordTypeOrStr = Field(default=RecordType.SEARCH_RESULT, alias="type")


class RecordDict(TypedDict):
    search_result: SearchRecordDict
    first_seen_at: NotRequired[str | None]
    record_id: NotRequired[str]
    run_id: NotRequired[str]
    type_: RecordTypeOrStr
