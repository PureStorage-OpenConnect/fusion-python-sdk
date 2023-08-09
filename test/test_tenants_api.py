# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.tenants_api import TenantsApi  # noqa: E501
from fusion.rest import ApiException


class TestTenantsApi(unittest.TestCase):
    """TenantsApi unit test stubs"""

    def setUp(self):
        self.api = TenantsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tenant(self):
        """Test case for create_tenant

        Creates a Tenant.  # noqa: E501
        """
        pass

    def test_delete_tenant(self):
        """Test case for delete_tenant

        Deletes a specific Tenant.  # noqa: E501
        """
        pass

    def test_get_tenant(self):
        """Test case for get_tenant

        Gets a specific Tenant.  # noqa: E501
        """
        pass

    def test_get_tenant_by_id(self):
        """Test case for get_tenant_by_id

        Gets a specific Tenant.  # noqa: E501
        """
        pass

    def test_get_tenant_performance(self):
        """Test case for get_tenant_performance

        Gets performance metrics of a specific Tenant.  # noqa: E501
        """
        pass

    def test_get_tenants_space(self):
        """Test case for get_tenants_space

        Gets space metrics of a specific Tenant.  # noqa: E501
        """
        pass

    def test_list_tenants(self):
        """Test case for list_tenants

        Gets a list of all Tenants.  # noqa: E501
        """
        pass

    def test_query_tenants(self):
        """Test case for query_tenants

        Get all Tenants in the org. Provide a filter to search for specific Tenants.  # noqa: E501
        """
        pass

    def test_update_tenant(self):
        """Test case for update_tenant

        Updates a Tenant.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
