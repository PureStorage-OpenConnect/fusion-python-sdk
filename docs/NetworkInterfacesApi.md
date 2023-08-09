# fusion.NetworkInterfacesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_interface**](NetworkInterfacesApi.md#get_network_interface) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces/{net_intf_name} | (Provider) Gets a specific Network Interface.
[**get_network_interface_by_id**](NetworkInterfacesApi.md#get_network_interface_by_id) | **GET** /resources/network-interfaces/{network_interface_id} | (Provider) Gets a specific Network Interface.
[**list_network_interfaces**](NetworkInterfacesApi.md#list_network_interfaces) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces | (Provider) Gets a list of all Network Interfaces.
[**update_network_interface**](NetworkInterfacesApi.md#update_network_interface) | **PATCH** /regions/{region_name}/availability-zones/{availability_zone_name}/arrays/{array_name}/network-interfaces/{net_intf_name} | (Provider) Updates a Network Interface.

# **get_network_interface**
> NetworkInterface get_network_interface(region_name, availability_zone_name, array_name, net_intf_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Network Interface.

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
api_instance = fusion.NetworkInterfacesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
array_name = 'array_name_example' # str | The Array name
net_intf_name = 'net_intf_name_example' # str | (Provider) The Network Interface name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Network Interface.
    api_response = api_instance.get_network_interface(region_name, availability_zone_name, array_name, net_intf_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->get_network_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **array_name** | **str**| The Array name | 
 **net_intf_name** | **str**| (Provider) The Network Interface name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interface_by_id**
> NetworkInterface get_network_interface_by_id(network_interface_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Network Interface.

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
api_instance = fusion.NetworkInterfacesApi(fusion.ApiClient(configuration))
network_interface_id = 'network_interface_id_example' # str | (Provider) The Network Interface ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Network Interface.
    api_response = api_instance.get_network_interface_by_id(network_interface_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->get_network_interface_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_interface_id** | **str**| (Provider) The Network Interface ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_interfaces**
> NetworkInterfaceList list_network_interfaces(region_name, availability_zone_name, array_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a list of all Network Interfaces.

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
api_instance = fusion.NetworkInterfacesApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
array_name = 'array_name_example' # str | The Array name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a list of all Network Interfaces.
    api_response = api_instance.list_network_interfaces(region_name, availability_zone_name, array_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->list_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **array_name** | **str**| The Array name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**NetworkInterfaceList**](NetworkInterfaceList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_interface**
> Operation update_network_interface(body, region_name, availability_zone_name, array_name, net_intf_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Updates a Network Interface.

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
api_instance = fusion.NetworkInterfacesApi(fusion.ApiClient(configuration))
body = fusion.NetworkInterfacePatch() # NetworkInterfacePatch | 
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
array_name = 'array_name_example' # str | The Array name
net_intf_name = 'net_intf_name_example' # str | (Provider) The Network Interface name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Updates a Network Interface.
    api_response = api_instance.update_network_interface(body, region_name, availability_zone_name, array_name, net_intf_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->update_network_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkInterfacePatch**](NetworkInterfacePatch.md)|  | 
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **array_name** | **str**| The Array name | 
 **net_intf_name** | **str**| (Provider) The Network Interface name | 
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

