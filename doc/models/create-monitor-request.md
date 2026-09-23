
# Create Monitor Request

*This model accepts additional fields of type Any.*

## Structure

`CreateMonitorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cadence` | `str` | Required | - |
| `api_key` | `str` | Optional | - |
| `name` | `str` | Optional | Unique per org among live monitors; a deleted monitor's name becomes<br>available again. At most 512 bytes of UTF-8. |
| `search_requests` | [`List[SearchRequest]`](../../doc/models/search-request.md) | Optional | At least one, at most 1000. Every request runs on every run. A request<br>with an `api_key` set, a blank `query`, or a body identical to another in<br>the list is rejected. |
| `status` | [`MonitorStatus2`](../../doc/models/monitor-status-2.md) | Optional | - |
| `webhook` | [`Webhook`](../../doc/models/webhook.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.create_monitor_request import CreateMonitorRequest
from seltzapi.models.monitor_status_2 import MonitorStatus2
from seltzapi.models.search_request import SearchRequest

create_monitor_request = CreateMonitorRequest(
    cadence='cadence2',
    api_key='api_key6',
    name='name6',
    search_requests=[
        None,
        SearchRequest(),
        SearchRequest()
    ],
    status=MonitorStatus2.ACTIVE,
    webhook=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

