from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .document import Document, DocumentDict
from .search_request_ref import SearchRequestRef, SearchRequestRefDict


class SearchRecord(SdkBaseModel):
    document: OptionalNullable[Document] = UNSET
    matched_requests: Optional[list[SearchRequestRef]] = UNSET
    """Only the requests that matched in the run that emitted this record. A record is emitted once, on first sight, so
    a request that would match it in a later run never attaches to it."""


class SearchRecordDict(TypedDict):
    document: NotRequired[DocumentDict | None]
    matched_requests: NotRequired[list[SearchRequestRefDict]]
