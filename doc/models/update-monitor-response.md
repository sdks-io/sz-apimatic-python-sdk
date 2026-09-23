
# Update Monitor Response

*This model accepts additional fields of type Any.*

## Structure

`UpdateMonitorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor` | [`Monitor`](../../doc/models/monitor.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.update_monitor_response import UpdateMonitorResponse

update_monitor_response = UpdateMonitorResponse(
    monitor=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

