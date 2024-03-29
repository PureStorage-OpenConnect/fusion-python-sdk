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

class StorageService(ResourceMetadata):
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
        'hardware_types': 'list[HardwareTypeRef]'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'hardware_types': 'hardware_types'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, hardware_types=None, *args, **kwargs):  # noqa: E501
        """StorageService - a model defined in Swagger"""  # noqa: E501
        self._hardware_types = None
        self.discriminator = None
        if hardware_types is not None:
            self.hardware_types = hardware_types
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def hardware_types(self):
        """Gets the hardware_types of this StorageService.  # noqa: E501


        :return: The hardware_types of this StorageService.  # noqa: E501
        :rtype: list[HardwareTypeRef]
        """
        return self._hardware_types

    @hardware_types.setter
    def hardware_types(self, hardware_types):
        """Sets the hardware_types of this StorageService.


        :param hardware_types: The hardware_types of this StorageService.  # noqa: E501
        :type: list[HardwareTypeRef]
        """

        self._hardware_types = hardware_types

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
        if issubclass(StorageService, dict):
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
        if not isinstance(other, StorageService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
