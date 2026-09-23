from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnvelopeError1(SdkBaseModel):
    """The error context."""

    code: str
    """The error code."""

    message: str
    """The error message."""


class EnvelopeError1Dict(TypedDict):
    code: str
    message: str
