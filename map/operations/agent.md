<!-- Generated file — do not edit; regenerated with the SDK. -->

# Agent — operations

Accessor: `client.agent` · Source: `seltz_api/apis/agent.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.agent.cancel_agent_run

- **Route**: `POST /v1/agent/runs/{id}/cancel`
- **Auth**: `api_key_auth`
- **Signature**: `def cancel_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AgentRun`
- **Returns (raw)**: `ApiResult[AgentRun, CancelAgentRunErrorBody]`
- **Error**: `CancelAgentRunErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [401, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentRun` | `seltz_api/models/agent_run.py` |
| `CancelAgentRunErrorBody` | `seltz_api/errors/cancel_agent_run_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.agent.create_agent_run

- **Route**: `POST /v1/agent/runs`
- **Auth**: `api_key_auth`
- **Signature**: `def create_agent_run(body: CreateAgentRunRequest | CreateAgentRunRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AgentRun`
- **Returns (raw)**: `ApiResult[AgentRun, CreateAgentRunErrorBody]`
- **Error**: `CreateAgentRunErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 402, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAgentRunRequest` | `seltz_api/models/create_agent_run_request.py` |
| `CreateAgentRunRequestDict` | `seltz_api/models/create_agent_run_request.py` |
| `AgentRun` | `seltz_api/models/agent_run.py` |
| `CreateAgentRunErrorBody` | `seltz_api/errors/create_agent_run_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.agent.get_agent_run

- **Route**: `GET /v1/agent/runs/{id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `AgentRun`
- **Returns (raw)**: `ApiResult[AgentRun, GetAgentRunErrorBody]`
- **Error**: `GetAgentRunErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [401, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentRun` | `seltz_api/models/agent_run.py` |
| `GetAgentRunErrorBody` | `seltz_api/errors/get_agent_run_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.agent.list_agent_runs

- **Route**: `GET /v1/agent/runs`
- **Auth**: `api_key_auth`
- **Signature**: `def list_agent_runs(*, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `after` — query
- **Returns (parsed)**: `ListAgentRunsResponse`
- **Returns (raw)**: `ApiResult[ListAgentRunsResponse, ListAgentRunsErrorBody]`
- **Error**: `ListAgentRunsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListAgentRunsResponse` | `seltz_api/models/list_agent_runs_response.py` |
| `ListAgentRunsErrorBody` | `seltz_api/errors/list_agent_runs_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

