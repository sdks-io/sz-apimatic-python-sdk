from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fetch_result import FetchResult, FetchResultDict


class FetchResponse(SdkBaseModel):
    """One result per requested URL."""

    results: Optional[list[FetchResult]] = UNSET
    """One entry per entry in ``FetchRequest.urls``, successful or not, in the order the URLs were requested.

    Correlate on ``FetchResult.requested_url`` rather than on position."""


class FetchResponseDict(TypedDict):
    results: NotRequired[list[FetchResultDict]]
