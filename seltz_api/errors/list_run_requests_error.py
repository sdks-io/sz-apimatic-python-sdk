from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

ListRunRequestsErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _ListRunRequestsError:
    def map(self, response: HttpResponse) -> ListRunRequestsErrorBody:
        match response.status_code:
            case 404:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


list_run_requests_error_mapper: Final[ErrorMapper[ListRunRequestsErrorBody]] = _ListRunRequestsError()
