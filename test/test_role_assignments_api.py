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
from fusion.api.role_assignments_api import RoleAssignmentsApi  # noqa: E501
from fusion.rest import ApiException


class TestRoleAssignmentsApi(unittest.TestCase):
    """RoleAssignmentsApi unit test stubs"""

    def setUp(self):
        self.api = RoleAssignmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role_assignment(self):
        """Test case for create_role_assignment

        Creates a Role Assignment.  # noqa: E501
        """
        pass

    def test_delete_role_assignment(self):
        """Test case for delete_role_assignment

        Delete a Role Assignment.  # noqa: E501
        """
        pass

    def test_get_role_assignment(self):
        """Test case for get_role_assignment

        Gets a specific Role Assignment.  # noqa: E501
        """
        pass

    def test_get_role_assignment_by_id(self):
        """Test case for get_role_assignment_by_id

        Gets a specific Role Assignment.  # noqa: E501
        """
        pass

    def test_list_role_assignments(self):
        """Test case for list_role_assignments

        Gets a list of all Role Assignments.  # noqa: E501
        """
        pass

    def test_list_role_assignments_canonical(self):
        """Test case for list_role_assignments_canonical

        Gets a list of all Role Assignments.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
