
# Search Response

*This model accepts additional fields of type Any.*

## Structure

`SearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | [`List[Document]`](../../doc/models/document.md) | Optional | Documents that are most relevant to the query |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.document import Document
from seltzapi.models.search_response import SearchResponse

search_response = SearchResponse(
    documents=[
        None,
        Document(),
        Document()
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

