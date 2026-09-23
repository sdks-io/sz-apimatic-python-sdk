from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.fetch_status2 import FetchStatus2, FetchStatus2OrStr
from .fetch_error1 import FetchError1, FetchError1Dict


class FetchResult(SdkBaseModel):
    """The outcome for one URL."""

    content_type: OptionalNullable[str] = UNSET
    """The origin's declared media type for the main document, without parameters.

    Frequently unset, including on results that carry content. Never branch on it: ``status`` says whether a result
    carries content."""

    error: OptionalNullable[FetchError1] = UNSET
    fetched_at: OptionalNullable[str] = UNSET
    final_url: OptionalNullable[str] = UNSET
    """The URL the content actually came from, after HTTP redirects and any client-side navigation. Equal to
    ``requested_url`` when nothing redirected.

    Set on a result whose ``status`` is ERROR only when the failure happened after the origin answered, such as a page
    this service could not extract. Unset when the URL was never reached."""

    http_status_code: OptionalNullable[int] = UNSET
    """The origin's HTTP status code for the main document. Unset when no network response was observed for the
    navigation.

    An HTTP error status is not a fetch failure: this service renders the origin's error page, so a 404 arrives as an OK
    result carrying 404. On a result whose ``status`` is ERROR, this follows ``final_url`` - set only when the failure
    happened after the origin answered."""

    markdown: OptionalNullable[str] = UNSET
    """The page's main content as Markdown, with boilerplate removed."""

    requested_url: str = ""
    """The URL this answers, echoed verbatim from the request -- byte for byte, never normalized, and never the
    post-redirect URL. This is the correlation key. Where redirects landed is ``final_url``."""

    status: FetchStatus2OrStr = FetchStatus2.OK


class FetchResultDict(TypedDict):
    content_type: NotRequired[str | None]
    error: NotRequired[FetchError1Dict | None]
    fetched_at: NotRequired[str | None]
    final_url: NotRequired[str | None]
    http_status_code: NotRequired[int | None]
    markdown: NotRequired[str | None]
    requested_url: NotRequired[str]
    status: FetchStatus2OrStr
