from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class HttpCitation(SdkBaseModel):
    """HTTP-shape citation. Mirrors the ``Citation`` proto."""

    content: OptionalNullable[str] = UNSET
    """Document content text (only when ``include_content = true``)."""

    url: str
    """URL of the source document."""


class HttpCitationDict(TypedDict):
    content: NotRequired[str | None]
    url: str
