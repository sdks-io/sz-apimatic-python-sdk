from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RunState2(str, Enum):
    """Live run state. Returned by this RPC only — the list endpoints do not include it."""

    IDLE = "idle"
    RUNNING = "running"
    UNKNOWN = "unknown"

    __str__ = str.__str__


RunState2OrStr: TypeAlias = Annotated[RunState2 | str, open_enum_validator(RunState2)]
