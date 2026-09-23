from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

GetRunErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _GetRunError:
    def map(self, response: HttpResponse) -> GetRunErrorBody:
        match response.status_code:
            case 404:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


get_run_error_mapper: Final[ErrorMapper[GetRunErrorBody]] = _GetRunError()
