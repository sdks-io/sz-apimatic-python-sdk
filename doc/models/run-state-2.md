
# Run State 2

Live run state. Returned by this RPC only — the list endpoints do not
include it.

## Enumeration

`RunState2`

## Fields

| Name |
|  --- |
| `IDLE` |
| `RUNNING` |
| `UNKNOWN` |

## Example

```python
from seltzapi.models.run_state_2 import RunState2

run_state_2 = RunState2.UNKNOWN
```

