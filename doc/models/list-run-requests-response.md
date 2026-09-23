
# List Run Requests Response

*This model accepts additional fields of type Any.*

## Structure

`ListRunRequestsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requests` | [`List[RunRequest]`](../../doc/models/run-request.md) | Optional | Ordered by request_id. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.list_run_requests_response import ListRunRequestsResponse
from seltzapi.models.request_status import RequestStatus
from seltzapi.models.run_request import RunRequest

list_run_requests_response = ListRunRequestsResponse(
    requests=[
        None,
        RunRequest(
            status=envrr
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

