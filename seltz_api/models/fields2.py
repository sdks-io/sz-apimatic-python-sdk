from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.content import Content, ContentDict
from .unions.snippets import Snippets, SnippetsDict


class Fields2(SdkBaseModel):
    """Which selectable members of ``Document`` to populate.

    If absent, defaults to ``{content: true}``, which returns content under the default ceiling stated on
    ``ContentOptions``."""

    content: Optional[Content] = UNSET
    """Emit ``Document.content``. Unset is true."""

    snippets: Optional[Snippets] = UNSET
    """Emit ``Document.snippets``. Unset is false."""


class Fields2Dict(TypedDict):
    content: NotRequired[ContentDict]
    snippets: NotRequired[SnippetsDict]
