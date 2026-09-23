
# Agent Run Status

Where a run is in its lifecycle:
pending → running → completed / failed / cancelled.

## Enumeration

`AgentRunStatus`

## Fields

| Name |
|  --- |
| `PENDING` |
| `RUNNING` |
| `COMPLETED` |
| `FAILED` |
| `CANCELLED` |

## Example

```python
from seltzapi.models.agent_run_status import AgentRunStatus

agent_run_status = AgentRunStatus.RUNNING
```

