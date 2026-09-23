from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .http_citation import HttpCitation, HttpCitationDict


class AnswerHttpResponse(SdkBaseModel):
    """Buffered JSON response body for ``POST /v1/answer``."""

    answer: str
    """Markdown answer text. Inline citations follow the form ``text (`Source Name <url>`__)``."""

    citations: list[HttpCitation]
    """The sources the answer was grounded in. Every source the answer was given is returned, whether or not the text
    cites it."""


class AnswerHttpResponseDict(TypedDict):
    answer: str
    citations: list[HttpCitationDict]
