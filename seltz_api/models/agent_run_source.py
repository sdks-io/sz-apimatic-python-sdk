from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AgentRunSource(SdkBaseModel):
    """One source a run cited."""

    id: int = 0
    r"""Identifier within the run, cited as ``\[id\]`` in ``text`` and as ``source_id`` in ``grounding``."""

    url: str = ""
    """URL of the source document."""


class AgentRunSourceDict(TypedDict):
    id: NotRequired[int]
    url: NotRequired[str]
