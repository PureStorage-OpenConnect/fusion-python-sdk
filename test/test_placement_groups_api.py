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
from fusion.api.placement_groups_api import PlacementGroupsApi  # noqa: E501
from fusion.rest import ApiException


class TestPlacementGroupsApi(unittest.TestCase):
    """PlacementGroupsApi unit test stubs"""

    def setUp(self):
        self.api = PlacementGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_placement_group(self):
        """Test case for create_placement_group

        Creates a Placement Group.  # noqa: E501
        """
        pass

    def test_delete_placement_group(self):
        """Test case for delete_placement_group

        Deletes a specific Placement Group.  # noqa: E501
        """
        pass

    def test_get_placement_group(self):
        """Test case for get_placement_group

        Gets a specific Placement Group.  # noqa: E501
        """
        pass

    def test_get_placement_group_by_id(self):
        """Test case for get_placement_group_by_id

        Gets a specific Placement Group.  # noqa: E501
        """
        pass

    def test_get_placement_group_sessions(self):
        """Test case for get_placement_group_sessions

        Gets iSCSI sessions data of a specific Placement Group.  # noqa: E501
        """
        pass

    def test_get_placement_groups_performance(self):
        """Test case for get_placement_groups_performance

        Get performance metrics of a specific Placement Group  # noqa: E501
        """
        pass

    def test_get_placement_groups_space(self):
        """Test case for get_placement_groups_space

        Get space metrics of a specific Placement Group  # noqa: E501
        """
        pass

    def test_list_placement_groups(self):
        """Test case for list_placement_groups

        Gets a list of all Placement Groups.  # noqa: E501
        """
        pass

    def test_query_placement_groups(self):
        """Test case for query_placement_groups

        Returns a list of Placement Groups from query  # noqa: E501
        """
        pass

    def test_update_placement_group(self):
        """Test case for update_placement_group

        Updates a specific Placement Group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
