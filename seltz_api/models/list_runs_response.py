from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .run import Run, RunDict


class ListRunsResponse(SdkBaseModel):
    has_more: bool = False
    """True when limit cut the page short."""

    runs: Optional[list[Run]] = UNSET
    r"""Newest first by default, so \[0\] is the latest run. Page back with before = runs\[last\].run_id; pass sort =
    SORT_ORDER_ASC to walk forward instead, and page with since = runs\[last\].run_id."""


class ListRunsResponseDict(TypedDict):
    has_more: NotRequired[bool]
    runs: NotRequired[list[RunDict]]
