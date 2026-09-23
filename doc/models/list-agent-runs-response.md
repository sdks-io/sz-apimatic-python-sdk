
# List Agent Runs Response

List-runs response: one page of runs.

*This model accepts additional fields of type Any.*

## Structure

`ListAgentRunsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next` | `str` | Optional | Cursor to the next page. Unset on the last page. |
| `runs` | [`List[AgentRun]`](../../doc/models/agent-run.md) | Optional | The page's runs, newest first. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run import AgentRun
from seltzapi.models.list_agent_runs_response import ListAgentRunsResponse

list_agent_runs_response = ListAgentRunsResponse(
    next='next2',
    runs=[
        None,
        AgentRun()
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

