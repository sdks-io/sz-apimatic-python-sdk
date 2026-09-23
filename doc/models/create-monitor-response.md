
# Create Monitor Response

*This model accepts additional fields of type Any.*

## Structure

`CreateMonitorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monitor` | [`Monitor`](../../doc/models/monitor.md) | Optional | - |
| `webhook_secret` | `str` | Optional | Returned once, at create, and never again. Issued whether or not the<br>create supplied a webhook, so keep it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.create_monitor_response import CreateMonitorResponse

create_monitor_response = CreateMonitorResponse(
    monitor=None,
    webhook_secret='webhook_secret4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

