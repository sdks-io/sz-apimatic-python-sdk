# Fetch

Fetch operations

```python
fetch_api = client.fetch
```

## Class Name

`FetchApi`


# Fetch

```python
def fetch(self,
         body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchRequest`](../../doc/models/fetch-request.md) | Body, Required | - |

## Response Type

**200**: One result per requested URL. A failure to fetch a page is still a 200, with that result's `status = "error"`.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FetchResponse`](../../doc/models/fetch-response.md).

## Example Usage

```python
body = FetchRequest(
    urls=[
        'https://example.com/'
    ]
)

result = fetch_api.fetch(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Malformed body, an out-of-bounds or duplicated `urls` entry, or an unavailable `formats` or `tier` value. Unrecognized fields are ignored. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 402 | Insufficient credits. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 429 | Rate limited. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

