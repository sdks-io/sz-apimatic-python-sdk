
# Document

A single search result.

`url` and `published_date` are returned without being asked for, and either
may still be absent for a document that carries no such value. The remaining
members are populated only when `SearchRequest.fields` asked for them.

*This model accepts additional fields of type Any.*

## Structure

`Document`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | - |
| `published_date` | `str` | Optional | Publication date as ISO 8601 string (e.g. "2024-03-15T00:00:00Z") |
| `snippets` | [`List[Snippet]`](../../doc/models/snippet.md) | Optional | The document's highest-scoring snippets, in the order they appear in the document.<br><br>Populated when `fields.snippets` is selected and passages are available;<br>empty otherwise. |
| `url` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.document import Document
from seltzapi.models.snippet import Snippet

document = Document(
    content='content0',
    published_date='published_date0',
    snippets=[
        None,
        Snippet()
    ],
    url='url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

