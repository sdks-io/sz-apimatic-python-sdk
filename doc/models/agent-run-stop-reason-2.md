
# Agent Run Stop Reason 2

Why the run stopped. Set once the run reaches a terminal state.

## Enumeration

`AgentRunStopReason2`

## Fields

| Name |
|  --- |
| `FINISHED` |
| `BUDGET_REACHED` |
| `TIMEOUT` |
| `CANCELLED` |
| `INVALID_OUTPUT` |
| `INTERNAL_ERROR` |

## Example

```python
from seltzapi.models.agent_run_stop_reason_2 import AgentRunStopReason2

agent_run_stop_reason_2 = AgentRunStopReason2.TIMEOUT
```

