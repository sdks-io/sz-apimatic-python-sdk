from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

CancelAgentRunErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _CancelAgentRunError:
    def map(self, response: HttpResponse) -> CancelAgentRunErrorBody:
        match response.status_code:
            case 401 | 404 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


cancel_agent_run_error_mapper: Final[ErrorMapper[CancelAgentRunErrorBody]] = _CancelAgentRunError()
