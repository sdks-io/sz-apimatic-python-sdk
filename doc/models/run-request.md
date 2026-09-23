
# Run Request

One run's outcome for one search request.

*This model accepts additional fields of type Any.*

## Structure

`RunRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `completed_at` | `str` | Optional | - |
| `new_records` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `reason` | `str` | Optional | Why the request failed, empty when it succeeded. Not machine-readable. |
| `request_id` | `str` | Optional | - |
| `results_returned` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `status` | [`RequestStatus`](../../doc/models/request-status.md) | Required | **Default**: `"ok"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.request_status import RequestStatus
from seltzapi.models.run_request import RunRequest

run_request = RunRequest(
    status=RequestStatus.OK,
    completed_at='completed_at4',
    new_records=0,
    reason='reason2',
    request_id='request_id6',
    results_returned=0,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

