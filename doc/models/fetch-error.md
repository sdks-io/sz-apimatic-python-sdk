
# Fetch Error

Why one URL failed.

*This model accepts additional fields of type Any.*

## Structure

`FetchError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | A stable, machine-readable reason. A client must treat an unrecognized<br>code as a generic failure rather than rejecting the result.<br><br>Documented codes:<br><br>"invalid_url"              -- not a parseable absolute URL.<br>"unsupported_scheme"       -- parseable, but not `http` or `https`.<br>"url_not_accessible"       -- DNS, connection, TLS, or navigation<br>failure reaching the origin, or a host<br>this service does not fetch.<br>"timeout"                  -- the fetch did not finish within<br>`timeout_ms`.<br>"unsupported_content_type" -- the document is not an HTML page. PDFs,<br>images, archives, and other binaries are<br>out of scope. Refused from the URL before<br>the fetch, or from the media type the<br>origin declared after it.<br>"extraction_failed"        -- the page was fetched, but no requested<br>format could be produced from it.<br>"upstream_error"           -- the fetch path itself failed. Ours, not<br>the URL's. |
| `message` | `str` | Optional | A human-readable explanation. Always set when this message is present:<br>`FetchError` itself is optional on the result, so an absent error is<br>absent whole, and there is no state where a failure arrives without a<br>reason. For operators and logs. Never parse it -- branch on `code`. The<br>wording of any given message may change at any time. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.fetch_error import FetchError

fetch_error = FetchError(
    code='code6',
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

