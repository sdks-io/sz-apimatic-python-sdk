from __future__ import annotations

from typing import TypeAlias

from ..snippet_options import SnippetOptions, SnippetOptionsDict

Snippets: TypeAlias = bool | SnippetOptions
"""Emit ``Document.snippets``. Unset is false."""

SnippetsDict: TypeAlias = bool | SnippetOptionsDict
