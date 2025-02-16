# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.org import Org  # noqa: F401,E501
from swagger_server import util


class UserOrg(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, org_id: int=None, name: str=None, privilege: int=None, user_org_id: str=None):  # noqa: E501
        """UserOrg - a model defined in Swagger

        :param org_id: The org_id of this UserOrg.  # noqa: E501
        :type org_id: int
        :param name: The name of this UserOrg.  # noqa: E501
        :type name: str
        :param privilege: The privilege of this UserOrg.  # noqa: E501
        :type privilege: int
        :param user_org_id: The user_org_id of this UserOrg.  # noqa: E501
        :type user_org_id: str
        """
        self.swagger_types = {
            'org_id': int,
            'name': str,
            'privilege': int,
            'user_org_id': str
        }

        self.attribute_map = {
            'org_id': 'org_id',
            'name': 'name',
            'privilege': 'privilege',
            'user_org_id': 'user_org_id'
        }
        self._org_id = org_id
        self._name = name
        self._privilege = privilege
        self._user_org_id = user_org_id

    @classmethod
    def from_dict(cls, dikt) -> 'UserOrg':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_org of this UserOrg.  # noqa: E501
        :rtype: UserOrg
        """
        return util.deserialize_model(dikt, cls)

    @property
    def org_id(self) -> int:
        """Gets the org_id of this UserOrg.

        A unique identifier  # noqa: E501

        :return: The org_id of this UserOrg.
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id: int):
        """Sets the org_id of this UserOrg.

        A unique identifier  # noqa: E501

        :param org_id: The org_id of this UserOrg.
        :type org_id: int
        """

        self._org_id = org_id

    @property
    def name(self) -> str:
        """Gets the name of this UserOrg.

        The name of the org  # noqa: E501

        :return: The name of this UserOrg.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserOrg.

        The name of the org  # noqa: E501

        :param name: The name of this UserOrg.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def privilege(self) -> int:
        """Gets the privilege of this UserOrg.

        The privilege level within the org  # noqa: E501

        :return: The privilege of this UserOrg.
        :rtype: int
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege: int):
        """Sets the privilege of this UserOrg.

        The privilege level within the org  # noqa: E501

        :param privilege: The privilege of this UserOrg.
        :type privilege: int
        """
        if privilege is None:
            raise ValueError("Invalid value for `privilege`, must not be `None`")  # noqa: E501

        self._privilege = privilege

    @property
    def user_org_id(self) -> str:
        """Gets the user_org_id of this UserOrg.

        The ID used by the user to identify himself within the org(Driver License, Passport, etc...)  # noqa: E501

        :return: The user_org_id of this UserOrg.
        :rtype: str
        """
        return self._user_org_id

    @user_org_id.setter
    def user_org_id(self, user_org_id: str):
        """Sets the user_org_id of this UserOrg.

        The ID used by the user to identify himself within the org(Driver License, Passport, etc...)  # noqa: E501

        :param user_org_id: The user_org_id of this UserOrg.
        :type user_org_id: str
        """
        if user_org_id is None:
            raise ValueError("Invalid value for `user_org_id`, must not be `None`")  # noqa: E501

        self._user_org_id = user_org_id
