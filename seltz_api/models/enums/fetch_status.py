from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FetchStatus(str, Enum):
    """Whether a ``FetchResult`` carries content."""

    OK = "ok"
    ERROR = "error"

    __str__ = str.__str__


FetchStatusOrStr: TypeAlias = Annotated[FetchStatus | str, open_enum_validator(FetchStatus)]
