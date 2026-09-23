<!-- Generated file — do not edit; regenerated with the SDK. -->

# Answer — operations

Accessor: `client.answer` · Source: `seltz_api/apis/answer.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.answer.answer

- **Route**: `POST /v1/answer`
- **Auth**: `api_key_auth`
- **Signature**: `def answer(body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AnswerHttpResponse`
- **Returns (raw)**: `ApiResult[AnswerHttpResponse, AnswerErrorBody]`
- **Error**: `AnswerErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorEnvelope` [400, 401, 402, 404, 405, 408, 413, 415, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AnswerHttpRequest` | `seltz_api/models/answer_http_request.py` |
| `AnswerHttpRequestDict` | `seltz_api/models/answer_http_request.py` |
| `AnswerHttpResponse` | `seltz_api/models/answer_http_response.py` |
| `AnswerErrorBody` | `seltz_api/errors/answer_error.py` |
| `ErrorEnvelope` | `seltz_api/models/error_envelope.py` |

