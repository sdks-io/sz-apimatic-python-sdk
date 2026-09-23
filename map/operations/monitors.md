<!-- Generated file — do not edit; regenerated with the SDK. -->

# Monitors — operations

Accessor: `client.monitors` · Source: `seltz_api/apis/monitors.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.monitors.create_monitor

- **Route**: `POST /v1/monitors`
- **Auth**: `api_key_auth`
- **Signature**: `def create_monitor(body: CreateMonitorRequest | CreateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateMonitorResponse`
- **Returns (raw)**: `ApiResult[CreateMonitorResponse, CreateMonitorErrorBody]`
- **Error**: `CreateMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 409] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMonitorRequest` | `seltz_api/models/create_monitor_request.py` |
| `CreateMonitorRequestDict` | `seltz_api/models/create_monitor_request.py` |
| `CreateMonitorResponse` | `seltz_api/models/create_monitor_response.py` |
| `CreateMonitorErrorBody` | `seltz_api/errors/create_monitor_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.monitors.delete_monitor

- **Route**: `DELETE /v1/monitors/{monitor_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DeleteMonitorErrorBody]`
- **Error**: `DeleteMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteMonitorErrorBody` | `seltz_api/errors/delete_monitor_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.monitors.get_monitor

- **Route**: `GET /v1/monitors/{monitor_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path
- **Returns (parsed)**: `GetMonitorResponse`
- **Returns (raw)**: `ApiResult[GetMonitorResponse, GetMonitorErrorBody]`
- **Error**: `GetMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetMonitorResponse` | `seltz_api/models/get_monitor_response.py` |
| `GetMonitorErrorBody` | `seltz_api/errors/get_monitor_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.monitors.list_monitors

- **Route**: `GET /v1/monitors`
- **Auth**: `api_key_auth`
- **Signature**: `def list_monitors(*, name: str | None = None, status: str | None = None, since: str | None = None, before: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `name` — query · `status` — query · `since` — query · `before` — query · `limit` — query
- **Returns (parsed)**: `ListMonitorsResponse`
- **Returns (raw)**: `ApiResult[ListMonitorsResponse, ListMonitorsErrorBody]`
- **Error**: `ListMonitorsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListMonitorsResponse` | `seltz_api/models/list_monitors_response.py` |
| `ListMonitorsErrorBody` | `seltz_api/errors/list_monitors_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

### client.monitors.update_monitor

- **Route**: `PATCH /v1/monitors/{monitor_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def update_monitor(monitor_id: str, body: UpdateMonitorRequest | UpdateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `body`
- **Params**: `monitor_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateMonitorResponse`
- **Returns (raw)**: `ApiResult[UpdateMonitorResponse, UpdateMonitorErrorBody]`
- **Error**: `UpdateMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [404, 409] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateMonitorRequest` | `seltz_api/models/update_monitor_request.py` |
| `UpdateMonitorRequestDict` | `seltz_api/models/update_monitor_request.py` |
| `UpdateMonitorResponse` | `seltz_api/models/update_monitor_response.py` |
| `UpdateMonitorErrorBody` | `seltz_api/errors/update_monitor_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

