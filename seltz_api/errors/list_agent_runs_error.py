from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_envelope import ErrorEnvelope

ListAgentRunsErrorBody: TypeAlias = ErrorEnvelope | RawError


@dataclass(frozen=True, slots=True)
class _ListAgentRunsError:
    def map(self, response: HttpResponse) -> ListAgentRunsErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 500:
                return decode_json[ErrorEnvelope](response)
            case _:
                return RawError(response)


list_agent_runs_error_mapper: Final[ErrorMapper[ListAgentRunsErrorBody]] = _ListAgentRunsError()
