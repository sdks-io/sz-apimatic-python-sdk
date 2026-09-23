from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.request_status import RequestStatus, RequestStatusOrStr


class RunRequest(SdkBaseModel):
    """One run's outcome for one search request."""

    completed_at: OptionalNullable[str] = UNSET
    new_records: int = 0
    reason: str = ""
    """Why the request failed, empty when it succeeded. Not machine-readable."""

    request_id: str = ""
    results_returned: int = 0
    status: RequestStatusOrStr = RequestStatus.OK


class RunRequestDict(TypedDict):
    completed_at: NotRequired[str | None]
    new_records: NotRequired[int]
    reason: NotRequired[str]
    request_id: NotRequired[str]
    results_returned: NotRequired[int]
    status: RequestStatusOrStr
