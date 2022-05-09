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
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class NetworkInterface(ResourceMetadata):
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
        'region': 'RegionRef',
        'availability_zone': 'AvailabilityZoneRef',
        'array': 'ArrayRef',
        'interface_type': 'str',
        'eth': 'NetworkInterfaceEth',
        'services': 'list[str]',
        'enabled': 'bool',
        'network_interface_group': 'NetworkInterfaceGroupRef',
        'max_speed': 'int'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'region': 'region',
        'availability_zone': 'availability_zone',
        'array': 'array',
        'interface_type': 'interface_type',
        'eth': 'eth',
        'services': 'services',
        'enabled': 'enabled',
        'network_interface_group': 'network_interface_group',
        'max_speed': 'max_speed'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, region=None, availability_zone=None, array=None, interface_type=None, eth=None, services=None, enabled=None, network_interface_group=None, max_speed=None, *args, **kwargs):  # noqa: E501
        """NetworkInterface - a model defined in Swagger"""  # noqa: E501
        self._region = None
        self._availability_zone = None
        self._array = None
        self._interface_type = None
        self._eth = None
        self._services = None
        self._enabled = None
        self._network_interface_group = None
        self._max_speed = None
        self.discriminator = None
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if array is not None:
            self.array = array
        self.interface_type = interface_type
        if eth is not None:
            self.eth = eth
        if services is not None:
            self.services = services
        self.enabled = enabled
        if network_interface_group is not None:
            self.network_interface_group = network_interface_group
        self.max_speed = max_speed
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def region(self):
        """Gets the region of this NetworkInterface.  # noqa: E501


        :return: The region of this NetworkInterface.  # noqa: E501
        :rtype: RegionRef
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this NetworkInterface.


        :param region: The region of this NetworkInterface.  # noqa: E501
        :type: RegionRef
        """

        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NetworkInterface.  # noqa: E501


        :return: The availability_zone of this NetworkInterface.  # noqa: E501
        :rtype: AvailabilityZoneRef
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NetworkInterface.


        :param availability_zone: The availability_zone of this NetworkInterface.  # noqa: E501
        :type: AvailabilityZoneRef
        """

        self._availability_zone = availability_zone

    @property
    def array(self):
        """Gets the array of this NetworkInterface.  # noqa: E501


        :return: The array of this NetworkInterface.  # noqa: E501
        :rtype: ArrayRef
        """
        return self._array

    @array.setter
    def array(self, array):
        """Sets the array of this NetworkInterface.


        :param array: The array of this NetworkInterface.  # noqa: E501
        :type: ArrayRef
        """

        self._array = array

    @property
    def interface_type(self):
        """Gets the interface_type of this NetworkInterface.  # noqa: E501

        The interface type.  # noqa: E501

        :return: The interface_type of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this NetworkInterface.

        The interface type.  # noqa: E501

        :param interface_type: The interface_type of this NetworkInterface.  # noqa: E501
        :type: str
        """
        if interface_type is None:
            raise ValueError("Invalid value for `interface_type`, must not be `None`")  # noqa: E501
        allowed_values = ["eth"]  # noqa: E501
        if interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interface_type, allowed_values)
            )

        self._interface_type = interface_type

    @property
    def eth(self):
        """Gets the eth of this NetworkInterface.  # noqa: E501


        :return: The eth of this NetworkInterface.  # noqa: E501
        :rtype: NetworkInterfaceEth
        """
        return self._eth

    @eth.setter
    def eth(self, eth):
        """Sets the eth of this NetworkInterface.


        :param eth: The eth of this NetworkInterface.  # noqa: E501
        :type: NetworkInterfaceEth
        """

        self._eth = eth

    @property
    def services(self):
        """Gets the services of this NetworkInterface.  # noqa: E501

        The services provided by this Network Interface.  # noqa: E501

        :return: The services of this NetworkInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this NetworkInterface.

        The services provided by this Network Interface.  # noqa: E501

        :param services: The services of this NetworkInterface.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def enabled(self):
        """Gets the enabled of this NetworkInterface.  # noqa: E501

        True if interface is in use.  # noqa: E501

        :return: The enabled of this NetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NetworkInterface.

        True if interface is in use.  # noqa: E501

        :param enabled: The enabled of this NetworkInterface.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def network_interface_group(self):
        """Gets the network_interface_group of this NetworkInterface.  # noqa: E501


        :return: The network_interface_group of this NetworkInterface.  # noqa: E501
        :rtype: NetworkInterfaceGroupRef
        """
        return self._network_interface_group

    @network_interface_group.setter
    def network_interface_group(self, network_interface_group):
        """Sets the network_interface_group of this NetworkInterface.


        :param network_interface_group: The network_interface_group of this NetworkInterface.  # noqa: E501
        :type: NetworkInterfaceGroupRef
        """

        self._network_interface_group = network_interface_group

    @property
    def max_speed(self):
        """Gets the max_speed of this NetworkInterface.  # noqa: E501

        Configured speed of this Network Interface. Typically this is the maximum speed of the port or bond represented by the Network Interface.  # noqa: E501

        :return: The max_speed of this NetworkInterface.  # noqa: E501
        :rtype: int
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        """Sets the max_speed of this NetworkInterface.

        Configured speed of this Network Interface. Typically this is the maximum speed of the port or bond represented by the Network Interface.  # noqa: E501

        :param max_speed: The max_speed of this NetworkInterface.  # noqa: E501
        :type: int
        """
        if max_speed is None:
            raise ValueError("Invalid value for `max_speed`, must not be `None`")  # noqa: E501

        self._max_speed = max_speed

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
        if issubclass(NetworkInterface, dict):
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
        if not isinstance(other, NetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
