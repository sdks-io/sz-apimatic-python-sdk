
# Agent Run Source

One source a run cited.

*This model accepts additional fields of type Any.*

## Structure

`AgentRunSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Identifier within the run, cited as `\[id\]` in `text` and as `source_id`<br>in `grounding`.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `url` | `str` | Optional | URL of the source document. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run_source import AgentRunSource

agent_run_source = AgentRunSource(
    id=0,
    url='url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

