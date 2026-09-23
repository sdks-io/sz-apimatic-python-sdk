
# Monitor

*This model accepts additional fields of type Any.*

## Structure

`Monitor`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cadence` | `str` | Required | - |
| `created_at` | `str` | Optional | - |
| `monitor_id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `search_requests` | [`List[MonitorSearchRequest]`](../../doc/models/monitor-search-request.md) | Optional | - |
| `status` | [`MonitorStatus`](../../doc/models/monitor-status.md) | Required | **Default**: `"active"` |
| `updated_at` | `str` | Optional | - |
| `webhook` | [`Webhook`](../../doc/models/webhook.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.monitor import Monitor
from seltzapi.models.monitor_status import MonitorStatus

monitor = Monitor(
    cadence='cadence6',
    status=MonitorStatus.ACTIVE,
    created_at='created_at2',
    monitor_id='monitor_id2',
    name='name4',
    search_requests=[
        None
    ],
    updated_at='updated_at0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

