from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RunStatus(str, Enum):
    """A run's outcome.

    ``completed`` -- every request succeeded. ``partial`` -- at least one request failed after retries and at least one
    succeeded. ``failed`` -- no request succeeded, and no records. ``skipped`` -- not attempted and not billed; see
    ``status_reason``. Any of them may produce no records."""

    COMPLETED = "completed"
    PARTIAL = "partial"
    FAILED = "failed"
    SKIPPED = "skipped"

    __str__ = str.__str__


RunStatusOrStr: TypeAlias = Annotated[RunStatus | str, open_enum_validator(RunStatus)]
