# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.workload_planner_api import WorkloadPlannerApi  # noqa: E501
from fusion.rest import ApiException


class TestWorkloadPlannerApi(unittest.TestCase):
    """WorkloadPlannerApi unit test stubs"""

    def setUp(self):
        self.api = WorkloadPlannerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_placement_recommendation(self):
        """Test case for create_placement_recommendation

        (Provider) Generates a report on the candidate arrays a given placement group can be placed/migrated to  # noqa: E501
        """
        pass

    def test_get_placement_recommendation(self):
        """Test case for get_placement_recommendation

        Gets a specific placement recommendation report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
