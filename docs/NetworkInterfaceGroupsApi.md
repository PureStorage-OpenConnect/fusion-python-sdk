# fusion.NetworkInterfaceGroupsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_interface_group**](NetworkInterfaceGroupsApi.md#create_network_interface_group) | **POST** /regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups | (Provider) Creates a Network Interface Group.
[**delete_network_interface_group**](NetworkInterfaceGroupsApi.md#delete_network_interface_group) | **DELETE** /regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name} | (Provider) Deletes a specific Network Interface Group.
[**get_network_interface_group**](NetworkInterfaceGroupsApi.md#get_network_interface_group) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name} | (Provider) Gets a specific Network Interface Group.
[**get_network_interface_group_by_id**](NetworkInterfaceGroupsApi.md#get_network_interface_group_by_id) | **GET** /resources/network-interface-groups/{network_interface_group_id} | (Provider) Gets a specific Network Interface Group.
[**list_network_interface_groups**](NetworkInterfaceGroupsApi.md#list_network_interface_groups) | **GET** /regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups | (Provider) Gets a list of all Network Interface Groups.
[**update_network_interface_group**](NetworkInterfaceGroupsApi.md#update_network_interface_group) | **PATCH** /regions/{region_name}/availability-zones/{availability_zone_name}/network-interface-groups/{network_interface_group_name} | (Provider) Updates a Network Interface Group.

# **create_network_interface_group**
> Operation create_network_interface_group(body, region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Creates a Network Interface Group.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
body = fusion.NetworkInterfaceGroupPost() # NetworkInterfaceGroupPost | 
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Creates a Network Interface Group.
    api_response = api_instance.create_network_interface_group(body, region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->create_network_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkInterfaceGroupPost**](NetworkInterfaceGroupPost.md)|  | 
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

# **delete_network_interface_group**
> Operation delete_network_interface_group(region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Deletes a specific Network Interface Group.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
network_interface_group_name = 'network_interface_group_name_example' # str | (Provider) The Network Interface Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Deletes a specific Network Interface Group.
    api_response = api_instance.delete_network_interface_group(region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->delete_network_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **network_interface_group_name** | **str**| (Provider) The Network Interface Group name | 
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

# **get_network_interface_group**
> NetworkInterfaceGroup get_network_interface_group(region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Network Interface Group.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
network_interface_group_name = 'network_interface_group_name_example' # str | (Provider) The Network Interface Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Network Interface Group.
    api_response = api_instance.get_network_interface_group(region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->get_network_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **network_interface_group_name** | **str**| (Provider) The Network Interface Group name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**NetworkInterfaceGroup**](NetworkInterfaceGroup.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interface_group_by_id**
> NetworkInterfaceGroup get_network_interface_group_by_id(network_interface_group_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a specific Network Interface Group.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
network_interface_group_id = 'network_interface_group_id_example' # str | (Provider) The Network Interface Group ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a specific Network Interface Group.
    api_response = api_instance.get_network_interface_group_by_id(network_interface_group_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->get_network_interface_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_interface_group_id** | **str**| (Provider) The Network Interface Group ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**NetworkInterfaceGroup**](NetworkInterfaceGroup.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_interface_groups**
> NetworkInterfaceGroupList list_network_interface_groups(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets a list of all Network Interface Groups.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets a list of all Network Interface Groups.
    api_response = api_instance.list_network_interface_groups(region_name, availability_zone_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->list_network_interface_groups: %s\n" % e)
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

[**NetworkInterfaceGroupList**](NetworkInterfaceGroupList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_interface_group**
> Operation update_network_interface_group(body, region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Updates a Network Interface Group.

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
api_instance = fusion.NetworkInterfaceGroupsApi(fusion.ApiClient(configuration))
body = fusion.NetworkInterfaceGroupPatch() # NetworkInterfaceGroupPatch | 
region_name = 'region_name_example' # str | The Region name
availability_zone_name = 'availability_zone_name_example' # str | The Availability Zone name
network_interface_group_name = 'network_interface_group_name_example' # str | (Provider) The Network Interface Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Updates a Network Interface Group.
    api_response = api_instance.update_network_interface_group(body, region_name, availability_zone_name, network_interface_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfaceGroupsApi->update_network_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkInterfaceGroupPatch**](NetworkInterfaceGroupPatch.md)|  | 
 **region_name** | **str**| The Region name | 
 **availability_zone_name** | **str**| The Availability Zone name | 
 **network_interface_group_name** | **str**| (Provider) The Network Interface Group name | 
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

