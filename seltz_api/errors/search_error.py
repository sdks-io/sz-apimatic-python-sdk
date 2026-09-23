from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

SearchErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _SearchError:
    def map(self, response: HttpResponse) -> SearchErrorBody:
        match response.status_code:
            case 400 | 401 | 402 | 404 | 405 | 413 | 429 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


search_error_mapper: Final[ErrorMapper[SearchErrorBody]] = _SearchError()
