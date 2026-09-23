
# Get Monitor Response

*This model accepts additional fields of type Any.*

## Structure

`GetMonitorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor` | [`Monitor`](../../doc/models/monitor.md) | Optional | - |
| `run_state` | [`RunState2`](../../doc/models/run-state-2.md) | Required | **Default**: `"idle"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.get_monitor_response import GetMonitorResponse
from seltzapi.models.run_state_2 import RunState2

get_monitor_response = GetMonitorResponse(
    run_state=RunState2.IDLE,
    monitor=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

