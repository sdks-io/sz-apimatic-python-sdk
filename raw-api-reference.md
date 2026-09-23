# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [SeltzApiClient](seltz_api/client.py)

## Agent

> Source: [Agent](seltz_api/apis/agent.py)

<details>
<summary><code>def cancel_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentRun, CancelAgentRunErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe to retry.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.agent.with_raw_response.cancel_agent_run(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelAgentRunErrorBody
```

**Async**

```python
result = await async_client.agent.with_raw_response.cancel_agent_run(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelAgentRunErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The run id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[AgentRun](seltz_api/models/agent_run.py), [CancelAgentRunErrorBody](seltz_api/errors/cancel_agent_run_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The run.

**On `Failure`**: `error` is <code>[CancelAgentRunErrorBody](seltz_api/errors/cancel_agent_run_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_agent_run(body: CreateAgentRunRequest | CreateAgentRunRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentRun, CreateAgentRunErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the new run in `pending` state. Poll it by id until `status` reaches a terminal state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.agent.with_raw_response.create_agent_run(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAgentRunErrorBody
```

**Async**

```python
result = await async_client.agent.with_raw_response.create_agent_run(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAgentRunErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateAgentRunRequest](seltz_api/models/create_agent_run_request.py) \| [CreateAgentRunRequestDict](seltz_api/models/create_agent_run_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[AgentRun](seltz_api/models/agent_run.py), [CreateAgentRunErrorBody](seltz_api/errors/create_agent_run_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The new run, in `pending` state.

**On `Failure`**: `error` is <code>[CreateAgentRunErrorBody](seltz_api/errors/create_agent_run_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentRun, GetAgentRunErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Poll until `status` reaches a terminal state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.agent.with_raw_response.get_agent_run(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAgentRunErrorBody
```

**Async**

```python
result = await async_client.agent.with_raw_response.get_agent_run(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAgentRunErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The run id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[AgentRun](seltz_api/models/agent_run.py), [GetAgentRunErrorBody](seltz_api/errors/get_agent_run_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The run.

**On `Failure`**: `error` is <code>[GetAgentRunErrorBody](seltz_api/errors/get_agent_run_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 404, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_agent_runs(*, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListAgentRunsResponse, ListAgentRunsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The organization's runs, newest first. Pass one page's `next` as the following request's `after`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.agent.with_raw_response.list_agent_runs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentRunsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAgentRunsErrorBody
```

**Async**

```python
result = await async_client.agent.with_raw_response.list_agent_runs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentRunsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAgentRunsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Page size, 1-100. Defaults to 20.<br>**Default**: <code>None</code> |
| <code>after</code> | <code>str \| None</code> | Pagination cursor: the previous page's `next`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListAgentRunsResponse](seltz_api/models/list_agent_runs_response.py), [ListAgentRunsErrorBody](seltz_api/errors/list_agent_runs_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListAgentRunsResponse](seltz_api/models/list_agent_runs_response.py)</code> -- One page of runs, newest first.

**On `Failure`**: `error` is <code>[ListAgentRunsErrorBody](seltz_api/errors/list_agent_runs_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Answer

> Source: [Answer](seltz_api/apis/answer.py)

<details>
<summary><code>def answer(body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnswerHttpResponse, AnswerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.answer.with_raw_response.answer(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnswerHttpResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AnswerErrorBody
```

**Async**

```python
result = await async_client.answer.with_raw_response.answer(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnswerHttpResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AnswerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AnswerHttpRequest](seltz_api/models/answer_http_request.py) \| [AnswerHttpRequestDict](seltz_api/models/answer_http_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[AnswerHttpResponse](seltz_api/models/answer_http_response.py), [AnswerErrorBody](seltz_api/errors/answer_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnswerHttpResponse](seltz_api/models/answer_http_response.py)</code> -- Answer for the query. When `stream = false` the body is a JSON `AnswerHttpResponse`; when `stream = true` it is a `text/event-stream` of OpenAI-style chunks.

**On `Failure`**: `error` is <code>[AnswerErrorBody](seltz_api/errors/answer_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 404, 405, 408, 413, 415, 429, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Fetch

> Source: [Fetch](seltz_api/apis/fetch.py)

<details>
<summary><code>def fetch(body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FetchResponse, FetchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.fetch.with_raw_response.fetch(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FetchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FetchErrorBody
```

**Async**

```python
result = await async_client.fetch.with_raw_response.fetch(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FetchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type FetchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FetchRequest](seltz_api/models/fetch_request.py) \| [FetchRequestDict](seltz_api/models/fetch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[FetchResponse](seltz_api/models/fetch_response.py), [FetchErrorBody](seltz_api/errors/fetch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FetchResponse](seltz_api/models/fetch_response.py)</code> -- One result per requested URL. A failure to fetch a page is still a 200, with that result's `status = "error"`.

**On `Failure`**: `error` is <code>[FetchErrorBody](seltz_api/errors/fetch_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 429, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Monitors

> Source: [Monitors](seltz_api/apis/monitors.py)

<details>
<summary><code>def create_monitor(body: CreateMonitorRequest | CreateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateMonitorResponse, CreateMonitorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.monitors.with_raw_response.create_monitor(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateMonitorErrorBody
```

**Async**

```python
result = await async_client.monitors.with_raw_response.create_monitor(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateMonitorRequest](seltz_api/models/create_monitor_request.py) \| [CreateMonitorRequestDict](seltz_api/models/create_monitor_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[CreateMonitorResponse](seltz_api/models/create_monitor_response.py), [CreateMonitorErrorBody](seltz_api/errors/create_monitor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateMonitorResponse](seltz_api/models/create_monitor_response.py)</code> -- Created. `webhook_secret` is returned once and never again.

**On `Failure`**: `error` is <code>[CreateMonitorErrorBody](seltz_api/errors/create_monitor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 409 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, DeleteMonitorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.monitors.with_raw_response.delete_monitor(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteMonitorErrorBody
```

**Async**

```python
result = await async_client.monitors.with_raw_response.delete_monitor(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;Any, [DeleteMonitorErrorBody](seltz_api/errors/delete_monitor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Deleted. Every record becomes invisible at once.

**On `Failure`**: `error` is <code>[DeleteMonitorErrorBody](seltz_api/errors/delete_monitor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetMonitorResponse, GetMonitorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.monitors.with_raw_response.get_monitor(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMonitorErrorBody
```

**Async**

```python
result = await async_client.monitors.with_raw_response.get_monitor(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[GetMonitorResponse](seltz_api/models/get_monitor_response.py), [GetMonitorErrorBody](seltz_api/errors/get_monitor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetMonitorResponse](seltz_api/models/get_monitor_response.py)</code> -- The monitor.

**On `Failure`**: `error` is <code>[GetMonitorErrorBody](seltz_api/errors/get_monitor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_monitors(*, name: str | None = None, status: str | None = None, since: str | None = None, before: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListMonitorsResponse, ListMonitorsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.monitors.with_raw_response.list_monitors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMonitorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListMonitorsErrorBody
```

**Async**

```python
result = await async_client.monitors.with_raw_response.list_monitors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMonitorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListMonitorsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str \| None</code> | Matches a monitor whose name is exactly this.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | One of `active`, `paused`, `disabled`. `deleted` is not a filter: a<br>deleted monitor is invisible.<br>**Default**: <code>None</code> |
| <code>since</code> | <code>str \| None</code> | Exclusive lower bound: the `monitor_id` of a monitor to start after.<br>**Default**: <code>None</code> |
| <code>before</code> | <code>str \| None</code> | Exclusive upper bound. The list is newest first, so page forward with<br>the `monitor_id` of the last monitor on the previous page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListMonitorsResponse](seltz_api/models/list_monitors_response.py), [ListMonitorsErrorBody](seltz_api/errors/list_monitors_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListMonitorsResponse](seltz_api/models/list_monitors_response.py)</code> -- The org's monitors.

**On `Failure`**: `error` is <code>[ListMonitorsErrorBody](seltz_api/errors/list_monitors_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_monitor(monitor_id: str, body: UpdateMonitorRequest | UpdateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateMonitorResponse, UpdateMonitorErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.monitors.with_raw_response.update_monitor(monitor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateMonitorErrorBody
```

**Async**

```python
result = await async_client.monitors.with_raw_response.update_monitor(monitor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMonitorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UpdateMonitorRequest](seltz_api/models/update_monitor_request.py) \| [UpdateMonitorRequestDict](seltz_api/models/update_monitor_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[UpdateMonitorResponse](seltz_api/models/update_monitor_response.py), [UpdateMonitorErrorBody](seltz_api/errors/update_monitor_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateMonitorResponse](seltz_api/models/update_monitor_response.py)</code> -- Updated.

**On `Failure`**: `error` is <code>[UpdateMonitorErrorBody](seltz_api/errors/update_monitor_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404, 409 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Records

> Source: [Records](seltz_api/apis/records.py)

<details>
<summary><code>def list_records(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListRecordsResponse, ListRecordsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.records.with_raw_response.list_records(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRecordsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRecordsErrorBody
```

**Async**

```python
result = await async_client.records.with_raw_response.list_records(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRecordsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRecordsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>since</code> | <code>str \| None</code> | Exclusive lower bound on `record_id`.<br>**Default**: <code>None</code> |
| <code>before</code> | <code>str \| None</code> | Exclusive upper bound on `record_id`.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first.<br>**Default**: <code>None</code> |
| <code>include_content</code> | <code>bool \| None</code> | Include each record's document content. Defaults to true.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListRecordsResponse](seltz_api/models/list_records_response.py), [ListRecordsErrorBody](seltz_api/errors/list_records_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListRecordsResponse](seltz_api/models/list_records_response.py)</code> -- A page of records.

**On `Failure`**: `error` is <code>[ListRecordsErrorBody](seltz_api/errors/list_records_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_run_records(monitor_id: str, run_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListRunRecordsResponse, ListRunRecordsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound, not a dense sequence.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.records.with_raw_response.list_run_records(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunRecordsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunRecordsErrorBody
```

**Async**

```python
result = await async_client.records.with_raw_response.list_run_records(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunRecordsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunRecordsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>run_id</code> | <code>str</code> | Value sent with the request. |
| <code>since</code> | <code>str \| None</code> | Exclusive lower bound on `record_id`.<br>**Default**: <code>None</code> |
| <code>before</code> | <code>str \| None</code> | Exclusive upper bound on `record_id`.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first.<br>**Default**: <code>None</code> |
| <code>include_content</code> | <code>bool \| None</code> | Include each record's document content. Defaults to true.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListRunRecordsResponse](seltz_api/models/list_run_records_response.py), [ListRunRecordsErrorBody](seltz_api/errors/list_run_records_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListRunRecordsResponse](seltz_api/models/list_run_records_response.py)</code> -- A page of that run's records.

**On `Failure`**: `error` is <code>[ListRunRecordsErrorBody](seltz_api/errors/list_run_records_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Runs

> Source: [Runs](seltz_api/apis/runs.py)

<details>
<summary><code>def get_run(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetRunResponse, GetRunErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.runs.with_raw_response.get_run(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRunErrorBody
```

**Async**

```python
result = await async_client.runs.with_raw_response.get_run(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRunErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>run_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[GetRunResponse](seltz_api/models/get_run_response.py), [GetRunErrorBody](seltz_api/errors/get_run_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetRunResponse](seltz_api/models/get_run_response.py)</code> -- The run. Carries no records and no breakdown.

**On `Failure`**: `error` is <code>[GetRunErrorBody](seltz_api/errors/get_run_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_run_requests(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListRunRequestsResponse, ListRunRequestsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a stream of positives, and absence cannot be inferred from presences.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.runs.with_raw_response.list_run_requests(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunRequestsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunRequestsErrorBody
```

**Async**

```python
result = await async_client.runs.with_raw_response.list_run_requests(monitor_id, run_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunRequestsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunRequestsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>run_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListRunRequestsResponse](seltz_api/models/list_run_requests_response.py), [ListRunRequestsErrorBody](seltz_api/errors/list_run_requests_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListRunRequestsResponse](seltz_api/models/list_run_requests_response.py)</code> -- That run's per-request outcomes.

**On `Failure`**: `error` is <code>[ListRunRequestsErrorBody](seltz_api/errors/list_run_requests_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_runs(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, sort: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListRunsResponse, ListRunsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.runs.with_raw_response.list_runs(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunsErrorBody
```

**Async**

```python
result = await async_client.runs.with_raw_response.list_runs(monitor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRunsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRunsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>str</code> | Value sent with the request. |
| <code>since</code> | <code>str \| None</code> | Exclusive lower bound on `run_id`.<br>**Default**: <code>None</code> |
| <code>before</code> | <code>str \| None</code> | Exclusive upper bound on `run_id`.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Defaults to 100, at most 1,000.<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>str \| None</code> | `desc` (the default, newest first) or `asc`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[ListRunsResponse](seltz_api/models/list_runs_response.py), [ListRunsErrorBody](seltz_api/errors/list_runs_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListRunsResponse](seltz_api/models/list_runs_response.py)</code> -- A page of runs.

**On `Failure`**: `error` is <code>[ListRunsErrorBody](seltz_api/errors/list_runs_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](seltz_api/apis/search.py)

<details>
<summary><code>def search(body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchResponse, SearchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.search.with_raw_response.search(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchErrorBody
```

**Async**

```python
result = await async_client.search.with_raw_response.search(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchRequest](seltz_api/models/search_request.py) \| [SearchRequestDict](seltz_api/models/search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](seltz_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](seltz_api/core/results.py)&#91;[SearchResponse](seltz_api/models/search_response.py), [SearchErrorBody](seltz_api/errors/search_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchResponse](seltz_api/models/search_response.py)</code> -- Search completed. Returns matched documents.

**On `Failure`**: `error` is <code>[SearchErrorBody](seltz_api/errors/search_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 402, 404, 405, 413, 429, 500 | <code>[ErrorEnvelope](seltz_api/models/error_envelope.py)</code> |
| anything unmapped | <code>[RawError](seltz_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

