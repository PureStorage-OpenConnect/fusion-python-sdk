# fusion.AvailabilityZonesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_availability_zone**](AvailabilityZonesApi.md#create_availability_zone) | **POST** /regions/{region_name}/availability-zones | Creates an Availability Zone.
[**delete_availability_zone**](AvailabilityZonesApi.md#delete_availability_zone) | **DELETE** /regions/{region_name}/availability-zones/{availability_zone_name} | Deletes a specific Availability Zone.
[**get_availability_zone**](AvailabilityZonesApi.md#get_availability_zone) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name} | Gets a specific Availability Zone.
[**get_availability_zone_by_id**](AvailabilityZonesApi.md#get_availability_zone_by_id) | **GET** /resources/availability-zones/{availability_zone_id} | Gets a specific Availability Zone.
[**get_availability_zone_performance**](AvailabilityZonesApi.md#get_availability_zone_performance) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/performance | (Provider) Gets performance metrics of a specific Availability Zone.
[**get_availability_zone_space**](AvailabilityZonesApi.md#get_availability_zone_space) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/space | (Provider) Gets space metrics of a specific Availability Zone.
[**list_availability_zones**](AvailabilityZonesApi.md#list_availability_zones) | **GET** /regions/{region_name}/availability-zones | Gets a list of all Availability Zones.

# **create_availability_zone**
> Operation create_availability_zone(body, region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates an Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
body = fusion.AvailabilityZonePost() # AvailabilityZonePost | 
region_name = 'region_name_example' # str | The Region name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates an Availability Zone.
    api_response = api_instance.create_availability_zone(body, region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->create_availability_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AvailabilityZonePost**](AvailabilityZonePost.md)|  | 
 **region_name** | **str**| The Region name | 
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

# **delete_availability_zone**
> Operation delete_availability_zone(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Deletes a specific Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Deletes a specific Availability Zone.
    api_response = api_instance.delete_availability_zone(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->delete_availability_zone: %s\n" % e)
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

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_zone**
> AvailabilityZone get_availability_zone(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Availability Zone.
    api_response = api_instance.get_availability_zone(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->get_availability_zone: %s\n" % e)
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

[**AvailabilityZone**](AvailabilityZone.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_zone_by_id**
> AvailabilityZone get_availability_zone_by_id(availability_zone_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
availability_zone_id = 'availability_zone_id_example' # str | The Availability Zone ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Availability Zone.
    api_response = api_instance.get_availability_zone_by_id(availability_zone_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->get_availability_zone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **availability_zone_id** | **str**| The Availability Zone ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**AvailabilityZone**](AvailabilityZone.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_zone_performance**
> Performance get_availability_zone_performance(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets performance metrics of a specific Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets performance metrics of a specific Availability Zone.
    api_response = api_instance.get_availability_zone_performance(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->get_availability_zone_performance: %s\n" % e)
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

[**Performance**](Performance.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_zone_space**
> Space get_availability_zone_space(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets space metrics of a specific Availability Zone.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets space metrics of a specific Availability Zone.
    api_response = api_instance.get_availability_zone_space(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->get_availability_zone_space: %s\n" % e)
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

[**Space**](Space.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_availability_zones**
> AvailabilityZoneList list_availability_zones(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a list of all Availability Zones.

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
api_instance = fusion.AvailabilityZonesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a list of all Availability Zones.
    api_response = api_instance.list_availability_zones(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityZonesApi->list_availability_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**AvailabilityZoneList**](AvailabilityZoneList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

