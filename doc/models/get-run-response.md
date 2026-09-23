
# Get Run Response

*This model accepts additional fields of type Any.*

## Structure

`GetRunResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `run` | [`Run`](../../doc/models/run.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.get_run_response import GetRunResponse

get_run_response = GetRunResponse(
    run=None,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

