<!-- Generated file — do not edit; regenerated with the SDK. -->

# Fetch — operations

Accessor: `client.fetch` · Source: `seltz_api/apis/fetch.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.fetch.fetch

- **Route**: `POST /v1/fetch`
- **Auth**: `api_key_auth`
- **Signature**: `def fetch(body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FetchResponse`
- **Returns (raw)**: `ApiResult[FetchResponse, FetchErrorBody]`
- **Error**: `FetchErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 402, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FetchRequest` | `seltz_api/models/fetch_request.py` |
| `FetchRequestDict` | `seltz_api/models/fetch_request.py` |
| `FetchResponse` | `seltz_api/models/fetch_response.py` |
| `FetchErrorBody` | `seltz_api/errors/fetch_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

