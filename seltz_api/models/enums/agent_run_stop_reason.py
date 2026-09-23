from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentRunStopReason(str, Enum):
    """Why a run stopped. ``budget_reached`` pairs with ``completed`` when the output so far is usable and with
    ``failed`` when it is not."""

    FINISHED = "finished"
    BUDGET_REACHED = "budget_reached"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"
    INVALID_OUTPUT = "invalid_output"
    INTERNAL_ERROR = "internal_error"

    __str__ = str.__str__


AgentRunStopReasonOrStr: TypeAlias = Annotated[AgentRunStopReason | str, open_enum_validator(AgentRunStopReason)]
