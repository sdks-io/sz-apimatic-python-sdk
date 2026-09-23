from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ContentOptions(SdkBaseModel):
    """The ceiling on the content returned.

    The ceiling is an upper bound; the response carries at most what is specified here.

    The service may hold callers to a tighter bound than the range below. A larger request is then served at that bound
    rather than refused, which still carries at most what was specified. Only a value outside the range below is
    rejected."""

    max_characters_per_result: OptionalNullable[int] = UNSET
    r"""Ceiling on the characters of any single result's content.

    Counts Unicode code points -- Rust ``char``, Python ``len(s)``, JavaScript ``\[...s\].length``.

    Defaults to 20000, accepted range 100-1000000."""


class ContentOptionsDict(TypedDict):
    max_characters_per_result: NotRequired[int | None]
