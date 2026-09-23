
# Fields

The selectable members of a response `Document`, and how much of each to return.

`Document.url` and `Document.published_date` are always selected.

Each member takes `true`, `false`, or an object of ceilings. An object selects the member and
bounds it, so `{"content": {"max_characters_per_result": 500}}` returns content and no
snippets. `{"content": true}` selects content under the default ceiling, which is what
`{"content": {}}` returns as well. `false` switches the member off.

A `fields` that names neither member returns the defaults below, so `{}` and a wholly absent
`fields` mean the same thing. A `fields` that names either is read literally, so
`{"snippets": true}` returns passages and no content.

*This model accepts additional fields of type Any.*

## Structure

`Fields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | bool \| [ContentOptions](../../doc/models/content-options.md) \| None | Optional | This is a container for one-of cases. |
| `snippets` | bool \| [SnippetOptions](../../doc/models/snippet-options.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.fields import Fields

fields = Fields(
    content=True,
    snippets=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

