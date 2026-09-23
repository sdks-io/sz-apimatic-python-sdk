
# Monitor Search Request

A search request stored on a monitor, with its server-assigned id.

*This model accepts additional fields of type Any.*

## Structure

`MonitorSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `consecutive_failures` | `int` | Optional | Consecutive failed runs for this request.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `last_success_at` | `str` | Optional | - |
| `request` | [`SearchRequest`](../../doc/models/search-request.md) | Optional | - |
| `request_id` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.monitor_search_request import MonitorSearchRequest

monitor_search_request = MonitorSearchRequest(
    consecutive_failures=0,
    last_success_at='last_success_at6',
    request=None,
    request_id='request_id6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

