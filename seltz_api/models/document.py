from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .snippet import Snippet, SnippetDict


class Document(SdkBaseModel):
    """A single search result.

    ``url`` and ``published_date`` are returned without being asked for, and either may still be absent for a document
    that carries no such value. The remaining members are populated only when ``SearchRequest.fields`` asked for
    them."""

    content: OptionalNullable[str] = UNSET
    published_date: OptionalNullable[str] = UNSET
    """Publication date as ISO 8601 string (e.g. "2024-03-15T00:00:00Z")"""

    snippets: Optional[list[Snippet]] = UNSET
    """The document's highest-scoring snippets, in the order they appear in the document.

    Populated when ``fields.snippets`` is selected and passages are available; empty otherwise."""

    url: OptionalNullable[str] = UNSET


class DocumentDict(TypedDict):
    content: NotRequired[str | None]
    published_date: NotRequired[str | None]
    snippets: NotRequired[list[SnippetDict]]
    url: NotRequired[str | None]
