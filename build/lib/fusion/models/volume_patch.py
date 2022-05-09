# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from fusion.models.resource_patch import ResourcePatch  # noqa: F401,E501

class VolumePatch(ResourcePatch):
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
        'source_volume_snapshot_link': 'NullableString',
        'size': 'NullableSize',
        'storage_class': 'NullableString',
        'placement_group': 'NullableString',
        'protection_policy': 'NullableString',
        'host_access_policies': 'NullableString'
    }
    if hasattr(ResourcePatch, "swagger_types"):
        swagger_types.update(ResourcePatch.swagger_types)

    attribute_map = {
        'source_volume_snapshot_link': 'source_volume_snapshot_link',
        'size': 'size',
        'storage_class': 'storage_class',
        'placement_group': 'placement_group',
        'protection_policy': 'protection_policy',
        'host_access_policies': 'host_access_policies'
    }
    if hasattr(ResourcePatch, "attribute_map"):
        attribute_map.update(ResourcePatch.attribute_map)

    def __init__(self, source_volume_snapshot_link=None, size=None, storage_class=None, placement_group=None, protection_policy=None, host_access_policies=None, *args, **kwargs):  # noqa: E501
        """VolumePatch - a model defined in Swagger"""  # noqa: E501
        self._source_volume_snapshot_link = None
        self._size = None
        self._storage_class = None
        self._placement_group = None
        self._protection_policy = None
        self._host_access_policies = None
        self.discriminator = None
        if source_volume_snapshot_link is not None:
            self.source_volume_snapshot_link = source_volume_snapshot_link
        if size is not None:
            self.size = size
        if storage_class is not None:
            self.storage_class = storage_class
        if placement_group is not None:
            self.placement_group = placement_group
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if host_access_policies is not None:
            self.host_access_policies = host_access_policies
        ResourcePatch.__init__(self, *args, **kwargs)

    @property
    def source_volume_snapshot_link(self):
        """Gets the source_volume_snapshot_link of this VolumePatch.  # noqa: E501


        :return: The source_volume_snapshot_link of this VolumePatch.  # noqa: E501
        :rtype: NullableString
        """
        return self._source_volume_snapshot_link

    @source_volume_snapshot_link.setter
    def source_volume_snapshot_link(self, source_volume_snapshot_link):
        """Sets the source_volume_snapshot_link of this VolumePatch.


        :param source_volume_snapshot_link: The source_volume_snapshot_link of this VolumePatch.  # noqa: E501
        :type: NullableString
        """

        self._source_volume_snapshot_link = source_volume_snapshot_link

    @property
    def size(self):
        """Gets the size of this VolumePatch.  # noqa: E501


        :return: The size of this VolumePatch.  # noqa: E501
        :rtype: NullableSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumePatch.


        :param size: The size of this VolumePatch.  # noqa: E501
        :type: NullableSize
        """

        self._size = size

    @property
    def storage_class(self):
        """Gets the storage_class of this VolumePatch.  # noqa: E501


        :return: The storage_class of this VolumePatch.  # noqa: E501
        :rtype: NullableString
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this VolumePatch.


        :param storage_class: The storage_class of this VolumePatch.  # noqa: E501
        :type: NullableString
        """

        self._storage_class = storage_class

    @property
    def placement_group(self):
        """Gets the placement_group of this VolumePatch.  # noqa: E501


        :return: The placement_group of this VolumePatch.  # noqa: E501
        :rtype: NullableString
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this VolumePatch.


        :param placement_group: The placement_group of this VolumePatch.  # noqa: E501
        :type: NullableString
        """

        self._placement_group = placement_group

    @property
    def protection_policy(self):
        """Gets the protection_policy of this VolumePatch.  # noqa: E501


        :return: The protection_policy of this VolumePatch.  # noqa: E501
        :rtype: NullableString
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this VolumePatch.


        :param protection_policy: The protection_policy of this VolumePatch.  # noqa: E501
        :type: NullableString
        """

        self._protection_policy = protection_policy

    @property
    def host_access_policies(self):
        """Gets the host_access_policies of this VolumePatch.  # noqa: E501


        :return: The host_access_policies of this VolumePatch.  # noqa: E501
        :rtype: NullableString
        """
        return self._host_access_policies

    @host_access_policies.setter
    def host_access_policies(self, host_access_policies):
        """Sets the host_access_policies of this VolumePatch.


        :param host_access_policies: The host_access_policies of this VolumePatch.  # noqa: E501
        :type: NullableString
        """

        self._host_access_policies = host_access_policies

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
        if issubclass(VolumePatch, dict):
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
        if not isinstance(other, VolumePatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
