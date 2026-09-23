
# List Monitors Response

*This model accepts additional fields of type Any.*

## Structure

`ListMonitorsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more` | `bool` | Optional | True when limit or the byte budget cut the page short. Page forward with<br>before = monitors\[last\].monitor_id.<br><br>**Default**: `False` |
| `monitors` | [`List[Monitor]`](../../doc/models/monitor.md) | Optional | Newest first. A short page is normal: a page ends at limit or at a byte<br>budget, whichever binds first. A monitor carries its whole request list,<br>so a count alone cannot bound the response. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.list_monitors_response import ListMonitorsResponse
from seltzapi.models.monitor import Monitor
from seltzapi.models.monitor_status import MonitorStatus

list_monitors_response = ListMonitorsResponse(
    has_more=False,
    monitors=[
        None,
        Monitor(
            cadence=None,
            status=envrr
        ),
        Monitor(
            cadence=None,
            status=envrr
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

