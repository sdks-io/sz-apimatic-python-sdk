from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

ListMonitorsErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _ListMonitorsError:
    def map(self, response: HttpResponse) -> ListMonitorsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


list_monitors_error_mapper: Final[ErrorMapper[ListMonitorsErrorBody]] = _ListMonitorsError()
