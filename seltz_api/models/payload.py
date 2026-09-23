from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .search_record import SearchRecord, SearchRecordDict


class Payload(SdkBaseModel):
    search_result: SearchRecord


class PayloadDict(TypedDict):
    search_result: SearchRecordDict
