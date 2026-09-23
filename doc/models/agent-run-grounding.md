
# Agent Run Grounding

Citations for one field of `output.structured`.

*This model accepts additional fields of type Any.*

## Structure

`AgentRunGrounding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `citations` | [`List[AgentRunCitation]`](../../doc/models/agent-run-citation.md) | Optional | Citations supporting this field's value. |
| `field` | `str` | Optional | Dot-notation path into the structured output, e.g. "companies.0.ceo". |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run_grounding import AgentRunGrounding

agent_run_grounding = AgentRunGrounding(
    citations=[
        None
    ],
    field='field0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

