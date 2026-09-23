
# Agent Run

An agent run.

*This model accepts additional fields of type Any.*

## Structure

`AgentRun`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `completed_at` | `str` | Optional | When the run reached a terminal state. Unset until then. |
| `created_at` | `str` | Optional | When the run was created, as an ISO 8601 timestamp. |
| `id` | `str` | Optional | Unique run id. |
| `object` | `str` | Optional | Object type, always "agent.run". |
| `output` | [`AgentRunOutput2`](../../doc/models/agent-run-output-2.md) | Optional | - |
| `request` | [`AgentRunRequest2`](../../doc/models/agent-run-request-2.md) | Optional | - |
| `started_at` | `str` | Optional | When the run started. Unset while pending. |
| `status` | [`AgentRunStatus2`](../../doc/models/agent-run-status-2.md) | Optional | **Default**: `"pending"` |
| `stop_reason` | [`AgentRunStopReason2`](../../doc/models/agent-run-stop-reason-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run import AgentRun
from seltzapi.models.agent_run_status_2 import AgentRunStatus2

agent_run = AgentRun(
    completed_at='completed_at8',
    created_at='created_at4',
    id='id6',
    object='object6',
    output=None,
    status=AgentRunStatus2.PENDING,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

