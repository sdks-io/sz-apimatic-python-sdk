# Search

Search operations

```python
search_api = client.search
```

## Class Name

`SearchApi`


# Search

```python
def search(self,
          body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SearchRequest`](../../doc/models/search-request.md) | Body, Required | - |

## Response Type

**200**: Search completed. Returns matched documents.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SearchResponse`](../../doc/models/search-response.md).

## Example Usage

```python
body = SearchRequest(
    query='How much is the fish?'
)

result = search_api.search(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Missing or malformed request fields. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 401 | Invalid or missing API key. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 402 | Insufficient credits. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 404 | Endpoint not found, or a scope that matches nothing. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 405 | Wrong method for this endpoint. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 413 | Request body is too large. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 429 | Rate limit exceeded. Wait before retrying. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

