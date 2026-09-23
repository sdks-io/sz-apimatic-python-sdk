
# Webhook 1

JSON `null` clears the webhook; an absent field keeps it. Set
`webhook.status` to turn delivery on or off.

*This model accepts additional fields of type Any.*

## Structure

`Webhook1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | `List[str]` | Optional | Exactly two strings are legal: "run.completed" and "run.failed". An empty<br>list is rejected.<br><br>"run.completed" means the run finished. Read the run's `record_count` to<br>see whether it produced records and its `status` to see whether every<br>request succeeded. "run.failed" means no request succeeded. Neither fires<br>for a skipped run. |
| `status` | `str` | Optional | Always reported on a monitor. Send ACTIVE to turn delivery back on once a<br>failing endpoint is repaired, or DISABLED to stop it yourself.<br><br>A disabled webhook stops the POST only. The monitor still runs and its<br>records are still readable through the records cursor, so nothing is lost<br>while it is off.<br><br>On the way in it is the one field of this message that may be omitted: an<br>absent status keeps whatever the monitor already has, so re-sending a<br>webhook body does not by itself restart delivery to a dead endpoint. |
| `url` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.webhook_1 import Webhook1

webhook_1 = Webhook1(
    events=[
        'events6'
    ],
    status='status8',
    url='url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

