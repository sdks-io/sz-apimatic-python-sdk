
# Envelope Error

The error context. `code` is a stable descriptor in all-caps from a closed
set per endpoint. `message` is a human-readable summary of what went wrong.

*This model accepts additional fields of type Any.*

## Structure

`EnvelopeError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | The error code. |
| `message` | `str` | Required | The error message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.envelope_error import EnvelopeError

envelope_error = EnvelopeError(
    code='code6',
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

