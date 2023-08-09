# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class PlacementGroup(ResourceMetadata):
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
        'availability_zone': 'AvailabilityZoneRef',
        'protocols': 'Target',
        'storage_service': 'StorageServiceRef',
        'array': 'ArrayRef'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'tenant': 'tenant',
        'tenant_space': 'tenant_space',
        'placement_engine': 'placement_engine',
        'availability_zone': 'availability_zone',
        'protocols': 'protocols',
        'storage_service': 'storage_service',
        'array': 'array'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, tenant=None, tenant_space=None, placement_engine=None, availability_zone=None, protocols=None, storage_service=None, array=None, *args, **kwargs):  # noqa: E501
        """PlacementGroup - a model defined in Swagger"""  # noqa: E501
        self._tenant = None
        self._tenant_space = None
        self._placement_engine = None
        self._availability_zone = None
        self._protocols = None
        self._storage_service = None
        self._array = None
        self.discriminator = None
        if tenant is not None:
            self.tenant = tenant
        self.tenant_space = tenant_space
        if placement_engine is not None:
            self.placement_engine = placement_engine
        self.availability_zone = availability_zone
        if protocols is not None:
            self.protocols = protocols
        if storage_service is not None:
            self.storage_service = storage_service
        if array is not None:
            self.array = array
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def tenant(self):
        """Gets the tenant of this PlacementGroup.  # noqa: E501


        :return: The tenant of this PlacementGroup.  # noqa: E501
        :rtype: TenantRef
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PlacementGroup.


        :param tenant: The tenant of this PlacementGroup.  # noqa: E501
        :type: TenantRef
        """

        self._tenant = tenant

    @property
    def tenant_space(self):
        """Gets the tenant_space of this PlacementGroup.  # noqa: E501


        :return: The tenant_space of this PlacementGroup.  # noqa: E501
        :rtype: TenantSpaceRef
        """
        return self._tenant_space

    @tenant_space.setter
    def tenant_space(self, tenant_space):
        """Sets the tenant_space of this PlacementGroup.


        :param tenant_space: The tenant_space of this PlacementGroup.  # noqa: E501
        :type: TenantSpaceRef
        """
        if tenant_space is None:
            raise ValueError("Invalid value for `tenant_space`, must not be `None`")  # noqa: E501

        self._tenant_space = tenant_space

    @property
    def placement_engine(self):
        """Gets the placement_engine of this PlacementGroup.  # noqa: E501


        :return: The placement_engine of this PlacementGroup.  # noqa: E501
        :rtype: PlacementEngine
        """
        return self._placement_engine

    @placement_engine.setter
    def placement_engine(self, placement_engine):
        """Sets the placement_engine of this PlacementGroup.


        :param placement_engine: The placement_engine of this PlacementGroup.  # noqa: E501
        :type: PlacementEngine
        """

        self._placement_engine = placement_engine

    @property
    def availability_zone(self):
        """Gets the availability_zone of this PlacementGroup.  # noqa: E501


        :return: The availability_zone of this PlacementGroup.  # noqa: E501
        :rtype: AvailabilityZoneRef
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this PlacementGroup.


        :param availability_zone: The availability_zone of this PlacementGroup.  # noqa: E501
        :type: AvailabilityZoneRef
        """
        if availability_zone is None:
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501

        self._availability_zone = availability_zone

    @property
    def protocols(self):
        """Gets the protocols of this PlacementGroup.  # noqa: E501


        :return: The protocols of this PlacementGroup.  # noqa: E501
        :rtype: Target
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this PlacementGroup.


        :param protocols: The protocols of this PlacementGroup.  # noqa: E501
        :type: Target
        """

        self._protocols = protocols

    @property
    def storage_service(self):
        """Gets the storage_service of this PlacementGroup.  # noqa: E501


        :return: The storage_service of this PlacementGroup.  # noqa: E501
        :rtype: StorageServiceRef
        """
        return self._storage_service

    @storage_service.setter
    def storage_service(self, storage_service):
        """Sets the storage_service of this PlacementGroup.


        :param storage_service: The storage_service of this PlacementGroup.  # noqa: E501
        :type: StorageServiceRef
        """

        self._storage_service = storage_service

    @property
    def array(self):
        """Gets the array of this PlacementGroup.  # noqa: E501


        :return: The array of this PlacementGroup.  # noqa: E501
        :rtype: ArrayRef
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this PlacementGroup.


        :param array: The array of this PlacementGroup.  # noqa: E501
        :type: ArrayRef
        """

        self._array = array

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
        if issubclass(PlacementGroup, dict):
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
        if not isinstance(other, PlacementGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
