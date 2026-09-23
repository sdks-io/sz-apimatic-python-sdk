
# Envelope Error 1

The error context.

*This model accepts additional fields of type Any.*

## Structure

`EnvelopeError1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | The error code. |
| `message` | `str` | Required | The error message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.envelope_error_1 import EnvelopeError1

envelope_error_1 = EnvelopeError1(
    code='code2',
    message='message4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

