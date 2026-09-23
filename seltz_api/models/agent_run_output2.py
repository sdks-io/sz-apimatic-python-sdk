from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .agent_run_grounding import AgentRunGrounding, AgentRunGroundingDict
from .agent_run_source import AgentRunSource, AgentRunSourceDict


class AgentRunOutput2(SdkBaseModel):
    """The run's output. Its members are unset until the run completes."""

    grounding: Optional[list[AgentRunGrounding]] = UNSET
    """Per-field citations for ``structured``. Empty when there is no structured output."""

    sources: Optional[list[AgentRunSource]] = UNSET
    """The sources cited by ``text`` or ``grounding``, numbered in order of first citation."""

    structured: OptionalNullable[Any] = UNSET
    """Structured result shaped by the request's ``output_schema``. Unset when the request had none. Fields that could
    not be grounded are expected to be null. On gRPC the object is JSON-encoded."""

    text: OptionalNullable[str] = UNSET
    r"""Cited markdown report. Inline ``\[n\]`` markers cite the entry of ``sources`` whose ``id`` is ``n``."""


class AgentRunOutput2Dict(TypedDict):
    grounding: NotRequired[list[AgentRunGroundingDict]]
    sources: NotRequired[list[AgentRunSourceDict]]
    structured: NotRequired[Any | None]
    text: NotRequired[str | None]
