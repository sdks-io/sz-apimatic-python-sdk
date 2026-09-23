from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentRunStopReason2(str, Enum):
    """Why the run stopped. Set once the run reaches a terminal state."""

    FINISHED = "finished"
    BUDGET_REACHED = "budget_reached"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"
    INVALID_OUTPUT = "invalid_output"
    INTERNAL_ERROR = "internal_error"

    __str__ = str.__str__


AgentRunStopReason2OrStr: TypeAlias = Annotated[AgentRunStopReason2 | str, open_enum_validator(AgentRunStopReason2)]
