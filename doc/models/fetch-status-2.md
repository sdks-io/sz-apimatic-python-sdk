
# Fetch Status 2

Whether this result carries content.

Branch on this field, never on whether a given content field is present: a
format the page could not produce is unset on an otherwise successful
result, so "markdown is absent" does not mean "the fetch failed".

A failed fetch is still HTTP 200, with the error status on the result.

## Enumeration

`FetchStatus2`

## Fields

| Name |
|  --- |
| `OK` |
| `ERROR` |

## Example

```python
from seltzapi.models.fetch_status_2 import FetchStatus2

fetch_status_2 = FetchStatus2.OK
```

