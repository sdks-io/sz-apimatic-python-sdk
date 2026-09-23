from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

CreateMonitorErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _CreateMonitorError:
    def map(self, response: HttpResponse) -> CreateMonitorErrorBody:
        match response.status_code:
            case 400 | 401 | 409:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


create_monitor_error_mapper: Final[ErrorMapper[CreateMonitorErrorBody]] = _CreateMonitorError()
