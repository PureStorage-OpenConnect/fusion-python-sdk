# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class PlacementRecommendation(ResourceMetadata):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tenant': 'TenantRef',
        'tenant_space': 'TenantSpaceRef',
        'placement_engine': 'PlacementEngine',
        'placement_group_id': 'str',
        'placement_group': 'PlacementGroupRef',
        'simulated_placement': 'SimulatedPlacement',
        'included_arrays': 'list[PlacementRecommendationIncludedArray]',
        'excluded_arrays': 'list[PlacementRecommendationExcludedArray]',
        'target_arrays': 'list[ArrayRef]',
        'time_remaining': 'int'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'tenant': 'tenant',
        'tenant_space': 'tenant_space',
        'placement_engine': 'placement_engine',
        'placement_group_id': 'placement_group_id',
        'placement_group': 'placement_group',
        'simulated_placement': 'simulated_placement',
        'included_arrays': 'included_arrays',
        'excluded_arrays': 'excluded_arrays',
        'target_arrays': 'target_arrays',
        'time_remaining': 'time_remaining'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, tenant=None, tenant_space=None, placement_engine=None, placement_group_id=None, placement_group=None, simulated_placement=None, included_arrays=None, excluded_arrays=None, target_arrays=None, time_remaining=None, *args, **kwargs):  # noqa: E501
        """PlacementRecommendation - a model defined in Swagger"""  # noqa: E501
        self._tenant = None
        self._tenant_space = None
        self._placement_engine = None
        self._placement_group_id = None
        self._placement_group = None
        self._simulated_placement = None
        self._included_arrays = None
        self._excluded_arrays = None
        self._target_arrays = None
        self._time_remaining = None
        self.discriminator = None
        if tenant is not None:
            self.tenant = tenant
        if tenant_space is not None:
            self.tenant_space = tenant_space
        if placement_engine is not None:
            self.placement_engine = placement_engine
        if placement_group_id is not None:
            self.placement_group_id = placement_group_id
        if placement_group is not None:
            self.placement_group = placement_group
        if simulated_placement is not None:
            self.simulated_placement = simulated_placement
        if included_arrays is not None:
            self.included_arrays = included_arrays
        if excluded_arrays is not None:
            self.excluded_arrays = excluded_arrays
        if target_arrays is not None:
            self.target_arrays = target_arrays
        if time_remaining is not None:
            self.time_remaining = time_remaining
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def tenant(self):
        """Gets the tenant of this PlacementRecommendation.  # noqa: E501


        :return: The tenant of this PlacementRecommendation.  # noqa: E501
        :rtype: TenantRef
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PlacementRecommendation.


        :param tenant: The tenant of this PlacementRecommendation.  # noqa: E501
        :type: TenantRef
        """

        self._tenant = tenant

    @property
    def tenant_space(self):
        """Gets the tenant_space of this PlacementRecommendation.  # noqa: E501


        :return: The tenant_space of this PlacementRecommendation.  # noqa: E501
        :rtype: TenantSpaceRef
        """
        return self._tenant_space

    @tenant_space.setter
    def tenant_space(self, tenant_space):
        """Sets the tenant_space of this PlacementRecommendation.


        :param tenant_space: The tenant_space of this PlacementRecommendation.  # noqa: E501
        :type: TenantSpaceRef
        """

        self._tenant_space = tenant_space

    @property
    def placement_engine(self):
        """Gets the placement_engine of this PlacementRecommendation.  # noqa: E501


        :return: The placement_engine of this PlacementRecommendation.  # noqa: E501
        :rtype: PlacementEngine
        """
        return self._placement_engine

    @placement_engine.setter
    def placement_engine(self, placement_engine):
        """Sets the placement_engine of this PlacementRecommendation.


        :param placement_engine: The placement_engine of this PlacementRecommendation.  # noqa: E501
        :type: PlacementEngine
        """

        self._placement_engine = placement_engine

    @property
    def placement_group_id(self):
        """Gets the placement_group_id of this PlacementRecommendation.  # noqa: E501

        If not empty, this is the Placement Group ID for which the placement recommendation was made  # noqa: E501

        :return: The placement_group_id of this PlacementRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._placement_group_id

    @placement_group_id.setter
    def placement_group_id(self, placement_group_id):
        """Sets the placement_group_id of this PlacementRecommendation.

        If not empty, this is the Placement Group ID for which the placement recommendation was made  # noqa: E501

        :param placement_group_id: The placement_group_id of this PlacementRecommendation.  # noqa: E501
        :type: str
        """

        self._placement_group_id = placement_group_id

    @property
    def placement_group(self):
        """Gets the placement_group of this PlacementRecommendation.  # noqa: E501


        :return: The placement_group of this PlacementRecommendation.  # noqa: E501
        :rtype: PlacementGroupRef
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this PlacementRecommendation.


        :param placement_group: The placement_group of this PlacementRecommendation.  # noqa: E501
        :type: PlacementGroupRef
        """

        self._placement_group = placement_group

    @property
    def simulated_placement(self):
        """Gets the simulated_placement of this PlacementRecommendation.  # noqa: E501


        :return: The simulated_placement of this PlacementRecommendation.  # noqa: E501
        :rtype: SimulatedPlacement
        """
        return self._simulated_placement

    @simulated_placement.setter
    def simulated_placement(self, simulated_placement):
        """Sets the simulated_placement of this PlacementRecommendation.


        :param simulated_placement: The simulated_placement of this PlacementRecommendation.  # noqa: E501
        :type: SimulatedPlacement
        """

        self._simulated_placement = simulated_placement

    @property
    def included_arrays(self):
        """Gets the included_arrays of this PlacementRecommendation.  # noqa: E501

        A JSON array of Arrays that the Placement Group can be placed/migrated to  # noqa: E501

        :return: The included_arrays of this PlacementRecommendation.  # noqa: E501
        :rtype: list[PlacementRecommendationIncludedArray]
        """
        return self._included_arrays

    @included_arrays.setter
    def included_arrays(self, included_arrays):
        """Sets the included_arrays of this PlacementRecommendation.

        A JSON array of Arrays that the Placement Group can be placed/migrated to  # noqa: E501

        :param included_arrays: The included_arrays of this PlacementRecommendation.  # noqa: E501
        :type: list[PlacementRecommendationIncludedArray]
        """

        self._included_arrays = included_arrays

    @property
    def excluded_arrays(self):
        """Gets the excluded_arrays of this PlacementRecommendation.  # noqa: E501

        A JSON array of Arrays that the Placement Group cannot be placed on  # noqa: E501

        :return: The excluded_arrays of this PlacementRecommendation.  # noqa: E501
        :rtype: list[PlacementRecommendationExcludedArray]
        """
        return self._excluded_arrays

    @excluded_arrays.setter
    def excluded_arrays(self, excluded_arrays):
        """Sets the excluded_arrays of this PlacementRecommendation.

        A JSON array of Arrays that the Placement Group cannot be placed on  # noqa: E501

        :param excluded_arrays: The excluded_arrays of this PlacementRecommendation.  # noqa: E501
        :type: list[PlacementRecommendationExcludedArray]
        """

        self._excluded_arrays = excluded_arrays

    @property
    def target_arrays(self):
        """Gets the target_arrays of this PlacementRecommendation.  # noqa: E501

        If present, this is the list of arrays that was provided when requesting the placement recommendation report to consider for placement recommendations  # noqa: E501

        :return: The target_arrays of this PlacementRecommendation.  # noqa: E501
        :rtype: list[ArrayRef]
        """
        return self._target_arrays

    @target_arrays.setter
    def target_arrays(self, target_arrays):
        """Sets the target_arrays of this PlacementRecommendation.

        If present, this is the list of arrays that was provided when requesting the placement recommendation report to consider for placement recommendations  # noqa: E501

        :param target_arrays: The target_arrays of this PlacementRecommendation.  # noqa: E501
        :type: list[ArrayRef]
        """

        self._target_arrays = target_arrays

    @property
    def time_remaining(self):
        """Gets the time_remaining of this PlacementRecommendation.  # noqa: E501

        Number of milliseconds left before this Placement Recommendation report is deleted  # noqa: E501

        :return: The time_remaining of this PlacementRecommendation.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this PlacementRecommendation.

        Number of milliseconds left before this Placement Recommendation report is deleted  # noqa: E501

        :param time_remaining: The time_remaining of this PlacementRecommendation.  # noqa: E501
        :type: int
        """

        self._time_remaining = time_remaining

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlacementRecommendation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlacementRecommendation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
