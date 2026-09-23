
# Payload

*This model accepts additional fields of type Any.*

## Structure

`Payload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_result` | [`SearchRecord`](../../doc/models/search-record.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.payload import Payload
from seltzapi.models.search_record import SearchRecord

payload = Payload(
    search_result=SearchRecord(
        document=None,
        matched_requests=[
            None
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

