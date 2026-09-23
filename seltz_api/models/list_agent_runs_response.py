from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .agent_run import AgentRun, AgentRunDict


class ListAgentRunsResponse(SdkBaseModel):
    """List-runs response: one page of runs."""

    next: OptionalNullable[str] = UNSET
    """Cursor to the next page. Unset on the last page."""

    runs: Optional[list[AgentRun]] = UNSET
    """The page's runs, newest first."""


class ListAgentRunsResponseDict(TypedDict):
    next: NotRequired[str | None]
    runs: NotRequired[list[AgentRunDict]]
