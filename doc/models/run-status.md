
# Run Status

A run's outcome.

`completed` -- every request succeeded. `partial` -- at least one request
failed after retries and at least one succeeded. `failed` -- no request
succeeded, and no records. `skipped` -- not attempted and not billed; see
`status_reason`. Any of them may produce no records.

## Enumeration

`RunStatus`

## Fields

| Name |
|  --- |
| `COMPLETED` |
| `PARTIAL` |
| `FAILED` |
| `SKIPPED` |

## Example

```python
from seltzapi.models.run_status import RunStatus

run_status = RunStatus.COMPLETED
```

