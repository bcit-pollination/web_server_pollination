# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ElectionInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, election_description: str=None, election_id: int=None, org_id: int=None, start_time: str=None, end_time: str=None, anonymous: bool=None, verified: bool=None, public_results: bool=None):  # noqa: E501
        """ElectionInfo - a model defined in Swagger

        :param election_description: The election_description of this ElectionInfo.  # noqa: E501
        :type election_description: str
        :param election_id: The election_id of this ElectionInfo.  # noqa: E501
        :type election_id: int
        :param org_id: The org_id of this ElectionInfo.  # noqa: E501
        :type org_id: int
        :param start_time: The start_time of this ElectionInfo.  # noqa: E501
        :type start_time: str
        :param end_time: The end_time of this ElectionInfo.  # noqa: E501
        :type end_time: str
        :param anonymous: The anonymous of this ElectionInfo.  # noqa: E501
        :type anonymous: bool
        :param verified: The verified of this ElectionInfo.  # noqa: E501
        :type verified: bool
        :param public_results: The public_results of this ElectionInfo.  # noqa: E501
        :type public_results: bool
        """
        self.swagger_types = {
            'election_description': str,
            'election_id': int,
            'org_id': int,
            'start_time': str,
            'end_time': str,
            'anonymous': bool,
            'verified': bool,
            'public_results': bool
        }

        self.attribute_map = {
            'election_description': 'election_description',
            'election_id': 'election_id',
            'org_id': 'org_id',
            'start_time': 'start_time',
            'end_time': 'end_time',
            'anonymous': 'anonymous',
            'verified': 'verified',
            'public_results': 'public_results'
        }
        self._election_description = election_description
        self._election_id = election_id
        self._org_id = org_id
        self._start_time = start_time
        self._end_time = end_time
        self._anonymous = anonymous
        self._verified = verified
        self._public_results = public_results

    @classmethod
    def from_dict(cls, dikt) -> 'ElectionInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The election_info of this ElectionInfo.  # noqa: E501
        :rtype: ElectionInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def election_description(self) -> str:
        """Gets the election_description of this ElectionInfo.

        A text describing the purpose of the election  # noqa: E501

        :return: The election_description of this ElectionInfo.
        :rtype: str
        """
        return self._election_description

    @election_description.setter
    def election_description(self, election_description: str):
        """Sets the election_description of this ElectionInfo.

        A text describing the purpose of the election  # noqa: E501

        :param election_description: The election_description of this ElectionInfo.
        :type election_description: str
        """
        if election_description is None:
            raise ValueError("Invalid value for `election_description`, must not be `None`")  # noqa: E501

        self._election_description = election_description

    @property
    def election_id(self) -> int:
        """Gets the election_id of this ElectionInfo.


        :return: The election_id of this ElectionInfo.
        :rtype: int
        """
        return self._election_id

    @election_id.setter
    def election_id(self, election_id: int):
        """Sets the election_id of this ElectionInfo.


        :param election_id: The election_id of this ElectionInfo.
        :type election_id: int
        """

        self._election_id = election_id

    @property
    def org_id(self) -> int:
        """Gets the org_id of this ElectionInfo.

        The id of the organization holding the election  # noqa: E501

        :return: The org_id of this ElectionInfo.
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id: int):
        """Sets the org_id of this ElectionInfo.

        The id of the organization holding the election  # noqa: E501

        :param org_id: The org_id of this ElectionInfo.
        :type org_id: int
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def start_time(self) -> str:
        """Gets the start_time of this ElectionInfo.

        The time and date that an election will be open for polling  # noqa: E501

        :return: The start_time of this ElectionInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: str):
        """Sets the start_time of this ElectionInfo.

        The time and date that an election will be open for polling  # noqa: E501

        :param start_time: The start_time of this ElectionInfo.
        :type start_time: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self) -> str:
        """Gets the end_time of this ElectionInfo.

        The time and date that an election will be closed for polling  # noqa: E501

        :return: The end_time of this ElectionInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: str):
        """Sets the end_time of this ElectionInfo.

        The time and date that an election will be closed for polling  # noqa: E501

        :param end_time: The end_time of this ElectionInfo.
        :type end_time: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def anonymous(self) -> bool:
        """Gets the anonymous of this ElectionInfo.

        Whether this election is anonymous. True for anonymous, else non-anonymous  # noqa: E501

        :return: The anonymous of this ElectionInfo.
        :rtype: bool
        """
        return self._anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        """Sets the anonymous of this ElectionInfo.

        Whether this election is anonymous. True for anonymous, else non-anonymous  # noqa: E501

        :param anonymous: The anonymous of this ElectionInfo.
        :type anonymous: bool
        """
        if anonymous is None:
            raise ValueError("Invalid value for `anonymous`, must not be `None`")  # noqa: E501

        self._anonymous = anonymous

    @property
    def verified(self) -> bool:
        """Gets the verified of this ElectionInfo.

        Whether it is required for voters to verify their ID's in order to vote  # noqa: E501

        :return: The verified of this ElectionInfo.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified: bool):
        """Sets the verified of this ElectionInfo.

        Whether it is required for voters to verify their ID's in order to vote  # noqa: E501

        :param verified: The verified of this ElectionInfo.
        :type verified: bool
        """
        if verified is None:
            raise ValueError("Invalid value for `verified`, must not be `None`")  # noqa: E501

        self._verified = verified

    @property
    def public_results(self) -> bool:
        """Gets the public_results of this ElectionInfo.

        Whether the results of the election are open to the general public, or just within the org  # noqa: E501

        :return: The public_results of this ElectionInfo.
        :rtype: bool
        """
        return self._public_results

    @public_results.setter
    def public_results(self, public_results: bool):
        """Sets the public_results of this ElectionInfo.

        Whether the results of the election are open to the general public, or just within the org  # noqa: E501

        :param public_results: The public_results of this ElectionInfo.
        :type public_results: bool
        """
        if public_results is None:
            raise ValueError("Invalid value for `public_results`, must not be `None`")  # noqa: E501

        self._public_results = public_results
