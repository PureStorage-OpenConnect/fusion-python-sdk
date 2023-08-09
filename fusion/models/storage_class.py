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

class StorageClass(ResourceMetadata):
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
        'storage_service': 'StorageServiceRef',
        'size_limit': 'int',
        'iops_limit': 'int',
        'bandwidth_limit': 'int'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'storage_service': 'storage_service',
        'size_limit': 'size_limit',
        'iops_limit': 'iops_limit',
        'bandwidth_limit': 'bandwidth_limit'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, storage_service=None, size_limit=None, iops_limit=None, bandwidth_limit=None, *args, **kwargs):  # noqa: E501
        """StorageClass - a model defined in Swagger"""  # noqa: E501
        self._storage_service = None
        self._size_limit = None
        self._iops_limit = None
        self._bandwidth_limit = None
        self.discriminator = None
        if storage_service is not None:
            self.storage_service = storage_service
        self.size_limit = size_limit
        self.iops_limit = iops_limit
        self.bandwidth_limit = bandwidth_limit
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def storage_service(self):
        """Gets the storage_service of this StorageClass.  # noqa: E501


        :return: The storage_service of this StorageClass.  # noqa: E501
        :rtype: StorageServiceRef
        """
        return self._storage_service

    @storage_service.setter
    def storage_service(self, storage_service):
        """Sets the storage_service of this StorageClass.


        :param storage_service: The storage_service of this StorageClass.  # noqa: E501
        :type: StorageServiceRef
        """

        self._storage_service = storage_service

    @property
    def size_limit(self):
        """Gets the size_limit of this StorageClass.  # noqa: E501

        The maximum size allowed  # noqa: E501

        :return: The size_limit of this StorageClass.  # noqa: E501
        :rtype: int
        """
        return self._size_limit

    @size_limit.setter
    def size_limit(self, size_limit):
        """Sets the size_limit of this StorageClass.

        The maximum size allowed  # noqa: E501

        :param size_limit: The size_limit of this StorageClass.  # noqa: E501
        :type: int
        """
        if size_limit is None:
            raise ValueError("Invalid value for `size_limit`, must not be `None`")  # noqa: E501

        self._size_limit = size_limit

    @property
    def iops_limit(self):
        """Gets the iops_limit of this StorageClass.  # noqa: E501

        The maximum IOPS allowed  # noqa: E501

        :return: The iops_limit of this StorageClass.  # noqa: E501
        :rtype: int
        """
        return self._iops_limit

    @iops_limit.setter
    def iops_limit(self, iops_limit):
        """Sets the iops_limit of this StorageClass.

        The maximum IOPS allowed  # noqa: E501

        :param iops_limit: The iops_limit of this StorageClass.  # noqa: E501
        :type: int
        """
        if iops_limit is None:
            raise ValueError("Invalid value for `iops_limit`, must not be `None`")  # noqa: E501

        self._iops_limit = iops_limit

    @property
    def bandwidth_limit(self):
        """Gets the bandwidth_limit of this StorageClass.  # noqa: E501

        The maximum bandwidth allowed  # noqa: E501

        :return: The bandwidth_limit of this StorageClass.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_limit

    @bandwidth_limit.setter
    def bandwidth_limit(self, bandwidth_limit):
        """Sets the bandwidth_limit of this StorageClass.

        The maximum bandwidth allowed  # noqa: E501

        :param bandwidth_limit: The bandwidth_limit of this StorageClass.  # noqa: E501
        :type: int
        """
        if bandwidth_limit is None:
            raise ValueError("Invalid value for `bandwidth_limit`, must not be `None`")  # noqa: E501

        self._bandwidth_limit = bandwidth_limit

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
        if issubclass(StorageClass, dict):
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
        if not isinstance(other, StorageClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
