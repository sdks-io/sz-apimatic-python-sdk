from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .monitor import Monitor, MonitorDict


class CreateMonitorResponse(SdkBaseModel):
    monitor: OptionalNullable[Monitor] = UNSET
    webhook_secret: str = ""
    """Returned once, at create, and never again. Issued whether or not the create supplied a webhook, so keep it."""


class CreateMonitorResponseDict(TypedDict):
    monitor: NotRequired[MonitorDict | None]
    webhook_secret: NotRequired[str]
