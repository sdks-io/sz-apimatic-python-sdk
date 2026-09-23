
# List Records Response

*This model accepts additional fields of type Any.*

## Structure

`ListRecordsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more` | `bool` | Optional | True when limit or the byte budget cut the page short. Page forward with<br>since = records\[last\].record_id.<br><br>**Default**: `False` |
| `records` | [`List[Record]`](../../doc/models/record.md) | Optional | Oldest first. A short page is normal: a page ends at limit or at a byte<br>budget, whichever binds first. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.list_records_response import ListRecordsResponse

list_records_response = ListRecordsResponse(
    has_more=False,
    records=[
        None
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

