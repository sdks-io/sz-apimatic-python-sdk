
# Monitor Status 2

Set to `paused` to create the monitor without starting it. Only `active`
and `paused` are accepted. Defaults to `active`.

## Enumeration

`MonitorStatus2`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `PAUSED` |
| `DISABLED` |
| `DELETED` |

## Example

```python
from seltzapi.models.monitor_status_2 import MonitorStatus2

monitor_status_2 = MonitorStatus2.ACTIVE
```

