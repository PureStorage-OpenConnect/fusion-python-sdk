# fusion.StorageEndpointsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storage_endpoint**](StorageEndpointsApi.md#create_storage_endpoint) | **POST** /regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints | (Provider) Creates a Storage Endpoint.
[**delete_storage_endpoint**](StorageEndpointsApi.md#delete_storage_endpoint) | **DELETE** /regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name} | (Provider) Deletes a specific Storage Endpoint.
[**get_storage_endpoint**](StorageEndpointsApi.md#get_storage_endpoint) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name} | (Provider) Gets a specific Storage Endpoint.
[**get_storage_endpoint_by_id**](StorageEndpointsApi.md#get_storage_endpoint_by_id) | **GET** /resources/storage-endpoints/{storage_endpoint_id} | (Provider) Gets a specific Storage Endpoint.
[**list_storage_endpoints**](StorageEndpointsApi.md#list_storage_endpoints) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints | (Provider) Gets a list of all Storage Endpoints.
[**update_storage_endpoint**](StorageEndpointsApi.md#update_storage_endpoint) | **PATCH** /regions/{region_name}/availability-zones/{availability_zone_name}/storage-endpoints/{storage_endpoint_name} | (Provider) Updates a Storage Endpoint.

# **create_storage_endpoint**
> Operation create_storage_endpoint(body, region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Creates a Storage Endpoint.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
body = fusion.StorageEndpointPost() # StorageEndpointPost | 
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Creates a Storage Endpoint.
    api_response = api_instance.create_storage_endpoint(body, region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->create_storage_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageEndpointPost**](StorageEndpointPost.md)|  | 
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_endpoint**
> Operation delete_storage_endpoint(region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Deletes a specific Storage Endpoint.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
storage_endpoint_name = 'storage_endpoint_name_example' # str | (Provider) The Storage Endpoint name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Deletes a specific Storage Endpoint.
    api_response = api_instance.delete_storage_endpoint(region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->delete_storage_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **storage_endpoint_name** | **str**| (Provider) The Storage Endpoint name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_endpoint**
> StorageEndpoint get_storage_endpoint(region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Storage Endpoint.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
storage_endpoint_name = 'storage_endpoint_name_example' # str | (Provider) The Storage Endpoint name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Storage Endpoint.
    api_response = api_instance.get_storage_endpoint(region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->get_storage_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **storage_endpoint_name** | **str**| (Provider) The Storage Endpoint name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**StorageEndpoint**](StorageEndpoint.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_endpoint_by_id**
> StorageEndpoint get_storage_endpoint_by_id(storage_endpoint_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Storage Endpoint.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
storage_endpoint_id = 'storage_endpoint_id_example' # str | (Provider) The Storage Endpoint ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Storage Endpoint.
    api_response = api_instance.get_storage_endpoint_by_id(storage_endpoint_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->get_storage_endpoint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_endpoint_id** | **str**| (Provider) The Storage Endpoint ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**StorageEndpoint**](StorageEndpoint.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storage_endpoints**
> StorageEndpointList list_storage_endpoints(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a list of all Storage Endpoints.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a list of all Storage Endpoints.
    api_response = api_instance.list_storage_endpoints(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->list_storage_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**StorageEndpointList**](StorageEndpointList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_endpoint**
> Operation update_storage_endpoint(body, region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Updates a Storage Endpoint.

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
api_instance = fusion.StorageEndpointsApi(fusion.ApiClient(configuration))
body = fusion.StorageEndpointPatch() # StorageEndpointPatch | 
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
storage_endpoint_name = 'storage_endpoint_name_example' # str | (Provider) The Storage Endpoint name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Updates a Storage Endpoint.
    api_response = api_instance.update_storage_endpoint(body, region_name, availability_zone_name, storage_endpoint_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageEndpointsApi->update_storage_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageEndpointPatch**](StorageEndpointPatch.md)|  | 
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **storage_endpoint_name** | **str**| (Provider) The Storage Endpoint name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

