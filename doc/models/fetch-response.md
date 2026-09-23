
# Fetch Response

One result per requested URL.

*This model accepts additional fields of type Any.*

## Structure

`FetchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `results` | [`List[FetchResult]`](../../doc/models/fetch-result.md) | Optional | One entry per entry in `FetchRequest.urls`, successful or not, in the order<br>the URLs were requested.<br><br>Correlate on `FetchResult.requested_url` rather than on position. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.fetch_response import FetchResponse

fetch_response = FetchResponse(
    results=[
        None
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

