# fusion.TenantSpacesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant_space**](TenantSpacesApi.md#create_tenant_space) | **POST** /tenants/{tenant_name}/tenant-spaces | Creates a Tenant Space.
[**delete_tenant_space**](TenantSpacesApi.md#delete_tenant_space) | **DELETE** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name} | Deletes a specific Tenant Space.
[**get_tenant_space**](TenantSpacesApi.md#get_tenant_space) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name} | Gets a specific Tenant Space.
[**get_tenant_space_by_id**](TenantSpacesApi.md#get_tenant_space_by_id) | **GET** /resources/tenant-spaces/{tenant_space_id} | Gets a specific Tenant Space.
[**get_tenant_space_performance**](TenantSpacesApi.md#get_tenant_space_performance) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/performance | Gets performance metrics of a specific Tenant Space.
[**get_tenant_space_space**](TenantSpacesApi.md#get_tenant_space_space) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/space | Gets space metrics of a specific Tenant Space.
[**list_tenant_spaces**](TenantSpacesApi.md#list_tenant_spaces) | **GET** /tenants/{tenant_name}/tenant-spaces | Gets a list of all Tenant Spaces.
[**query_tenant_spaces**](TenantSpacesApi.md#query_tenant_spaces) | **GET** /resources/tenant-spaces | (Opt-in) Get all Tenant Spaces in the org. Provide a filter to search for specific Tenant Spaces
[**update_tenant_space**](TenantSpacesApi.md#update_tenant_space) | **PATCH** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name} | Updates a Tenant Space.

# **create_tenant_space**
> Operation create_tenant_space(body, tenant_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
body = fusion.TenantSpacePost() # TenantSpacePost | 
tenant_name = 'tenant_name_example' # str | The Tenant name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Tenant Space.
    api_response = api_instance.create_tenant_space(body, tenant_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->create_tenant_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantSpacePost**](TenantSpacePost.md)|  | 
 **tenant_name** | **str**| The Tenant name | 
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

# **delete_tenant_space**
> Operation delete_tenant_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Deletes a specific Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Deletes a specific Tenant Space.
    api_response = api_instance.delete_tenant_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->delete_tenant_space: %s\n" % e)
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

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_space**
> TenantSpace get_tenant_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Tenant Space.
    api_response = api_instance.get_tenant_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->get_tenant_space: %s\n" % e)
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

[**TenantSpace**](TenantSpace.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_space_by_id**
> TenantSpace get_tenant_space_by_id(tenant_space_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_space_id = 'tenant_space_id_example' # str | The Tenant Space ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Tenant Space.
    api_response = api_instance.get_tenant_space_by_id(tenant_space_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->get_tenant_space_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_space_id** | **str**| The Tenant Space ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**TenantSpace**](TenantSpace.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_space_performance**
> Performance get_tenant_space_performance(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets performance metrics of a specific Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets performance metrics of a specific Tenant Space.
    api_response = api_instance.get_tenant_space_performance(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->get_tenant_space_performance: %s\n" % e)
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

[**Performance**](Performance.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_space_space**
> Space get_tenant_space_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets space metrics of a specific Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets space metrics of a specific Tenant Space.
    api_response = api_instance.get_tenant_space_space(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->get_tenant_space_space: %s\n" % e)
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

[**Space**](Space.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenant_spaces**
> TenantSpaceList list_tenant_spaces(tenant_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a list of all Tenant Spaces.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a list of all Tenant Spaces.
    api_response = api_instance.list_tenant_spaces(tenant_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->list_tenant_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**TenantSpaceList**](TenantSpaceList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tenant_spaces**
> TenantSpaceList query_tenant_spaces(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, tenant_id=tenant_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Opt-in) Get all Tenant Spaces in the org. Provide a filter to search for specific Tenant Spaces

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
filter = 'filter_example' # str | filter should use expression language for filtering (optional)
sort = 'sort_example' # str | Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\") (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
display_name = 'display_name_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Opt-in) Get all Tenant Spaces in the org. Provide a filter to search for specific Tenant Spaces
    api_response = api_instance.query_tenant_spaces(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, tenant_id=tenant_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->query_tenant_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| filter should use expression language for filtering | [optional] 
 **sort** | **str**| Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \&quot;sort&#x3D;size-,name\&quot;) | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**TenantSpaceList**](TenantSpaceList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_space**
> Operation update_tenant_space(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Updates a Tenant Space.

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
api_instance = fusion.TenantSpacesApi(fusion.ApiClient(configuration))
body = fusion.TenantSpacePatch() # TenantSpacePatch | 
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Updates a Tenant Space.
    api_response = api_instance.update_tenant_space(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSpacesApi->update_tenant_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantSpacePatch**](TenantSpacePatch.md)|  | 
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

