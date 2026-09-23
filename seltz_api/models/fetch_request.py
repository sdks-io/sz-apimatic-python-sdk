from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FetchRequest(SdkBaseModel):
    api_key: OptionalNullable[str] = UNSET
    """API key to access the service. Either this or the ``x-api-key`` header must be supplied on the HTTP surface; the
    header takes precedence and is the documented path. On gRPC this field is the only carrier.

    Each URL that comes back with the OK status is billed. A URL that comes back with an error is not. The call is
    refused up front unless the balance covers the whole batch."""

    formats: Optional[list[str]] = UNSET
    r"""Representations to return, as documented format names.

    Omitted, or sent empty, means ``\["markdown"\]`` -- a repeated field carries no presence, so the two are the same
    request and neither means "no formats".

    Documented names:

    "markdown" -- the main content as Markdown, boilerplate removed.

    An unrecognized name is rejected."""

    tier: OptionalNullable[str] = UNSET
    """The service tier, which selects the price. Send ``"pro"``. Unset resolves to ``"pro"``.

    An unrecognized value is rejected rather than defaulted, because the value selects a price. The name is matched
    exactly."""

    timeout_ms: OptionalNullable[int] = UNSET
    """Wall-clock budget for one URL, in milliseconds.

    Applies to each URL, not to the batch. A URL that exceeds the budget gets ``error.code = "timeout"``; the others in
    the same request are unaffected.

    Unset means 75000, which is also the maximum; a larger value is served as 75000, and a value below 1000 is served as
    1000."""

    urls: Optional[list[str]] = UNSET
    """The URLs to fetch. At least one, at most 20.

    An empty list, more than 20 entries, a duplicate entry, a blank or padded entry, or an entry over 2048 bytes is
    rejected before any billing -- duplicates because ``FetchResult.requested_url`` is the correlation key and a
    repeated key is ambiguous.

    Everything else is reported inside a ``200`` as that URL's error result: a value that is not an absolute ``http`` or
    ``https`` URL, a host that does not resolve or that this service will not fetch, an origin that refuses, and a
    document that is not an HTML page."""


class FetchRequestDict(TypedDict):
    api_key: NotRequired[str | None]
    formats: NotRequired[list[str]]
    tier: NotRequired[str | None]
    timeout_ms: NotRequired[int | None]
    urls: NotRequired[list[str]]
