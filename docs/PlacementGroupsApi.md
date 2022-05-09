# fusion.PlacementGroupsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_placement_group**](PlacementGroupsApi.md#create_placement_group) | **POST** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups | Creates a Placement Group.
[**delete_placement_group**](PlacementGroupsApi.md#delete_placement_group) | **DELETE** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name} | Deletes a specific Placement Group.
[**get_placement_group**](PlacementGroupsApi.md#get_placement_group) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name} | Gets a specific Placement Group.
[**get_placement_group_by_id**](PlacementGroupsApi.md#get_placement_group_by_id) | **GET** /resources/placement-groups/{placement_group_id} | Gets a specific Placement Group.
[**get_placement_group_sessions**](PlacementGroupsApi.md#get_placement_group_sessions) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/sessions | Gets iSCSI sessions data of a specific Placement Group.
[**get_placement_groups_performance**](PlacementGroupsApi.md#get_placement_groups_performance) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/performance | Get performance metrics of a specific Placement Group
[**get_placement_groups_space**](PlacementGroupsApi.md#get_placement_groups_space) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name}/space | Get space metrics of a specific Placement Group
[**list_placement_groups**](PlacementGroupsApi.md#list_placement_groups) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups | Gets a list of all Placement Groups.
[**query_placement_groups**](PlacementGroupsApi.md#query_placement_groups) | **GET** /resources/placement-groups | Returns a list of Placement Groups from query
[**update_placement_group**](PlacementGroupsApi.md#update_placement_group) | **PATCH** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/placement-groups/{placement_group_name} | Updates a specific Placement Group.

# **create_placement_group**
> Operation create_placement_group(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
body = fusion.PlacementGroupPost() # PlacementGroupPost | 
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Placement Group.
    api_response = api_instance.create_placement_group(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->create_placement_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlacementGroupPost**](PlacementGroupPost.md)|  | 
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
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

# **delete_placement_group**
> Operation delete_placement_group(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Deletes a specific Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Deletes a specific Placement Group.
    api_response = api_instance.delete_placement_group(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->delete_placement_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
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

# **get_placement_group**
> PlacementGroup get_placement_group(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Placement Group.
    api_response = api_instance.get_placement_group(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->get_placement_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_group_by_id**
> PlacementGroup get_placement_group_by_id(placement_group_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
placement_group_id = 'placement_group_id_example' # str | The Placement Group ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Placement Group.
    api_response = api_instance.get_placement_group_by_id(placement_group_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->get_placement_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_group_id** | **str**| The Placement Group ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_group_sessions**
> SessionList get_placement_group_sessions(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets iSCSI sessions data of a specific Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets iSCSI sessions data of a specific Placement Group.
    api_response = api_instance.get_placement_group_sessions(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->get_placement_group_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**SessionList**](SessionList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_groups_performance**
> Performance get_placement_groups_performance(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Get performance metrics of a specific Placement Group

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Get performance metrics of a specific Placement Group
    api_response = api_instance.get_placement_groups_performance(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->get_placement_groups_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
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

# **get_placement_groups_space**
> Space get_placement_groups_space(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Get space metrics of a specific Placement Group

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Get space metrics of a specific Placement Group
    api_response = api_instance.get_placement_groups_space(tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->get_placement_groups_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
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

# **list_placement_groups**
> PlacementGroupList list_placement_groups(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a list of all Placement Groups.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a list of all Placement Groups.
    api_response = api_instance.list_placement_groups(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->list_placement_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**PlacementGroupList**](PlacementGroupList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_placement_groups**
> PlacementGroupList query_placement_groups(region_name, availability_zone_name, array_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Returns a list of Placement Groups from query

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | Region that array belongs to.
availability_zone_name = 'availability_zone_name_example' # str | Availability zone that array belongs to.
array_name = 'array_name_example' # str | Return placement-groups across all tenant spaces that are located on the array.
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Returns a list of Placement Groups from query
    api_response = api_instance.query_placement_groups(region_name, availability_zone_name, array_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->query_placement_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| Region that array belongs to. | 
 **availability_zone_name** | **str**| Availability zone that array belongs to. | 
 **array_name** | **str**| Return placement-groups across all tenant spaces that are located on the array. | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**PlacementGroupList**](PlacementGroupList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_placement_group**
> Operation update_placement_group(body, tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Updates a specific Placement Group.

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
api_instance = fusion.PlacementGroupsApi(fusion.ApiClient(configuration))
body = fusion.PlacementGroupPatch() # PlacementGroupPatch | 
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
placement_group_name = 'placement_group_name_example' # str | The Placement Group name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Updates a specific Placement Group.
    api_response = api_instance.update_placement_group(body, tenant_name, tenant_space_name, placement_group_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementGroupsApi->update_placement_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlacementGroupPatch**](PlacementGroupPatch.md)|  | 
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **placement_group_name** | **str**| The Placement Group name | 
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

