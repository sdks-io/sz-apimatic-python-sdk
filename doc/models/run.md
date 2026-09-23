
# Run

*This model accepts additional fields of type Any.*

## Structure

`Run`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `completed_at` | `str` | Optional | - |
| `first_record_id` | `str` | Optional | The lowest `record_id` this run produced. Records are not contiguous; use<br>`record_count` for the count.<br><br>**Default**: `"0"` |
| `last_record_id` | `str` | Optional | The highest `record_id` this run produced. Records are not contiguous; use<br>`record_count` for the count.<br><br>**Default**: `"0"` |
| `monitor_id` | `str` | Optional | - |
| `record_count` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `requests_failed` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `requests_ok` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `requests_total` | `int` | Optional | **Default**: `0`<br><br>**Constraints**: `>= 0` |
| `run_id` | `str` | Optional | **Default**: `"0"` |
| `started_at` | `str` | Optional | - |
| `status` | [`RunStatus`](../../doc/models/run-status.md) | Required | **Default**: `"completed"` |
| `status_reason` | `str` | Optional | Prose for a human, empty when completed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.run import Run
from seltzapi.models.run_status import RunStatus

run = Run(
    status=RunStatus.COMPLETED,
    completed_at='completed_at0',
    first_record_id='0',
    last_record_id='0',
    monitor_id='monitor_id6',
    record_count=0,
    requests_failed=0,
    requests_ok=0,
    requests_total=0,
    run_id='0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

