
# Agent Run Output 2

The run's output. Its members are unset until the run completes.

*This model accepts additional fields of type Any.*

## Structure

`AgentRunOutput2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grounding` | [`List[AgentRunGrounding]`](../../doc/models/agent-run-grounding.md) | Optional | Per-field citations for `structured`. Empty when there is no structured<br>output. |
| `sources` | [`List[AgentRunSource]`](../../doc/models/agent-run-source.md) | Optional | The sources cited by `text` or `grounding`, numbered in order of first<br>citation. |
| `structured` | `Any` | Optional | Structured result shaped by the request's `output_schema`. Unset when the<br>request had none. Fields that could not be grounded are expected to be<br>null. On gRPC the object is JSON-encoded. |
| `text` | `str` | Optional | Cited markdown report. Inline `\[n\]` markers cite the entry of `sources`<br>whose `id` is `n`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run_output_2 import AgentRunOutput2
from seltzapi.models.agent_run_source import AgentRunSource

agent_run_output_2 = AgentRunOutput2(
    grounding=[
        None
    ],
    sources=[
        None,
        AgentRunSource(),
        AgentRunSource()
    ],
    structured=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    text='text2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

