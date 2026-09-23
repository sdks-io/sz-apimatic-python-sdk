from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

GetAgentRunErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _GetAgentRunError:
    def map(self, response: HttpResponse) -> GetAgentRunErrorBody:
        match response.status_code:
            case 401 | 404 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


get_agent_run_error_mapper: Final[ErrorMapper[GetAgentRunErrorBody]] = _GetAgentRunError()
