# fusion.WorkloadPlannerApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_placement_recommendation**](WorkloadPlannerApi.md#create_placement_recommendation) | **POST** /workload-planner/placement-recommendations | (Provider) Generates a report on the candidate arrays a given placement group can be placed/migrated to
[**get_placement_recommendation**](WorkloadPlannerApi.md#get_placement_recommendation) | **GET** /workload-planner/placement-recommendations/{placement_recommendation_name} | Gets a specific placement recommendation report

# **create_placement_recommendation**
> Operation create_placement_recommendation(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Generates a report on the candidate arrays a given placement group can be placed/migrated to

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
api_instance = fusion.WorkloadPlannerApi(fusion.ApiClient(configuration))
body = fusion.PlacementRecommendationPost() # PlacementRecommendationPost | 
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Generates a report on the candidate arrays a given placement group can be placed/migrated to
    api_response = api_instance.create_placement_recommendation(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadPlannerApi->create_placement_recommendation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlacementRecommendationPost**](PlacementRecommendationPost.md)|  | 
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

# **get_placement_recommendation**
> PlacementRecommendation get_placement_recommendation(placement_recommendation_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific placement recommendation report

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
api_instance = fusion.WorkloadPlannerApi(fusion.ApiClient(configuration))
placement_recommendation_name = 'placement_recommendation_name_example' # str | Name of Placement Recommendation report
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific placement recommendation report
    api_response = api_instance.get_placement_recommendation(placement_recommendation_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadPlannerApi->get_placement_recommendation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_recommendation_name** | **str**| Name of Placement Recommendation report | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**PlacementRecommendation**](PlacementRecommendation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

