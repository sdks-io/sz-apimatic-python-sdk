<!-- Generated file — do not edit; regenerated with the SDK. -->

# Search — operations

Accessor: `client.search` · Source: `seltz_api/apis/search.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search.search

- **Route**: `POST /v1/search`
- **Auth**: `api_key_auth`
- **Signature**: `def search(body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchResponse`
- **Returns (raw)**: `ApiResult[SearchResponse, SearchErrorBody]`
- **Error**: `SearchErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 402, 404, 405, 413, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SearchRequest` | `seltz_api/models/search_request.py` |
| `SearchRequestDict` | `seltz_api/models/search_request.py` |
| `SearchResponse` | `seltz_api/models/search_response.py` |
| `SearchErrorBody` | `seltz_api/errors/search_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

