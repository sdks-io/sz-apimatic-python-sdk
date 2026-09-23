from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MonitorStatus(str, Enum):
    """A monitor's lifecycle state.

    ``active`` is scheduled and running. ``paused`` runs nothing and keeps its records and its record of what it has
    already delivered. Only those two can be set through the API; ``disabled`` and ``deleted`` are set by Seltz."""

    ACTIVE = "active"
    PAUSED = "paused"
    DISABLED = "disabled"
    DELETED = "deleted"

    __str__ = str.__str__


MonitorStatusOrStr: TypeAlias = Annotated[MonitorStatus | str, open_enum_validator(MonitorStatus)]
