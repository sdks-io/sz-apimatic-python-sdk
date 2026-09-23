from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

AnswerErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _AnswerError:
    def map(self, response: HttpResponse) -> AnswerErrorBody:
        match response.status_code:
            case 400 | 401 | 402 | 404 | 405 | 408 | 413 | 415 | 429 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


answer_error_mapper: Final[ErrorMapper[AnswerErrorBody]] = _AnswerError()
