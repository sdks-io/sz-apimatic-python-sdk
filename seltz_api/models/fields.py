from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.content import Content, ContentDict
from .unions.snippets import Snippets, SnippetsDict


class Fields(SdkBaseModel):
    """The selectable members of a response ``Document``, and how much of each to return.

    ``Document.url`` and ``Document.published_date`` are always selected.

    Each member takes ``true``, ``false``, or an object of ceilings. An object selects the member and bounds it, so
    ``{"content": {"max_characters_per_result": 500}}`` returns content and no snippets. ``{"content": true}`` selects
    content under the default ceiling, which is what ``{"content": {}}`` returns as well. ``false`` switches the member
    off.

    A ``fields`` that names neither member returns the defaults below, so ``{}`` and a wholly absent ``fields`` mean the
    same thing. A ``fields`` that names either is read literally, so ``{"snippets": true}`` returns passages and no
    content."""

    content: Optional[Content] = UNSET
    """Emit ``Document.content``. Unset is true."""

    snippets: Optional[Snippets] = UNSET
    """Emit ``Document.snippets``. Unset is false."""


class FieldsDict(TypedDict):
    content: NotRequired[ContentDict]
    snippets: NotRequired[SnippetsDict]
