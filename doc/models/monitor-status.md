
# Monitor Status

A monitor's lifecycle state.

`active` is scheduled and running. `paused` runs nothing and keeps its
records and its record of what it has already delivered. Only those two can
be set through the API; `disabled` and `deleted` are set by Seltz.

## Enumeration

`MonitorStatus`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `PAUSED` |
| `DISABLED` |
| `DELETED` |

## Example

```python
from seltzapi.models.monitor_status import MonitorStatus

monitor_status = MonitorStatus.ACTIVE
```

