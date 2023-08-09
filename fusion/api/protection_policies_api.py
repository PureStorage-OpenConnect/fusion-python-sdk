# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fusion.api_client import ApiClient


class ProtectionPoliciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_protection_policy(self, body, **kwargs):  # noqa: E501
        """Creates a Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protection_policy(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProtectionPolicyPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_protection_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_protection_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_protection_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protection_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProtectionPolicyPost body: (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_protection_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_protection_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/protection-policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_protection_policy(self, protection_policy_name, **kwargs):  # noqa: E501
        """Deletes a specific protection policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_protection_policy(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_protection_policy_with_http_info(protection_policy_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_protection_policy_with_http_info(protection_policy_name, **kwargs)  # noqa: E501
            return data

    def delete_protection_policy_with_http_info(self, protection_policy_name, **kwargs):  # noqa: E501
        """Deletes a specific protection policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_protection_policy_with_http_info(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protection_policy_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_protection_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protection_policy_name' is set
        if ('protection_policy_name' not in params or
                params['protection_policy_name'] is None):
            raise ValueError("Missing the required parameter `protection_policy_name` when calling `delete_protection_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protection_policy_name' in params:
            path_params['protection_policy_name'] = params['protection_policy_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/protection-policies/{protection_policy_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_protection_policy(self, protection_policy_name, **kwargs):  # noqa: E501
        """Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_protection_policy_with_http_info(protection_policy_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_protection_policy_with_http_info(protection_policy_name, **kwargs)  # noqa: E501
            return data

    def get_protection_policy_with_http_info(self, protection_policy_name, **kwargs):  # noqa: E501
        """Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy_with_http_info(protection_policy_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_name: The Protection Policy name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protection_policy_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_protection_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protection_policy_name' is set
        if ('protection_policy_name' not in params or
                params['protection_policy_name'] is None):
            raise ValueError("Missing the required parameter `protection_policy_name` when calling `get_protection_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protection_policy_name' in params:
            path_params['protection_policy_name'] = params['protection_policy_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/protection-policies/{protection_policy_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_protection_policy_by_id(self, protection_policy_id, **kwargs):  # noqa: E501
        """Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy_by_id(protection_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_id: The Protection Policy ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_protection_policy_by_id_with_http_info(protection_policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_protection_policy_by_id_with_http_info(protection_policy_id, **kwargs)  # noqa: E501
            return data

    def get_protection_policy_by_id_with_http_info(self, protection_policy_id, **kwargs):  # noqa: E501
        """Gets a specific Protection Policy.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_protection_policy_by_id_with_http_info(protection_policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protection_policy_id: The Protection Policy ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protection_policy_id', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_protection_policy_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protection_policy_id' is set
        if ('protection_policy_id' not in params or
                params['protection_policy_id'] is None):
            raise ValueError("Missing the required parameter `protection_policy_id` when calling `get_protection_policy_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protection_policy_id' in params:
            path_params['protection_policy_id'] = params['protection_policy_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/protection-policies/{protection_policy_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionPolicy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_protection_policies(self, **kwargs):  # noqa: E501
        """Gets a list of all Protection Policies.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_protection_policies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_protection_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_protection_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_protection_policies_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of all Protection Policies.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_protection_policies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: ProtectionPolicyList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_protection_policies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/protection-policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProtectionPolicyList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
