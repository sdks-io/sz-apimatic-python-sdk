
# Answer Http Response

Buffered JSON response body for `POST /v1/answer`.

*This model accepts additional fields of type Any.*

## Structure

`AnswerHttpResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `answer` | `str` | Required | Markdown answer text. Inline citations follow the form<br>`text ([Source Name](url))`. |
| `citations` | [`List[HttpCitation]`](../../doc/models/http-citation.md) | Required | The sources the answer was grounded in. Every source the answer was<br>given is returned, whether or not the text cites it. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from seltzapi.models.answer_http_response import AnswerHttpResponse
from seltzapi.models.http_citation import HttpCitation

answer_http_response = AnswerHttpResponse(
    answer='answer6',
    citations=[
        HttpCitation(
            url='url2',
            content='content2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

