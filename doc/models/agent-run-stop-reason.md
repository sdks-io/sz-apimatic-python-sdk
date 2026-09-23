
# Agent Run Stop Reason

Why a run stopped. `budget_reached` pairs with `completed` when the output
so far is usable and with `failed` when it is not.

## Enumeration

`AgentRunStopReason`

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
from seltzapi.models.agent_run_stop_reason import AgentRunStopReason

agent_run_stop_reason = AgentRunStopReason.TIMEOUT
```

