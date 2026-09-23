from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AgentRunCitation(SdkBaseModel):
    """One citation supporting a grounded field."""

    source_id: int = 0
    """``id`` of the entry in ``sources`` this citation points at."""

    url: str = ""
    """URL of the cited document."""


class AgentRunCitationDict(TypedDict):
    source_id: NotRequired[int]
    url: NotRequired[str]
