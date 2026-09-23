
# Error Envelope Exception

The response body returned for any error.

*This model accepts additional fields of type Any.*

## Structure

`ErrorEnvelopeException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | [`EnvelopeError1`](../../doc/models/envelope-error-1.md) | Required | The error context. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ErrorEnvelopeException as e:
    print(e)
except ApiException as e:
    print(e)
```

