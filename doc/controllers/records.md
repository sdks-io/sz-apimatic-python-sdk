# Records

The delivered records

```python
records_api = client.records
```

## Class Name

`RecordsApi`

## Methods

* [List Records](../../doc/controllers/records.md#list-records)
* [List Run Records](../../doc/controllers/records.md#list-run-records)


# List Records

```python
def list_records(self,
                monitor_id,
                since=None,
                before=None,
                limit=None,
                include_content=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `since` | `str` | Query, Optional | Exclusive lower bound on `record_id`. |
| `before` | `str` | Query, Optional | Exclusive upper bound on `record_id`. |
| `limit` | `int` | Query, Optional | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first. |
| `include_content` | `bool` | Query, Optional | Include each record's document content. Defaults to true. |

## Response Type

**200**: A page of records.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListRecordsResponse`](../../doc/models/list-records-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

result = records_api.list_records(monitor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such monitor in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# List Run Records

Exists so that no consumer does arithmetic on a record id: a webhook carries a run's record range as a bound, not a dense sequence.

```python
def list_run_records(self,
                    monitor_id,
                    run_id,
                    since=None,
                    before=None,
                    limit=None,
                    include_content=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `run_id` | `str` | Template, Required | - |
| `since` | `str` | Query, Optional | Exclusive lower bound on `record_id`. |
| `before` | `str` | Query, Optional | Exclusive upper bound on `record_id`. |
| `limit` | `int` | Query, Optional | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first. |
| `include_content` | `bool` | Query, Optional | Include each record's document content. Defaults to true. |

## Response Type

**200**: A page of that run's records.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListRunRecordsResponse`](../../doc/models/list-run-records-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

run_id = 'run_id8'

result = records_api.list_run_records(
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

