from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document import Document, DocumentDict


class SearchResponse(SdkBaseModel):
    documents: Optional[list[Document]] = UNSET
    """Documents that are most relevant to the query"""


class SearchResponseDict(TypedDict):
    documents: NotRequired[list[DocumentDict]]
