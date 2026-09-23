
# Getting Started with Seltz API

## Introduction

REST API for the Seltz platform: context retrieval (`/v1/search`), RAG answers (`/v1/answer`), monitors (`/v1/monitors`), and page fetching (`/v1/fetch`).

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install stz-apimatic-sdk==0.0.2
```

You can also view the package at:
https://pypi.python.org/pypi/stz-apimatic-sdk/0.0.2

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| custom_header_authentication_credentials | [`CustomHeaderAuthenticationCredentials`](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
import logging

from seltzapi.configuration import Environment
from seltzapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from seltzapi.logging.configuration.api_logging_configuration import LoggingConfiguration
from seltzapi.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from seltzapi.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from seltzapi.seltzapi_client import SeltzapiClient

client = SeltzapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='x-api-key'
    ),
    environment=Environment.PRODUCTION,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

### Environment-Based Client Initialization

```python
from seltzapi.seltzapi_client import SeltzapiClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = SeltzapiClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/environment-based-client-initialization.md) section for details.

## Authorization

This API uses the following authentication schemes.

* [`ApiKeyAuth (Custom Header Signature)`](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/auth/custom-header-signature.md)

## List of APIs

* [Search](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/search.md)
* [Answer](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/answer.md)
* [Monitors](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/monitors.md)
* [Records](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/records.md)
* [Runs](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/runs.md)
* [Agent](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/agent.md)
* [Fetch](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/controllers/fetch.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/environment-based-client-initialization.md)
* [AbstractLogger](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/http-request.md)

### Utilities

* [ApiResponse](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/api-response.md)
* [ApiHelper](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/sdks-io/sz-apimatic-python-sdk/tree/0.0.2/doc/unix-date-time.md)

