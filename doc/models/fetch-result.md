
# Fetch Result

The outcome for one URL.

*This model accepts additional fields of type Any.*

## Structure

`FetchResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `str` | Optional | The origin's declared media type for the main document, without<br>parameters.<br><br>Frequently unset, including on results that carry content. Never branch on<br>it: `status` says whether a result carries content. |
| `error` | [`FetchError1`](../../doc/models/fetch-error-1.md) | Optional | - |
| `fetched_at` | `str` | Optional | - |
| `final_url` | `str` | Optional | The URL the content actually came from, after HTTP redirects and any<br>client-side navigation. Equal to `requested_url` when nothing redirected.<br><br>Set on a result whose `status` is ERROR only when the failure happened<br>after the origin answered, such as a page this service could not extract.<br>Unset when the URL was never reached. |
| `http_status_code` | `int` | Optional | The origin's HTTP status code for the main document. Unset when no network<br>response was observed for the navigation.<br><br>An HTTP error status is not a fetch failure: this service renders the<br>origin's error page, so a 404 arrives as an OK result carrying 404. On a<br>result whose `status` is ERROR, this follows `final_url` - set only when<br>the failure happened after the origin answered.<br><br>**Constraints**: `>= 0` |
| `markdown` | `str` | Optional | The page's main content as Markdown, with boilerplate removed. |
| `requested_url` | `str` | Optional | The URL this answers, echoed verbatim from the request -- byte for byte,<br>never normalized, and never the post-redirect URL. This is the correlation<br>key. Where redirects landed is `final_url`. |
| `status` | [`FetchStatus2`](../../doc/models/fetch-status-2.md) | Required | **Default**: `"ok"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.fetch_result import FetchResult
from seltzapi.models.fetch_status_2 import FetchStatus2

fetch_result = FetchResult(
    status=FetchStatus2.OK,
    content_type='content_type2',
    error=None,
    fetched_at='fetched_at8',
    final_url='final_url2',
    http_status_code=106,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

