from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentRunStatus2(str, Enum):
    """Where the run is in its lifecycle."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    __str__ = str.__str__


AgentRunStatus2OrStr: TypeAlias = Annotated[AgentRunStatus2 | str, open_enum_validator(AgentRunStatus2)]
