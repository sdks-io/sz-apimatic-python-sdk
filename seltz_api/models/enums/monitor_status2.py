from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MonitorStatus2(str, Enum):
    """Set to ``paused`` to create the monitor without starting it. Only ``active`` and ``paused`` are accepted.
    Defaults to ``active``."""

    ACTIVE = "active"
    PAUSED = "paused"
    DISABLED = "disabled"
    DELETED = "deleted"

    __str__ = str.__str__


MonitorStatus2OrStr: TypeAlias = Annotated[MonitorStatus2 | str, open_enum_validator(MonitorStatus2)]
