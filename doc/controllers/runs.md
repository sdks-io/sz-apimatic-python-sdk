# Runs

Run history and per-request outcomes

```python
runs_api = client.runs
```

## Class Name

`RunsApi`

## Methods

* [List Runs](../../doc/controllers/runs.md#list-runs)
* [Get Run](../../doc/controllers/runs.md#get-run)
* [List Run Requests](../../doc/controllers/runs.md#list-run-requests)


# List Runs

```python
def list_runs(self,
             monitor_id,
             since=None,
             before=None,
             limit=None,
             sort=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `since` | `str` | Query, Optional | Exclusive lower bound on `run_id`. |
| `before` | `str` | Query, Optional | Exclusive upper bound on `run_id`. |
| `limit` | `int` | Query, Optional | Defaults to 100, at most 1,000. |
| `sort` | `str` | Query, Optional | `desc` (the default, newest first) or `asc`. |

## Response Type

**200**: A page of runs.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListRunsResponse`](../../doc/models/list-runs-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

result = runs_api.list_runs(monitor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such monitor in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Get Run

```python
def get_run(self,
           monitor_id,
           run_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `run_id` | `str` | Template, Required | - |

## Response Type

**200**: The run. Carries no records and no breakdown.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetRunResponse`](../../doc/models/get-run-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

run_id = 'run_id8'

result = runs_api.get_run(
    monitor_id,
    run_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such run on this monitor. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# List Run Requests

The only place a customer can tell *this query failed* from *there was genuinely nothing new*: records are a stream of positives, and absence cannot be inferred from presences.

```python
def list_run_requests(self,
                     monitor_id,
                     run_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `run_id` | `str` | Template, Required | - |

## Response Type

**200**: That run's per-request outcomes.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListRunRequestsResponse`](../../doc/models/list-run-requests-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

run_id = 'run_id8'

result = runs_api.list_run_requests(
    monitor_id,
    run_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such run on this monitor. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

