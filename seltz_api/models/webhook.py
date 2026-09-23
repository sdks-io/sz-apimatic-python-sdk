from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Webhook(SdkBaseModel):
    events: Optional[list[str]] = UNSET
    """Exactly two strings are legal: "run.completed" and "run.failed". An empty list is rejected.

    "run.completed" means the run finished. Read the run's ``record_count`` to see whether it produced records and its
    ``status`` to see whether every request succeeded. "run.failed" means no request succeeded. Neither fires for a
    skipped run."""

    status: Optional[str] = UNSET
    """Always reported on a monitor. Send ACTIVE to turn delivery back on once a failing endpoint is repaired, or
    DISABLED to stop it yourself.

    A disabled webhook stops the POST only. The monitor still runs and its records are still readable through the
    records cursor, so nothing is lost while it is off.

    On the way in it is the one field of this message that may be omitted: an absent status keeps whatever the monitor
    already has, so re-sending a webhook body does not by itself restart delivery to a dead endpoint."""

    url: str = ""


class WebhookDict(TypedDict):
    events: NotRequired[list[str]]
    status: NotRequired[str]
    url: NotRequired[str]
