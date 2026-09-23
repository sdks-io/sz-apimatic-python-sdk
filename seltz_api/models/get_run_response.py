from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .run import Run, RunDict


class GetRunResponse(SdkBaseModel):
    run: OptionalNullable[Run] = UNSET


class GetRunResponseDict(TypedDict):
    run: NotRequired[RunDict | None]
