from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class AnswerHttpRequest(SdkBaseModel):
    """JSON request body for ``POST /v1/answer``."""

    api_key: OptionalNullable[str] = UNSET
    """API key. Either this or the ``x-api-key`` header must be supplied; the header takes precedence."""

    include_content: Optional[bool] = UNSET
    """When true, citations carry the document content text. Default false."""

    model: OptionalNullable[str] = UNSET
    """Selects the answer tier, which determines behavior and billing. Omitted resolves to the default tier. Independent
    of ``scope``; the response shape is unchanged."""

    query: str
    """The natural-language question."""

    response_format: Optional[Any] = UNSET
    """Optional ``OpenAI`` ``response_format`` object (`{"type": "text" | "json_object" | "json_schema", ...}`),
    accepted as raw JSON exactly like ``/v1/chat/completions``. Under a structured type no inline citations are added,
    so the answer stays schema-valid; a malformed value is a ``400`` before billing. Omitted leaves the answer as
    Markdown prose. Applies at every tier."""

    scope: OptionalNullable[str] = UNSET
    """Restricts the grounding search to one scope.

    Currently available:

    - ``news``
    - ``wikipedia``
    - ``people``
    - ``companies``

    Omitted, empty or whitespace-only searches the default scope."""

    stream: Optional[bool] = UNSET
    """When true, stream the answer as OpenAI-mimic SSE chunks. Default false."""

    system_prompt: OptionalNullable[str] = UNSET
    """Steers how the answer is presented — tone, voice, format. It is subordinate to the grounding and citation rules,
    which stay in force. That precedence is instructional, not a sandbox. Omitted, empty or whitespace-only leaves the
    presentation unchanged. Applies at every tier and composes with ``response_format``. At most 8 KiB of UTF-8; a
    longer value is a ``400`` before billing."""


class AnswerHttpRequestDict(TypedDict):
    api_key: NotRequired[str | None]
    include_content: NotRequired[bool]
    model: NotRequired[str | None]
    query: str
    response_format: NotRequired[Any]
    scope: NotRequired[str | None]
    stream: NotRequired[bool]
    system_prompt: NotRequired[str | None]
