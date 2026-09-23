
# Agent Run Request

The request a run was created with.

*This model accepts additional fields of type Any.*

## Structure

`AgentRunRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `effort` | `str` | Optional | The effort level the run executes at: the request's `effort`, or the<br>default level when it named none. |
| `output_schema` | `Any` | Optional | The request's `output_schema`, when one was given. On gRPC the object is<br>JSON-encoded. |
| `query` | `str` | Optional | The natural-language question. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run_request import AgentRunRequest

agent_run_request = AgentRunRequest(
    effort='effort8',
    output_schema=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    query='query8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

