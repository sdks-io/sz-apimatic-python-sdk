
# Agent Run Citation

One citation supporting a grounded field.

*This model accepts additional fields of type Any.*

## Structure

`AgentRunCitation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_id` | `int` | Optional | `id` of the entry in `sources` this citation points at.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `url` | `str` | Optional | URL of the cited document. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.agent_run_citation import AgentRunCitation

agent_run_citation = AgentRunCitation(
    source_id=0,
    url='url2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

