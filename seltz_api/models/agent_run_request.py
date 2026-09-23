from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AgentRunRequest(SdkBaseModel):
    """The request a run was created with."""

    effort: OptionalNullable[str] = UNSET
    """The effort level the run executes at: the request's ``effort``, or the default level when it named none."""

    output_schema: OptionalNullable[Any] = UNSET
    """The request's ``output_schema``, when one was given. On gRPC the object is JSON-encoded."""

    query: str = ""
    """The natural-language question."""


class AgentRunRequestDict(TypedDict):
    effort: NotRequired[str | None]
    output_schema: NotRequired[Any | None]
    query: NotRequired[str]
