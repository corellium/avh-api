# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.15.0-15704
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from avh_api_async.configuration import Configuration


class Address(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'postal_code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'postal_code': 'postal_code',
        'state': 'state'
    }

    def __init__(self, address1=None, address2=None, city=None, country=None, postal_code=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._postal_code = None
        self._state = None
        self.discriminator = None

        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.state = state

    @property
    def address1(self):
        """Gets the address1 of this Address.  # noqa: E501

        Address line 1 (e.g., street, PO Box, or company name).  # noqa: E501

        :return: The address1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Address.

        Address line 1 (e.g., street, PO Box, or company name).  # noqa: E501

        :param address1: The address1 of this Address.  # noqa: E501
        :type address1: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Address.  # noqa: E501

        Address line 2 (e.g., apartment, suite, unit, or building).  # noqa: E501

        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Address.

        Address line 2 (e.g., apartment, suite, unit, or building).  # noqa: E501

        :param address2: The address2 of this Address.  # noqa: E501
        :type address2: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        City, district, suburb, town, or village.  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        City, district, suburb, town, or village.  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        Two-letter country code (ISO 3166-1 alpha-2).  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        Two-letter country code (ISO 3166-1 alpha-2).  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        ZIP or postal code.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        ZIP or postal code.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type postal_code: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501

        State, county, province, or region.  # noqa: E501

        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.

        State, county, province, or region.  # noqa: E501

        :param state: The state of this Address.  # noqa: E501
        :type state: str
        """

        self._state = state

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()