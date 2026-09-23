from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RequestStatus(str, Enum):
    """Whether one search request succeeded in a run."""

    OK = "ok"
    FAILED = "failed"

    __str__ = str.__str__


RequestStatusOrStr: TypeAlias = Annotated[RequestStatus | str, open_enum_validator(RequestStatus)]
