
# Fields 2

Which selectable members of `Document` to populate.

If absent, defaults to `{content: true}`, which returns content under the
default ceiling stated on `ContentOptions`.

*This model accepts additional fields of type Any.*

## Structure

`Fields2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | bool \| [ContentOptions](../../doc/models/content-options.md) \| None | Optional | This is a container for one-of cases. |
| `snippets` | bool \| [SnippetOptions](../../doc/models/snippet-options.md) \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.fields_2 import Fields2

fields_2 = Fields2(
    content=True,
    snippets=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

