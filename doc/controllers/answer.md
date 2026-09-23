# Answer

Answer operations

```python
answer_api = client.answer
```

## Class Name

`AnswerApi`


# Answer

```python
def answer(self,
          body)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AnswerHttpRequest`](../../doc/models/answer-http-request.md) | Body, Required | - |

## Response Type

**200**: Answer for the query. When `stream = false` the body is a JSON `AnswerHttpResponse`; when `stream = true` it is a `text/event-stream` of OpenAI-style chunks.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AnswerHttpResponse`](../../doc/models/answer-http-response.md).

## Example Usage

```python
body = AnswerHttpRequest(
    query='Who is reported to be Apple\'s next CEO?'
)

result = answer_api.answer(body)

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
| 408 | The answer did not complete in time. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 413 | Request body is too large. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 415 | `Content-Type` is not `application/json`. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 429 | Rate limit exceeded. Wait before retrying. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |
| 500 | Unexpected server error. | [`ErrorEnvelopeException`](../../doc/models/error-envelope-exception.md) |

