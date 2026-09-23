from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .agent_run_citation import AgentRunCitation, AgentRunCitationDict


class AgentRunGrounding(SdkBaseModel):
    """Citations for one field of ``output.structured``."""

    citations: Optional[list[AgentRunCitation]] = UNSET
    """Citations supporting this field's value."""

    field: str = ""
    """Dot-notation path into the structured output, e.g. "companies.0.ceo"."""


class AgentRunGroundingDict(TypedDict):
    citations: NotRequired[list[AgentRunCitationDict]]
    field: NotRequired[str]
