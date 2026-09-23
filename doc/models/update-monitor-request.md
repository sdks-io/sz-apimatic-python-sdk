
# Update Monitor Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateMonitorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cadence` | `str` | Required | - |
| `api_key` | `str` | Optional | - |
| `monitor_id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `search_requests` | [`List[SearchRequest]`](../../doc/models/search-request.md) | Optional | Replaces the list wholesale when set. An empty list is read as "not set"<br>and keeps the current requests. A request keeps its id and its health when<br>every field of its body is unchanged. |
| `status` | [`MonitorStatus`](../../doc/models/monitor-status.md) | Optional | - |
| `webhook` | [`Webhook1`](../../doc/models/webhook-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.monitor_status import MonitorStatus
from seltzapi.models.update_monitor_request import UpdateMonitorRequest

update_monitor_request = UpdateMonitorRequest(
    cadence='cadence6',
    api_key='api_key8',
    monitor_id='monitor_id2',
    name='name4',
    search_requests=[
        None
    ],
    status=MonitorStatus.DISABLED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

