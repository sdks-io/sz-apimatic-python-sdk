
# Content Options

The ceiling on the content returned.

The ceiling is an upper bound; the response carries at most what is specified here.

The service may hold callers to a tighter bound than the range below. A larger
request is then served at that bound rather than refused, which still carries at
most what was specified. Only a value outside the range below is rejected.

*This model accepts additional fields of type Any.*

## Structure

`ContentOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_characters_per_result` | `int` | Optional | Ceiling on the characters of any single result's content.<br><br>Counts Unicode code points -- Rust `char`, Python `len(s)`, JavaScript `\[...s\].length`.<br><br>Defaults to 20000, accepted range 100-1000000.<br><br>**Constraints**: `>= 100`, `<= 1000000` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.content_options import ContentOptions

content_options = ContentOptions(
    max_characters_per_result=188,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

