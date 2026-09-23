from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fields2 import Fields2, Fields2Dict


class SearchRequest(SdkBaseModel):
    api_key: OptionalNullable[str] = UNSET
    """API key. On the HTTP surface, either this or the ``x-api-key`` header must be supplied; the header takes
    precedence."""

    exclude_domains: Optional[list[str]] = UNSET
    """Exclude results from these domains"""

    fields: OptionalNullable[Fields2] = UNSET
    from_date: OptionalNullable[str] = UNSET
    """Only include results published on or after this point. UTC throughout.

    A date "2025-10-28", a datetime "2025-10-28T23:00:00" or "2025-10-28T23:00:00Z", or an offset from "now", which is
    the time the request is served: "now" itself, or "now-" and one duration such as "now-7d" for the past week. A
    datetime written without a zone is read as UTC, and a date written without a time is the start of that day.

    Offset units are s = second, m = minute, h = hour, d = 24 h, w = 7 d, M = one calendar month and y = one calendar
    year. A unit and a count are both required, and the case carries meaning.

    A month and a year step the calendar rather than a fixed number of seconds, and the day of the month is clamped to
    the length of the target month. So "now-1M" from the 31st of March lands on the 28th or 29th of February.

    An offset is a filter, not a freshness guarantee: the corpus refreshes on its own cadence, so a window of an hour or
    two can return nothing.

    Only a single offset before "now" is accepted. Rounding, several terms in one value, a "+" offset, and any anchor
    other than "now" are rejected."""

    include_domains: Optional[list[str]] = UNSET
    r"""Include only results from these domains (e.g., \["google.com", "example.com"\])"""

    max_results: OptionalNullable[int] = UNSET
    """Maximum number of results to return. Defaults to 10. A larger value is served as 1000."""

    query: str = ""
    """The search query."""

    scope: OptionalNullable[str] = UNSET
    """Restricts the results to one vertical or data set.

    Currently available: "news", "wikipedia", "people", "companies".

    When omitted, the default scope is searched. A scope that does not exist, or that this key cannot reach, returns
    404."""

    tier: OptionalNullable[str] = UNSET
    """How much work goes into ordering the results. It does not change which corpus is searched -- that is ``scope`` --
    so any scope can be requested in either tier.

    ``"base"`` returns first-stage ranking. ``"pro"`` adds a ranking stage for higher precision at the top of the list.

    Unset resolves to ``"pro"``, so ``"base"`` is opt-out. A scope with no Pro configuration serves ``"pro"`` exactly as
    ``"base"`` rather than failing, so a caller may always ask for ``"pro"``.

    The name is matched without regard to case, and surrounding whitespace is ignored, so "pro", "PRO" and " Pro " are
    one tier. A name that is neither is rejected rather than defaulted, because the value selects a price."""

    to_date: OptionalNullable[str] = UNSET
    """Only include results published on or before this point. UTC throughout.

    A date, a datetime, or an offset from "now", in the same spellings from_date takes. A date written without a time
    covers the whole of that day, ending at 23:59:59.999; an offset is an instant."""


class SearchRequestDict(TypedDict):
    api_key: NotRequired[str | None]
    exclude_domains: NotRequired[list[str]]
    fields: NotRequired[Fields2Dict | None]
    from_date: NotRequired[str | None]
    include_domains: NotRequired[list[str]]
    max_results: NotRequired[int | None]
    query: NotRequired[str]
    scope: NotRequired[str | None]
    tier: NotRequired[str | None]
    to_date: NotRequired[str | None]
