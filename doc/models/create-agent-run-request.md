
# Create Agent Run Request

## Structure

`CreateAgentRunRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Optional | The API key, on gRPC requests. REST reads the `x-api-key` header instead. |
| `effort` | `str` | Optional | Effort level: how much research the run may do, and its price. One of<br>the configured level names (e.g. `low`, `medium`, `high`, `max`).<br>Omitted = the default level. |
| `output_schema` | `Any` | Optional | Optional OpenAI-style `response_format` object requesting structured<br>output: `{"type": "text" \| "json_object" \| "json_schema", ...}`, with<br>`name` / `schema` / `strict` for type `json_schema`. A structured type<br>adds `output.structured` and its `grounding` alongside the cited text;<br>type `text` is accepted and requests no structure. On gRPC the object is<br>JSON-encoded. |
| `query` | `str` | Optional | The natural-language question. Instructions inside the query are<br>followed. |

## Example

```python
import jsonpickle

from seltzapi.models.create_agent_run_request import CreateAgentRunRequest

create_agent_run_request = CreateAgentRunRequest(
    api_key='api_key8',
    effort='effort4',
    output_schema=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    query='query4'
)
```

