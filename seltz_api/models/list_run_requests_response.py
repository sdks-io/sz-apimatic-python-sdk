from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .run_request import RunRequest, RunRequestDict


class ListRunRequestsResponse(SdkBaseModel):
    requests: Optional[list[RunRequest]] = UNSET
    """Ordered by request_id."""


class ListRunRequestsResponseDict(TypedDict):
    requests: NotRequired[list[RunRequestDict]]
