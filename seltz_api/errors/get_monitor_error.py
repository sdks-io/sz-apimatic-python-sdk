from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

GetMonitorErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _GetMonitorError:
    def map(self, response: HttpResponse) -> GetMonitorErrorBody:
        match response.status_code:
            case 404:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


get_monitor_error_mapper: Final[ErrorMapper[GetMonitorErrorBody]] = _GetMonitorError()
