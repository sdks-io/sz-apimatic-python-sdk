
# List Runs Response

*This model accepts additional fields of type Any.*

## Structure

`ListRunsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more` | `bool` | Optional | True when limit cut the page short.<br><br>**Default**: `False` |
| `runs` | [`List[Run]`](../../doc/models/run.md) | Optional | Newest first by default, so \[0\] is the latest run. Page back with<br>before = runs\[last\].run_id; pass sort = SORT_ORDER_ASC to walk forward<br>instead, and page with since = runs\[last\].run_id. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.list_runs_response import ListRunsResponse

list_runs_response = ListRunsResponse(
    has_more=False,
    runs=[
        None
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

