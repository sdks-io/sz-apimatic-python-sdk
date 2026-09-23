from __future__ import annotations

from typing import TypeAlias

from ..content_options import ContentOptions, ContentOptionsDict

Content: TypeAlias = bool | ContentOptions
"""Emit ``Document.content``. Unset is true."""

ContentDict: TypeAlias = bool | ContentOptionsDict
