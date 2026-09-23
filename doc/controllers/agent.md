# Agent

Agent runs: create, poll, list, cancel

```python
agent_api = client.agent
```

## Class Name

`AgentApi`

## Methods

* [List Agent Runs](../../doc/controllers/agent.md#list-agent-runs)
* [Create Agent Run](../../doc/controllers/agent.md#create-agent-run)
* [Get Agent Run](../../doc/controllers/agent.md#get-agent-run)
* [Cancel Agent Run](../../doc/controllers/agent.md#cancel-agent-run)


# List Agent Runs

The organization's runs, newest first. Pass one page's `next` as the following request's `after`.

```python
def list_agent_runs(self,
                   limit=None,
                   after=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Page size, 1-100. Defaults to 20. |
| `after` | `str` | Query, Optional | Pagination cursor: the previous page's `next`. |

## Response Type

**200**: One page of runs, newest first.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListAgentRunsResponse`](../../doc/models/list-agent-runs-response.md).

## Example Usage

```python
result = agent_api.list_agent_runs()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Malformed or unknown query parameter. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 404 | Unknown `after` cursor. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Create Agent Run

Returns the new run in `pending` state. Poll it by id until `status` reaches a terminal state.

```python
def create_agent_run(self,
                    body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateAgentRunRequest`](../../doc/models/create-agent-run-request.md) | Body, Required | - |

## Response Type

**201**: The new run, in `pending` state.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentRun`](../../doc/models/agent-run.md).

## Example Usage

```python
body = CreateAgentRunRequest()

result = agent_api.create_agent_run(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Malformed body, unknown field, unknown `effort`, or a rejected `output_schema`. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 402 | Insufficient credits. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Get Agent Run

Poll until `status` reaches a terminal state.

```python
def get_agent_run(self,
                 id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The run id. |

## Response Type

**200**: The run.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentRun`](../../doc/models/agent-run.md).

## Example Usage

```python
id = 'id0'

result = agent_api.get_agent_run(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 404 | No such run in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Cancel Agent Run

Stop a run that has not finished. Returns the run, unchanged if it had already ended, so cancelling is safe to retry.

```python
def cancel_agent_run(self,
                    id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The run id. |

## Response Type

**200**: The run.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentRun`](../../doc/models/agent-run.md).

## Example Usage

```python
id = 'id0'

result = agent_api.cancel_agent_run(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 404 | No such run in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

