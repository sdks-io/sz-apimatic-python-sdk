from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CreateAgentRunRequest(SdkBaseModel):
    api_key: OptionalNullable[str] = UNSET
    """The API key, on gRPC requests. REST reads the ``x-api-key`` header instead."""

    effort: OptionalNullable[str] = UNSET
    """Effort level: how much research the run may do, and its price. One of the configured level names (e.g. ``low``,
    ``medium``, ``high``, ``max``). Omitted = the default level."""

    output_schema: OptionalNullable[Any] = UNSET
    """Optional OpenAI-style ``response_format`` object requesting structured output: ``{"type": "text" | "json_object"
    | "json_schema", ...}``, with ``name`` / ``schema`` / ``strict`` for type ``json_schema``. A structured type adds
    ``output.structured`` and its ``grounding`` alongside the cited text; type ``text`` is accepted and requests no
    structure. On gRPC the object is JSON-encoded."""

    query: str = ""
    """The natural-language question. Instructions inside the query are followed."""


class CreateAgentRunRequestDict(TypedDict):
    api_key: NotRequired[str | None]
    effort: NotRequired[str | None]
    output_schema: NotRequired[Any | None]
    query: NotRequired[str]
