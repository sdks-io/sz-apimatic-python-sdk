from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RecordType(str, Enum):
    """What a record carries."""

    SEARCH_RESULT = "search_result"

    __str__ = str.__str__


RecordTypeOrStr: TypeAlias = Annotated[RecordType | str, open_enum_validator(RecordType)]
