
# Search Request Ref

*This model accepts additional fields of type Any.*

## Structure

`SearchRequestRef`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Optional | The request's query text, carried here so a record can be rendered without<br>a second lookup. |
| `request_id` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.search_request_ref import SearchRequestRef

search_request_ref = SearchRequestRef(
    query='query0',
    request_id='request_id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

