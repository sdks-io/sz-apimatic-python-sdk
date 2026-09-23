
# Record

*This model accepts additional fields of type Any.*

## Structure

`Record`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_result` | [`SearchRecord`](../../doc/models/search-record.md) | Required | - |
| `first_seen_at` | `str` | Optional | - |
| `record_id` | `str` | Optional | **Default**: `"0"` |
| `run_id` | `str` | Optional | **Default**: `"0"` |
| `mtype` | [`RecordType`](../../doc/models/record-type.md) | Required | **Default**: `"search_result"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.record import Record
from seltzapi.models.record_type import RecordType
from seltzapi.models.search_record import SearchRecord

record = Record(
    search_result=SearchRecord(
        document=None,
        matched_requests=[
            None
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mtype=RecordType.SEARCH_RESULT,
    first_seen_at='first_seen_at0',
    record_id='0',
    run_id='0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

