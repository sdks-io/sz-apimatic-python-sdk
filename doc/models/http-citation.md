
# Http Citation

HTTP-shape citation. Mirrors the `Citation` proto.

*This model accepts additional fields of type Any.*

## Structure

`HttpCitation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | Document content text (only when `include_content = true`). |
| `url` | `str` | Required | URL of the source document. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.http_citation import HttpCitation

http_citation = HttpCitation(
    url='url8',
    content='content8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

