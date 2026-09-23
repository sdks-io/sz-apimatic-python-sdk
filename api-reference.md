# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [SeltzApiClient](seltz_api/client.py)

## Agent

> Source: [Agent](seltz_api/apis/agent.py)

<details>
<summary><code>def cancel_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun</code></summary>

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
try:
    response = client.agent.cancel_agent_run(id)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAgentRunErrorBody
```

**Async**

```python
try:
    response = await async_client.agent.cancel_agent_run(id)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelAgentRunErrorBody
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

**OnSuccess**: <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The run.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[CancelAgentRunErrorBody](seltz_api/errors/cancel_agent_run_error.py)&#93;</code>

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
<summary><code>def create_agent_run(body: CreateAgentRunRequest | CreateAgentRunRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun</code></summary>

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
try:
    response = client.agent.create_agent_run(body)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAgentRunErrorBody
```

**Async**

```python
try:
    response = await async_client.agent.create_agent_run(body)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAgentRunErrorBody
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

**OnSuccess**: <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The new run, in `pending` state.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[CreateAgentRunErrorBody](seltz_api/errors/create_agent_run_error.py)&#93;</code>

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
<summary><code>def get_agent_run(id: str, *, request_options: RequestOptionsOrDict | None = None) -> AgentRun</code></summary>

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
try:
    response = client.agent.get_agent_run(id)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAgentRunErrorBody
```

**Async**

```python
try:
    response = await async_client.agent.get_agent_run(id)
    # TODO: Handle 'response' of type AgentRun
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAgentRunErrorBody
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

**OnSuccess**: <code>[AgentRun](seltz_api/models/agent_run.py)</code> -- The run.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[GetAgentRunErrorBody](seltz_api/errors/get_agent_run_error.py)&#93;</code>

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
<summary><code>def list_agent_runs(*, limit: int | None = None, after: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListAgentRunsResponse</code></summary>

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
try:
    response = client.agent.list_agent_runs()
    # TODO: Handle 'response' of type ListAgentRunsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAgentRunsErrorBody
```

**Async**

```python
try:
    response = await async_client.agent.list_agent_runs()
    # TODO: Handle 'response' of type ListAgentRunsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAgentRunsErrorBody
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

**OnSuccess**: <code>[ListAgentRunsResponse](seltz_api/models/list_agent_runs_response.py)</code> -- One page of runs, newest first.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListAgentRunsErrorBody](seltz_api/errors/list_agent_runs_error.py)&#93;</code>

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
<summary><code>def answer(body: AnswerHttpRequest | AnswerHttpRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AnswerHttpResponse</code></summary>

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
try:
    response = client.answer.answer(body)
    # TODO: Handle 'response' of type AnswerHttpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AnswerErrorBody
```

**Async**

```python
try:
    response = await async_client.answer.answer(body)
    # TODO: Handle 'response' of type AnswerHttpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AnswerErrorBody
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

**OnSuccess**: <code>[AnswerHttpResponse](seltz_api/models/answer_http_response.py)</code> -- Answer for the query. When `stream = false` the body is a JSON `AnswerHttpResponse`; when `stream = true` it is a `text/event-stream` of OpenAI-style chunks.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[AnswerErrorBody](seltz_api/errors/answer_error.py)&#93;</code>

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
<summary><code>def fetch(body: FetchRequest | FetchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FetchResponse</code></summary>

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
try:
    response = client.fetch.fetch(body)
    # TODO: Handle 'response' of type FetchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchErrorBody
```

**Async**

```python
try:
    response = await async_client.fetch.fetch(body)
    # TODO: Handle 'response' of type FetchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type FetchErrorBody
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

**OnSuccess**: <code>[FetchResponse](seltz_api/models/fetch_response.py)</code> -- One result per requested URL. A failure to fetch a page is still a 200, with that result's `status = "error"`.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[FetchErrorBody](seltz_api/errors/fetch_error.py)&#93;</code>

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
<summary><code>def create_monitor(body: CreateMonitorRequest | CreateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateMonitorResponse</code></summary>

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
try:
    response = client.monitors.create_monitor(body)
    # TODO: Handle 'response' of type CreateMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitors.create_monitor(body)
    # TODO: Handle 'response' of type CreateMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMonitorErrorBody
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

**OnSuccess**: <code>[CreateMonitorResponse](seltz_api/models/create_monitor_response.py)</code> -- Created. `webhook_secret` is returned once and never again.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[CreateMonitorErrorBody](seltz_api/errors/create_monitor_error.py)&#93;</code>

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
<summary><code>def delete_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.monitors.delete_monitor(monitor_id)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitors.delete_monitor(monitor_id)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMonitorErrorBody
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

**OnSuccess**: <code>Any</code> -- Deleted. Every record becomes invisible at once.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[DeleteMonitorErrorBody](seltz_api/errors/delete_monitor_error.py)&#93;</code>

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
<summary><code>def get_monitor(monitor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetMonitorResponse</code></summary>

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
try:
    response = client.monitors.get_monitor(monitor_id)
    # TODO: Handle 'response' of type GetMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitors.get_monitor(monitor_id)
    # TODO: Handle 'response' of type GetMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorErrorBody
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

**OnSuccess**: <code>[GetMonitorResponse](seltz_api/models/get_monitor_response.py)</code> -- The monitor.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[GetMonitorErrorBody](seltz_api/errors/get_monitor_error.py)&#93;</code>

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
<summary><code>def list_monitors(*, name: str | None = None, status: str | None = None, since: str | None = None, before: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ListMonitorsResponse</code></summary>

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
try:
    response = client.monitors.list_monitors()
    # TODO: Handle 'response' of type ListMonitorsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListMonitorsErrorBody
```

**Async**

```python
try:
    response = await async_client.monitors.list_monitors()
    # TODO: Handle 'response' of type ListMonitorsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListMonitorsErrorBody
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

**OnSuccess**: <code>[ListMonitorsResponse](seltz_api/models/list_monitors_response.py)</code> -- The org's monitors.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListMonitorsErrorBody](seltz_api/errors/list_monitors_error.py)&#93;</code>

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
<summary><code>def update_monitor(monitor_id: str, body: UpdateMonitorRequest | UpdateMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateMonitorResponse</code></summary>

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
try:
    response = client.monitors.update_monitor(monitor_id, body)
    # TODO: Handle 'response' of type UpdateMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitors.update_monitor(monitor_id, body)
    # TODO: Handle 'response' of type UpdateMonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMonitorErrorBody
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

**OnSuccess**: <code>[UpdateMonitorResponse](seltz_api/models/update_monitor_response.py)</code> -- Updated.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[UpdateMonitorErrorBody](seltz_api/errors/update_monitor_error.py)&#93;</code>

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
<summary><code>def list_records(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ListRecordsResponse</code></summary>

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
try:
    response = client.records.list_records(monitor_id)
    # TODO: Handle 'response' of type ListRecordsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRecordsErrorBody
```

**Async**

```python
try:
    response = await async_client.records.list_records(monitor_id)
    # TODO: Handle 'response' of type ListRecordsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRecordsErrorBody
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

**OnSuccess**: <code>[ListRecordsResponse](seltz_api/models/list_records_response.py)</code> -- A page of records.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListRecordsErrorBody](seltz_api/errors/list_records_error.py)&#93;</code>

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
<summary><code>def list_run_records(monitor_id: str, run_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, include_content: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ListRunRecordsResponse</code></summary>

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
try:
    response = client.records.list_run_records(monitor_id, run_id)
    # TODO: Handle 'response' of type ListRunRecordsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunRecordsErrorBody
```

**Async**

```python
try:
    response = await async_client.records.list_run_records(monitor_id, run_id)
    # TODO: Handle 'response' of type ListRunRecordsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunRecordsErrorBody
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

**OnSuccess**: <code>[ListRunRecordsResponse](seltz_api/models/list_run_records_response.py)</code> -- A page of that run's records.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListRunRecordsErrorBody](seltz_api/errors/list_run_records_error.py)&#93;</code>

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
<summary><code>def get_run(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetRunResponse</code></summary>

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
try:
    response = client.runs.get_run(monitor_id, run_id)
    # TODO: Handle 'response' of type GetRunResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRunErrorBody
```

**Async**

```python
try:
    response = await async_client.runs.get_run(monitor_id, run_id)
    # TODO: Handle 'response' of type GetRunResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRunErrorBody
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

**OnSuccess**: <code>[GetRunResponse](seltz_api/models/get_run_response.py)</code> -- The run. Carries no records and no breakdown.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[GetRunErrorBody](seltz_api/errors/get_run_error.py)&#93;</code>

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
<summary><code>def list_run_requests(monitor_id: str, run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ListRunRequestsResponse</code></summary>

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
try:
    response = client.runs.list_run_requests(monitor_id, run_id)
    # TODO: Handle 'response' of type ListRunRequestsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunRequestsErrorBody
```

**Async**

```python
try:
    response = await async_client.runs.list_run_requests(monitor_id, run_id)
    # TODO: Handle 'response' of type ListRunRequestsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunRequestsErrorBody
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

**OnSuccess**: <code>[ListRunRequestsResponse](seltz_api/models/list_run_requests_response.py)</code> -- That run's per-request outcomes.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListRunRequestsErrorBody](seltz_api/errors/list_run_requests_error.py)&#93;</code>

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
<summary><code>def list_runs(monitor_id: str, *, since: str | None = None, before: str | None = None, limit: int | None = None, sort: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListRunsResponse</code></summary>

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
try:
    response = client.runs.list_runs(monitor_id)
    # TODO: Handle 'response' of type ListRunsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunsErrorBody
```

**Async**

```python
try:
    response = await async_client.runs.list_runs(monitor_id)
    # TODO: Handle 'response' of type ListRunsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRunsErrorBody
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

**OnSuccess**: <code>[ListRunsResponse](seltz_api/models/list_runs_response.py)</code> -- A page of runs.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[ListRunsErrorBody](seltz_api/errors/list_runs_error.py)&#93;</code>

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
<summary><code>def search(body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchResponse</code></summary>

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
try:
    response = client.search.search(body)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchErrorBody
```

**Async**

```python
try:
    response = await async_client.search.search(body)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchErrorBody
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

**OnSuccess**: <code>[SearchResponse](seltz_api/models/search_response.py)</code> -- Search completed. Returns matched documents.

**OnError**: <code>[ApiError](seltz_api/core/exceptions.py)&#91;[SearchErrorBody](seltz_api/errors/search_error.py)&#93;</code>

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

