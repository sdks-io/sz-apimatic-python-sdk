# Monitors

Monitor configuration

```python
monitors_api = client.monitors
```

## Class Name

`MonitorsApi`

## Methods

* [List Monitors](../../doc/controllers/monitors.md#list-monitors)
* [Create Monitor](../../doc/controllers/monitors.md#create-monitor)
* [Get Monitor](../../doc/controllers/monitors.md#get-monitor)
* [Delete Monitor](../../doc/controllers/monitors.md#delete-monitor)
* [Update Monitor](../../doc/controllers/monitors.md#update-monitor)


# List Monitors

```python
def list_monitors(self,
                 name=None,
                 status=None,
                 since=None,
                 before=None,
                 limit=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Query, Optional | Matches a monitor whose name is exactly this. |
| `status` | `str` | Query, Optional | One of `active`, `paused`, `disabled`. `deleted` is not a filter: a<br>deleted monitor is invisible. |
| `since` | `str` | Query, Optional | Exclusive lower bound: the `monitor_id` of a monitor to start after. |
| `before` | `str` | Query, Optional | Exclusive upper bound. The list is newest first, so page forward with<br>the `monitor_id` of the last monitor on the previous page. |
| `limit` | `int` | Query, Optional | Defaults to 100, at most 1,000. A short page is normal: a page ends at<br>`limit` or at the byte budget, whichever binds first. |

## Response Type

**200**: The org's monitors.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListMonitorsResponse`](../../doc/models/list-monitors-response.md).

## Example Usage

```python
result = monitors_api.list_monitors()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Create Monitor

```python
def create_monitor(self,
                  body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateMonitorRequest`](../../doc/models/create-monitor-request.md) | Body, Required | - |

## Response Type

**201**: Created. `webhook_secret` is returned once and never again.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateMonitorResponse`](../../doc/models/create-monitor-response.md).

## Example Usage

```python
body = CreateMonitorRequest(
    cadence='cadence2'
)

result = monitors_api.create_monitor(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Missing or malformed fields. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 409 | That name is already taken in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Get Monitor

```python
def get_monitor(self,
               monitor_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |

## Response Type

**200**: The monitor.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetMonitorResponse`](../../doc/models/get-monitor-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

result = monitors_api.get_monitor(monitor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such monitor in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Delete Monitor

```python
def delete_monitor(self,
                  monitor_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |

## Response Type

**200**: Deleted. Every record becomes invisible at once.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
monitor_id = 'monitor_id2'

result = monitors_api.delete_monitor(monitor_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such monitor in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |


# Update Monitor

```python
def update_monitor(self,
                  monitor_id,
                  body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor_id` | `str` | Template, Required | - |
| `body` | [`UpdateMonitorRequest`](../../doc/models/update-monitor-request.md) | Body, Required | - |

## Response Type

**200**: Updated.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateMonitorResponse`](../../doc/models/update-monitor-response.md).

## Example Usage

```python
monitor_id = 'monitor_id2'

body = UpdateMonitorRequest(
    cadence='cadence2'
)

result = monitors_api.update_monitor(
    monitor_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | No such monitor in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 409 | That name is already taken in this org. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

