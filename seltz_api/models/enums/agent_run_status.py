from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentRunStatus(str, Enum):
    """Where a run is in its lifecycle: pending → running → completed / failed / cancelled."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    __str__ = str.__str__


AgentRunStatusOrStr: TypeAlias = Annotated[AgentRunStatus | str, open_enum_validator(AgentRunStatus)]
