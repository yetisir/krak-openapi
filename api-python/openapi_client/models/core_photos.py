# coding: utf-8

"""
    Krak REST API

    Krak REST API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class CorePhotos(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'photo': 'file',
        'data': 'CorePhotosData'
    }

    attribute_map = {
        'photo': 'photo',
        'data': 'data'
    }

    def __init__(self, photo=None, data=None, local_vars_configuration=None):  # noqa: E501
        """CorePhotos - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._photo = None
        self._data = None
        self.discriminator = None

        self.photo = photo
        self.data = data

    @property
    def photo(self):
        """Gets the photo of this CorePhotos.  # noqa: E501


        :return: The photo of this CorePhotos.  # noqa: E501
        :rtype: file
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this CorePhotos.


        :param photo: The photo of this CorePhotos.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and photo is None:  # noqa: E501
            raise ValueError("Invalid value for `photo`, must not be `None`")  # noqa: E501

        self._photo = photo

    @property
    def data(self):
        """Gets the data of this CorePhotos.  # noqa: E501


        :return: The data of this CorePhotos.  # noqa: E501
        :rtype: CorePhotosData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CorePhotos.


        :param data: The data of this CorePhotos.  # noqa: E501
        :type: CorePhotosData
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CorePhotos):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CorePhotos):
            return True

        return self.to_dict() != other.to_dict()
