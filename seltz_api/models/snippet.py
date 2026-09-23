from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Snippet(SdkBaseModel):
    """One passage selected from a document's body."""

    text: OptionalNullable[str] = UNSET


class SnippetDict(TypedDict):
    text: NotRequired[str | None]
