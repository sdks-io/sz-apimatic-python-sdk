from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class FetchError1(SdkBaseModel):
    """Why the fetch failed. Set when ``status`` is the error status, unset otherwise."""

    code: str = ""
    """A stable, machine-readable reason. A client must treat an unrecognized code as a generic failure rather than
    rejecting the result.

    Documented codes:

    "invalid_url" -- not a parseable absolute URL. "unsupported_scheme" -- parseable, but not ``http`` or ``https``.
    "url_not_accessible" -- DNS, connection, TLS, or navigation failure reaching the origin, or a host this service does
    not fetch. "timeout" -- the fetch did not finish within ``timeout_ms``. "unsupported_content_type" -- the document
    is not an HTML page. PDFs, images, archives, and other binaries are out of scope. Refused from the URL before the
    fetch, or from the media type the origin declared after it. "extraction_failed" -- the page was fetched, but no
    requested format could be produced from it. "upstream_error" -- the fetch path itself failed. Ours, not the
    URL's."""

    message: str = ""
    """A human-readable explanation. Always set when this message is present: ``FetchError`` itself is optional on the
    result, so an absent error is absent whole, and there is no state where a failure arrives without a reason. For
    operators and logs. Never parse it -- branch on ``code``. The wording of any given message may change at any
    time."""


class FetchError1Dict(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]
