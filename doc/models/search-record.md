
# Search Record

*This model accepts additional fields of type Any.*

## Structure

`SearchRecord`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document` | [`Document`](../../doc/models/document.md) | Optional | - |
| `matched_requests` | [`List[SearchRequestRef]`](../../doc/models/search-request-ref.md) | Optional | Only the requests that matched in the run that emitted this record. A record<br>is emitted once, on first sight, so a request that would match it in a later<br>run never attaches to it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.search_record import SearchRecord
from seltzapi.models.search_request_ref import SearchRequestRef

search_record = SearchRecord(
    document=None,
    matched_requests=[
        None,
        SearchRequestRef(),
        SearchRequestRef()
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

