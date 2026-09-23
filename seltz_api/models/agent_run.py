from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .agent_run_output2 import AgentRunOutput2, AgentRunOutput2Dict
from .agent_run_request2 import AgentRunRequest2, AgentRunRequest2Dict
from .enums.agent_run_status2 import AgentRunStatus2, AgentRunStatus2OrStr
from .enums.agent_run_stop_reason2 import AgentRunStopReason2OrStr


class AgentRun(SdkBaseModel):
    """An agent run."""

    completed_at: OptionalNullable[str] = UNSET
    """When the run reached a terminal state. Unset until then."""

    created_at: str = ""
    """When the run was created, as an ISO 8601 timestamp."""

    id: str = ""
    """Unique run id."""

    object_: str = Field(default="", alias="object")
    """Object type, always "agent.run"."""

    output: OptionalNullable[AgentRunOutput2] = UNSET
    request: OptionalNullable[AgentRunRequest2] = UNSET
    started_at: OptionalNullable[str] = UNSET
    """When the run started. Unset while pending."""

    status: AgentRunStatus2OrStr = AgentRunStatus2.PENDING
    stop_reason: OptionalNullable[AgentRunStopReason2OrStr] = UNSET


class AgentRunDict(TypedDict):
    completed_at: NotRequired[str | None]
    created_at: NotRequired[str]
    id: NotRequired[str]
    object_: NotRequired[str]
    output: NotRequired[AgentRunOutput2Dict | None]
    request: NotRequired[AgentRunRequest2Dict | None]
    started_at: NotRequired[str | None]
    status: NotRequired[AgentRunStatus2OrStr]
    stop_reason: NotRequired[AgentRunStopReason2OrStr | None]
