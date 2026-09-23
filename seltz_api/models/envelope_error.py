from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnvelopeError(SdkBaseModel):
    """The error context. ``code`` is a stable descriptor in all-caps from a closed set per endpoint. ``message`` is a
    human-readable summary of what went wrong."""

    code: str
    """The error code."""

    message: str
    """The error message."""


class EnvelopeErrorDict(TypedDict):
    code: str
    message: str
