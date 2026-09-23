from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

UpdateMonitorErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _UpdateMonitorError:
    def map(self, response: HttpResponse) -> UpdateMonitorErrorBody:
        match response.status_code:
            case 404 | 409:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


update_monitor_error_mapper: Final[ErrorMapper[UpdateMonitorErrorBody]] = _UpdateMonitorError()
