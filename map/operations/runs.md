<!-- Generated file — do not edit; regenerated with the SDK. -->

# Runs — operations

Accessor: `client.runs` · Source: `seltz_api/apis/runs.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.runs.get_run

- **Route**: `GET /v1/monitors/{monitor_id}/runs/{run_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get_run(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `run_id`
- **Params**: `monitor_id` — path · `run_id` — path
- **Returns (parsed)**: `GetRunResponse`
- **Returns (raw)**: `ApiResult[GetRunResponse, GetRunErrorBody]`
- **Error**: `GetRunErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetRunResponse` | `seltz_api/models/get_run_response.py` |
| `GetRunErrorBody` | `seltz_api/errors/get_run_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.runs.list_run_requests

- **Route**: `GET /v1/monitors/{monitor_id}/runs/{run_id}/requests`
- **Auth**: `api_key_auth`
- **Signature**: `def list_run_requests(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `run_id`
- **Params**: `monitor_id` — path · `run_id` — path
- **Returns (parsed)**: `ListRunRequestsResponse`
- **Returns (raw)**: `ApiResult[ListRunRequestsResponse, ListRunRequestsErrorBody]`
- **Error**: `ListRunRequestsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListRunRequestsResponse` | `seltz_api/models/list_run_requests_response.py` |
| `ListRunRequestsErrorBody` | `seltz_api/errors/list_run_requests_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.runs.list_runs

- **Route**: `GET /v1/monitors/{monitor_id}/runs`
- **Auth**: `api_key_auth`
- **Signature**: `def list_runs(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, sort: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path · `since` — query · `before` — query · `limit` — query · `sort` — query
- **Returns (parsed)**: `ListRunsResponse`
- **Returns (raw)**: `ApiResult[ListRunsResponse, ListRunsErrorBody]`
- **Error**: `ListRunsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListRunsResponse` | `seltz_api/models/list_runs_response.py` |
| `ListRunsErrorBody` | `seltz_api/errors/list_runs_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

