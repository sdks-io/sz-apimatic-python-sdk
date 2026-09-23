from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RunState(str, Enum):
    """Whether a monitor has a run open on it right now."""

    IDLE = "idle"
    RUNNING = "running"
    UNKNOWN = "unknown"

    __str__ = str.__str__


RunStateOrStr: TypeAlias = Annotated[RunState | str, open_enum_validator(RunState)]
