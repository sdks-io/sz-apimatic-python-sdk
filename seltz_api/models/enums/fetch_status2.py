from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FetchStatus2(str, Enum):
    """Whether this result carries content.

    Branch on this field, never on whether a given content field is present: a format the page could not produce is
    unset on an otherwise successful result, so "markdown is absent" does not mean "the fetch failed".

    A failed fetch is still HTTP 200, with the error status on the result."""

    OK = "ok"
    ERROR = "error"

    __str__ = str.__str__


FetchStatus2OrStr: TypeAlias = Annotated[FetchStatus2 | str, open_enum_validator(FetchStatus2)]
