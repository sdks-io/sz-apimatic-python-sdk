
# List Run Records Response

*This model accepts additional fields of type Any.*

## Structure

`ListRunRecordsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more` | `bool` | Optional | True when limit or the byte budget cut the page short. Page forward with<br>since = records\[last\].record_id.<br><br>**Default**: `False` |
| `records` | [`List[Record]`](../../doc/models/record.md) | Optional | Oldest first. A short page is normal: a page ends at limit or at a byte<br>budget, whichever binds first. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.list_run_records_response import ListRunRecordsResponse
from seltzapi.models.record import Record
from seltzapi.models.record_type import RecordType
from seltzapi.models.search_record import SearchRecord

list_run_records_response = ListRunRecordsResponse(
    has_more=False,
    records=[
        None,
        Record(
            search_result=SearchRecord(),
            mtype=envrr
        ),
        Record(
            search_result=SearchRecord(),
            mtype=envrr
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

