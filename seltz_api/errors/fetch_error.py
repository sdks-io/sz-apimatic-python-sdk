from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

FetchErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _FetchError:
    def map(self, response: HttpResponse) -> FetchErrorBody:
        match response.status_code:
            case 400 | 401 | 402 | 429 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


fetch_error_mapper: Final[ErrorMapper[FetchErrorBody]] = _FetchError()
