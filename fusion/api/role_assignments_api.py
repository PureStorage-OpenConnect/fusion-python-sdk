# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fusion.api_client import ApiClient


class RoleAssignmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_role_assignment(self, body, role_name, **kwargs):  # noqa: E501
        """Creates a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_assignment(body, role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleAssignmentPost body: (required)
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_role_assignment_with_http_info(body, role_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_role_assignment_with_http_info(body, role_name, **kwargs)  # noqa: E501
            return data

    def create_role_assignment_with_http_info(self, body, role_name, **kwargs):  # noqa: E501
        """Creates a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_assignment_with_http_info(body, role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleAssignmentPost body: (required)
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'role_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_role_assignment`")  # noqa: E501
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `create_role_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['role_name'] = params['role_name']  # noqa: E501

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
            '/roles/{role_name}/role-assignments', 'POST',
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

    def delete_role_assignment(self, role_name, role_assignment_name, **kwargs):  # noqa: E501
        """Delete a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_assignment(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_role_assignment_with_http_info(role_name, role_assignment_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_role_assignment_with_http_info(role_name, role_assignment_name, **kwargs)  # noqa: E501
            return data

    def delete_role_assignment_with_http_info(self, role_name, role_assignment_name, **kwargs):  # noqa: E501
        """Delete a Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_assignment_with_http_info(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_name', 'role_assignment_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `delete_role_assignment`")  # noqa: E501
        # verify the required parameter 'role_assignment_name' is set
        if ('role_assignment_name' not in params or
                params['role_assignment_name'] is None):
            raise ValueError("Missing the required parameter `role_assignment_name` when calling `delete_role_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['role_name'] = params['role_name']  # noqa: E501
        if 'role_assignment_name' in params:
            path_params['role_assignment_name'] = params['role_assignment_name']  # noqa: E501

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
            '/roles/{role_name}/role-assignments/{role_assignment_name}', 'DELETE',
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

    def get_role_assignment(self, role_name, role_assignment_name, **kwargs):  # noqa: E501
        """Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_assignment_with_http_info(role_name, role_assignment_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_assignment_with_http_info(role_name, role_assignment_name, **kwargs)  # noqa: E501
            return data

    def get_role_assignment_with_http_info(self, role_name, role_assignment_name, **kwargs):  # noqa: E501
        """Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment_with_http_info(role_name, role_assignment_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str role_assignment_name: The Role Assignment name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_name', 'role_assignment_name', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `get_role_assignment`")  # noqa: E501
        # verify the required parameter 'role_assignment_name' is set
        if ('role_assignment_name' not in params or
                params['role_assignment_name'] is None):
            raise ValueError("Missing the required parameter `role_assignment_name` when calling `get_role_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['role_name'] = params['role_name']  # noqa: E501
        if 'role_assignment_name' in params:
            path_params['role_assignment_name'] = params['role_assignment_name']  # noqa: E501

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
            '/roles/{role_name}/role-assignments/{role_assignment_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleAssignment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role_assignment_by_id(self, role_assignment_id, **kwargs):  # noqa: E501
        """Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment_by_id(role_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_assignment_id: The Role Assignment ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_assignment_by_id_with_http_info(role_assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_assignment_by_id_with_http_info(role_assignment_id, **kwargs)  # noqa: E501
            return data

    def get_role_assignment_by_id_with_http_info(self, role_assignment_id, **kwargs):  # noqa: E501
        """Gets a specific Role Assignment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_assignment_by_id_with_http_info(role_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_assignment_id: The Role Assignment ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: RoleAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_assignment_id', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_assignment_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_assignment_id' is set
        if ('role_assignment_id' not in params or
                params['role_assignment_id'] is None):
            raise ValueError("Missing the required parameter `role_assignment_id` when calling `get_role_assignment_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_assignment_id' in params:
            path_params['role_assignment_id'] = params['role_assignment_id']  # noqa: E501

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
            '/resources/role-assignments/{role_assignment_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleAssignment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_role_assignments(self, role_name, **kwargs):  # noqa: E501
        """Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_assignments_with_http_info(role_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_role_assignments_with_http_info(role_name, **kwargs)  # noqa: E501
            return data

    def list_role_assignments_with_http_info(self, role_name, **kwargs):  # noqa: E501
        """Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_with_http_info(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: The Role name (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_name', 'x_request_id', 'authorization', 'x_correlation_id', 'scope', 'principal']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_assignments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params or
                params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `list_role_assignments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_name' in params:
            path_params['role_name'] = params['role_name']  # noqa: E501

        query_params = []
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'principal' in params:
            query_params.append(('principal', params['principal']))  # noqa: E501

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
            '/roles/{role_name}/role-assignments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RoleAssignment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_role_assignments_canonical(self, **kwargs):  # noqa: E501
        """Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_canonical(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :param str role:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_assignments_canonical_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_role_assignments_canonical_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_role_assignments_canonical_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of all Role Assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_canonical_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str scope:
        :param str principal:
        :param str role:
        :return: list[RoleAssignment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'authorization', 'x_correlation_id', 'scope', 'principal', 'role']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_assignments_canonical" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'principal' in params:
            query_params.append(('principal', params['principal']))  # noqa: E501
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501

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
            '/resources/role-assignments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RoleAssignment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
