from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .envelope_error1 import EnvelopeError1, EnvelopeError1Dict


class ErrorEnvelope(SdkBaseModel):
    """The response body returned for any error."""

    error: EnvelopeError1
    """The error context."""


class ErrorEnvelopeDict(TypedDict):
    error: EnvelopeError1Dict
