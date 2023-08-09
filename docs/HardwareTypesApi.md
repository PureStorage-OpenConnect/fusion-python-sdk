# fusion.HardwareTypesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hardware_type**](HardwareTypesApi.md#get_hardware_type) | **GET** /hardware-types/{hardware_type_name} | (Provider) Gets a specific Hardware Type.
[**get_hardware_type_by_id**](HardwareTypesApi.md#get_hardware_type_by_id) | **GET** /resources/hardware-types/{hardware_type_id} | (Provider) Gets a specific Hardware Type.
[**list_hardware_types**](HardwareTypesApi.md#list_hardware_types) | **GET** /hardware-types | (Provider) Gets a list of all hardware types.

# **get_hardware_type**
> HardwareType get_hardware_type(hardware_type_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Hardware Type.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.HardwareTypesApi(fusion.ApiClient(configuration))
hardware_type_name = 'hardware_type_name_example' # str | (Provider) The Hardware Type name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Hardware Type.
    api_response = api_instance.get_hardware_type(hardware_type_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareTypesApi->get_hardware_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_type_name** | **str**| (Provider) The Hardware Type name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**HardwareType**](HardwareType.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_type_by_id**
> HardwareType get_hardware_type_by_id(hardware_type_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Hardware Type.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.HardwareTypesApi(fusion.ApiClient(configuration))
hardware_type_id = 'hardware_type_id_example' # str | (Provider) The Hardware Type ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Hardware Type.
    api_response = api_instance.get_hardware_type_by_id(hardware_type_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareTypesApi->get_hardware_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_type_id** | **str**| (Provider) The Hardware Type ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**HardwareType**](HardwareType.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hardware_types**
> HardwareTypeList list_hardware_types(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, media_type=media_type, array_type=array_type)

(Provider) Gets a list of all hardware types.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.HardwareTypesApi(fusion.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)
media_type = 'media_type_example' # str | Return only hardware types matching the given media type (optional)
array_type = 'array_type_example' # str | Return only hardware types matching the given array type (optional)

try:
    # (Provider) Gets a list of all hardware types.
    api_response = api_instance.list_hardware_types(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, media_type=media_type, array_type=array_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareTypesApi->list_hardware_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 
 **media_type** | **str**| Return only hardware types matching the given media type | [optional] 
 **array_type** | **str**| Return only hardware types matching the given array type | [optional] 

### Return type

[**HardwareTypeList**](HardwareTypeList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

