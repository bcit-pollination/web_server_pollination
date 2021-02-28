# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.question_results import QuestionResults  # noqa: F401,E501
from swagger_server.models.vote import Vote  # noqa: F401,E501
from swagger_server import util


class PrivateElectionResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, question_results: List[QuestionResults]=None, user_votes: List[Vote]=None):  # noqa: E501
        """PrivateElectionResults - a model defined in Swagger

        :param question_results: The question_results of this PrivateElectionResults.  # noqa: E501
        :type question_results: List[QuestionResults]
        :param user_votes: The user_votes of this PrivateElectionResults.  # noqa: E501
        :type user_votes: List[Vote]
        """
        self.swagger_types = {
            'question_results': List[QuestionResults],
            'user_votes': List[Vote]
        }

        self.attribute_map = {
            'question_results': 'question_results',
            'user_votes': 'user_votes'
        }
        self._question_results = question_results
        self._user_votes = user_votes

    @classmethod
    def from_dict(cls, dikt) -> 'PrivateElectionResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The private_election_results of this PrivateElectionResults.  # noqa: E501
        :rtype: PrivateElectionResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def question_results(self) -> List[QuestionResults]:
        """Gets the question_results of this PrivateElectionResults.

        The results for each question posed  # noqa: E501

        :return: The question_results of this PrivateElectionResults.
        :rtype: List[QuestionResults]
        """
        return self._question_results

    @question_results.setter
    def question_results(self, question_results: List[QuestionResults]):
        """Sets the question_results of this PrivateElectionResults.

        The results for each question posed  # noqa: E501

        :param question_results: The question_results of this PrivateElectionResults.
        :type question_results: List[QuestionResults]
        """
        if question_results is None:
            raise ValueError("Invalid value for `question_results`, must not be `None`")  # noqa: E501

        self._question_results = question_results

    @property
    def user_votes(self) -> List[Vote]:
        """Gets the user_votes of this PrivateElectionResults.

        The votes cast. Optional and dependant on whether the election was anonymous  # noqa: E501

        :return: The user_votes of this PrivateElectionResults.
        :rtype: List[Vote]
        """
        return self._user_votes

    @user_votes.setter
    def user_votes(self, user_votes: List[Vote]):
        """Sets the user_votes of this PrivateElectionResults.

        The votes cast. Optional and dependant on whether the election was anonymous  # noqa: E501

        :param user_votes: The user_votes of this PrivateElectionResults.
        :type user_votes: List[Vote]
        """

        self._user_votes = user_votes
