# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.election import Election  # noqa: F401,E501
from swagger_server.models.org import Org  # noqa: F401,E501
from swagger_server.models.vote import Vote  # noqa: F401,E501
from swagger_server import util


class ElectionResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, org_info: Org=None, election_info: Election=None, user_votes: List[Vote]=None):  # noqa: E501
        """ElectionResults - a model defined in Swagger

        :param org_info: The org_info of this ElectionResults.  # noqa: E501
        :type org_info: Org
        :param election_info: The election_info of this ElectionResults.  # noqa: E501
        :type election_info: Election
        :param user_votes: The user_votes of this ElectionResults.  # noqa: E501
        :type user_votes: List[Vote]
        """
        self.swagger_types = {
            'org_info': Org,
            'election_info': Election,
            'user_votes': List[Vote]
        }

        self.attribute_map = {
            'org_info': 'org_info',
            'election_info': 'election_info',
            'user_votes': 'user_votes'
        }
        self._org_info = org_info
        self._election_info = election_info
        self._user_votes = user_votes

    @classmethod
    def from_dict(cls, dikt) -> 'ElectionResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The election_results of this ElectionResults.  # noqa: E501
        :rtype: ElectionResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def org_info(self) -> Org:
        """Gets the org_info of this ElectionResults.


        :return: The org_info of this ElectionResults.
        :rtype: Org
        """
        return self._org_info

    @org_info.setter
    def org_info(self, org_info: Org):
        """Sets the org_info of this ElectionResults.


        :param org_info: The org_info of this ElectionResults.
        :type org_info: Org
        """
        if org_info is None:
            raise ValueError("Invalid value for `org_info`, must not be `None`")  # noqa: E501

        self._org_info = org_info

    @property
    def election_info(self) -> Election:
        """Gets the election_info of this ElectionResults.


        :return: The election_info of this ElectionResults.
        :rtype: Election
        """
        return self._election_info

    @election_info.setter
    def election_info(self, election_info: Election):
        """Sets the election_info of this ElectionResults.


        :param election_info: The election_info of this ElectionResults.
        :type election_info: Election
        """
        if election_info is None:
            raise ValueError("Invalid value for `election_info`, must not be `None`")  # noqa: E501

        self._election_info = election_info

    @property
    def user_votes(self) -> List[Vote]:
        """Gets the user_votes of this ElectionResults.

        The votes cast. Optional and dependant on whether the election was anonymous  # noqa: E501

        :return: The user_votes of this ElectionResults.
        :rtype: List[Vote]
        """
        return self._user_votes

    @user_votes.setter
    def user_votes(self, user_votes: List[Vote]):
        """Sets the user_votes of this ElectionResults.

        The votes cast. Optional and dependant on whether the election was anonymous  # noqa: E501

        :param user_votes: The user_votes of this ElectionResults.
        :type user_votes: List[Vote]
        """

        self._user_votes = user_votes
