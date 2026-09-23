from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

ListRunRecordsErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _ListRunRecordsError:
    def map(self, response: HttpResponse) -> ListRunRecordsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


list_run_records_error_mapper: Final[ErrorMapper[ListRunRecordsErrorBody]] = _ListRunRecordsError()
