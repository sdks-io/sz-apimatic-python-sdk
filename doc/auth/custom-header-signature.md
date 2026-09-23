
# Custom Header Signature



Documentation for accessing and setting credentials for ApiKeyAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| x-api-key | `str` | Seltz API key. Create one in the [Seltz Console](https://console.seltz.ai/api-keys) under **Settings → API Keys**. | `x_api_key` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from seltzapi.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
from seltzapi.seltzapi_client import SeltzapiClient

client = SeltzapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        x_api_key='x-api-key'
    )
)
```


