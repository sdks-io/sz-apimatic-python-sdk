from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

CreateAgentRunErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _CreateAgentRunError:
    def map(self, response: HttpResponse) -> CreateAgentRunErrorBody:
        match response.status_code:
            case 400 | 401 | 402 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


create_agent_run_error_mapper: Final[ErrorMapper[CreateAgentRunErrorBody]] = _CreateAgentRunError()
