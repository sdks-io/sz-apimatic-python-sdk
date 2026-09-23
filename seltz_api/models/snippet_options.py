from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SnippetOptions(SdkBaseModel):
    """Tuning for snippet selection.

    Each option is an upper bound; the response carries at most what is specified here.

    The service may hold callers to a tighter bound than the ranges below. A larger request is then served at that bound
    rather than refused, which still carries at most what was specified. Only a value outside the range below is
    rejected."""

    max_snippets: OptionalNullable[int] = UNSET
    """Maximum snippets returned across all documents. Accepted range 1-512.

    No default. Left unset, no response-wide ceiling applies at all, which is the recommended setting:
    ``max_snippets_per_result`` already bounds every document, so the response is bounded without one.

    This budget is spent one snippet per document at a time, so every document gets its best snippet before any document
    gets a second. This value is potentially raised to ensure each document can be given at least one snippet."""

    max_snippets_per_result: OptionalNullable[int] = UNSET
    """Maximum snippets from any single document. Defaults to 16, accepted range 1-256."""

    max_tokens: OptionalNullable[int] = UNSET
    """Ceiling on tokens across all snippets in the response. Defaults to 8192, accepted range 512-65536.

    Spent in the same order as ``max_snippets``, one snippet per document at a time, but unlike ``max_snippets`` this
    ceiling is not raised to fit ``max_results``. Set it low against many results and the budget runs out partway
    through a round: the documents it does not reach are still returned, with no snippets at all. If every result needs
    a snippet, raise this or lower ``max_results``."""

    max_tokens_per_result: OptionalNullable[int] = UNSET
    """Ceiling on tokens of snippets from any single document. Defaults to 4096, accepted range 128-32768."""


class SnippetOptionsDict(TypedDict):
    max_snippets: NotRequired[int | None]
    max_snippets_per_result: NotRequired[int | None]
    max_tokens: NotRequired[int | None]
    max_tokens_per_result: NotRequired[int | None]
