from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SearchRequestRef(SdkBaseModel):
    query: str = ""
    """The request's query text, carried here so a record can be rendered without a second lookup."""

    request_id: str = ""


class SearchRequestRefDict(TypedDict):
    query: NotRequired[str]
    request_id: NotRequired[str]
