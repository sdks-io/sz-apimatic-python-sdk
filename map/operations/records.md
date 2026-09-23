<!-- Generated file — do not edit; regenerated with the SDK. -->

# Records — operations

Accessor: `client.records` · Source: `seltz_api/apis/records.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.records.list_records

- **Route**: `GET /v1/monitors/{monitor_id}/records`
- **Auth**: `api_key_auth`
- **Signature**: `def list_records(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path · `since` — query · `before` — query · `limit` — query · `include_content` — query
- **Returns (parsed)**: `ListRecordsResponse`
- **Returns (raw)**: `ApiResult[ListRecordsResponse, ListRecordsErrorBody]`
- **Error**: `ListRecordsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListRecordsResponse` | `seltz_api/models/list_records_response.py` |
| `ListRecordsErrorBody` | `seltz_api/errors/list_records_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.records.list_run_records

- **Route**: `GET /v1/monitors/{monitor_id}/runs/{run_id}/records`
- **Auth**: `api_key_auth`
- **Signature**: `def list_run_records(monitor_id: str, run_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `run_id`
- **Params**: `monitor_id` — path · `run_id` — path · `since` — query · `before` — query · `limit` — query · `include_content` — query
- **Returns (parsed)**: `ListRunRecordsResponse`
- **Returns (raw)**: `ApiResult[ListRunRecordsResponse, ListRunRecordsErrorBody]`
- **Error**: `ListRunRecordsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListRunRecordsResponse` | `seltz_api/models/list_run_records_response.py` |
| `ListRunRecordsErrorBody` | `seltz_api/errors/list_run_records_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

