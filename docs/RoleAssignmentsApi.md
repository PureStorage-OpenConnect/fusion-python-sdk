# fusion.RoleAssignmentsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_assignment**](RoleAssignmentsApi.md#create_role_assignment) | **POST** /roles/{role_name}/role-assignments | Creates a Role Assignment.
[**delete_role_assignment**](RoleAssignmentsApi.md#delete_role_assignment) | **DELETE** /roles/{role_name}/role-assignments/{role_assignment_name} | Delete a Role Assignment.
[**get_role_assignment**](RoleAssignmentsApi.md#get_role_assignment) | **GET** /roles/{role_name}/role-assignments/{role_assignment_name} | Gets a specific Role Assignment.
[**get_role_assignment_by_id**](RoleAssignmentsApi.md#get_role_assignment_by_id) | **GET** /resources/role-assignments/{role_assignment_id} | Gets a specific Role Assignment.
[**list_role_assignments**](RoleAssignmentsApi.md#list_role_assignments) | **GET** /roles/{role_name}/role-assignments | Gets a list of all Role Assignments.
[**list_role_assignments_canonical**](RoleAssignmentsApi.md#list_role_assignments_canonical) | **GET** /resources/role-assignments | Gets a list of all Role Assignments.

# **create_role_assignment**
> Operation create_role_assignment(body, role_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Role Assignment.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
body = fusion.RoleAssignmentPost() # RoleAssignmentPost | 
role_name = 'role_name_example' # str | The Role name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Role Assignment.
    api_response = api_instance.create_role_assignment(body, role_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->create_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleAssignmentPost**](RoleAssignmentPost.md)|  | 
 **role_name** | **str**| The Role name | 
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

# **delete_role_assignment**
> Operation delete_role_assignment(role_name, role_assignment_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Delete a Role Assignment.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
role_name = 'role_name_example' # str | The Role name
role_assignment_name = 'role_assignment_name_example' # str | The Role Assignment name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Delete a Role Assignment.
    api_response = api_instance.delete_role_assignment(role_name, role_assignment_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->delete_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The Role name | 
 **role_assignment_name** | **str**| The Role Assignment name | 
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

# **get_role_assignment**
> RoleAssignment get_role_assignment(role_name, role_assignment_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Role Assignment.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
role_name = 'role_name_example' # str | The Role name
role_assignment_name = 'role_assignment_name_example' # str | The Role Assignment name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Role Assignment.
    api_response = api_instance.get_role_assignment(role_name, role_assignment_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_role_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The Role name | 
 **role_assignment_name** | **str**| The Role Assignment name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_assignment_by_id**
> RoleAssignment get_role_assignment_by_id(role_assignment_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Role Assignment.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
role_assignment_id = 'role_assignment_id_example' # str | The Role Assignment ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Role Assignment.
    api_response = api_instance.get_role_assignment_by_id(role_assignment_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->get_role_assignment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_assignment_id** | **str**| The Role Assignment ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_assignments**
> list[RoleAssignment] list_role_assignments(role_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, scope=scope, principal=principal)

Gets a list of all Role Assignments.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
role_name = 'role_name_example' # str | The Role name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)
scope = 'scope_example' # str |  (optional)
principal = 'principal_example' # str |  (optional)

try:
    # Gets a list of all Role Assignments.
    api_response = api_instance.list_role_assignments(role_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, scope=scope, principal=principal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->list_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| The Role name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 
 **scope** | **str**|  | [optional] 
 **principal** | **str**|  | [optional] 

### Return type

[**list[RoleAssignment]**](RoleAssignment.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_assignments_canonical**
> list[RoleAssignment] list_role_assignments_canonical(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, scope=scope, principal=principal, role=role)

Gets a list of all Role Assignments.

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
api_instance = fusion.RoleAssignmentsApi(fusion.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)
scope = 'scope_example' # str |  (optional)
principal = 'principal_example' # str |  (optional)
role = 'role_example' # str |  (optional)

try:
    # Gets a list of all Role Assignments.
    api_response = api_instance.list_role_assignments_canonical(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, scope=scope, principal=principal, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleAssignmentsApi->list_role_assignments_canonical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 
 **scope** | **str**|  | [optional] 
 **principal** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 

### Return type

[**list[RoleAssignment]**](RoleAssignment.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

