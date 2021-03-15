import connexion
import six
from werkzeug.exceptions import NotFound, Unauthorized, InternalServerError

from src.constants_enums.privileges import PrivilegeLevels
from src.endpoint_controllers.org_controller import get_org
from src.endpoint_controllers.org_elections_controller import get_election, get_election_with_results
from swagger_server.models import Vote, Choice, Org
from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server import util
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import *


def get_votes(election_id):
    votes_tuple_list = db.get_election_votes(election_id)
    votes = []
    current_token = ""
    current_location = ""
    current_timestamp = ""
    current_first_name = ""
    current_last_name = ""
    current_choices = []
    for choice_tuple in votes_tuple_list:
        voting_token = choice_tuple[7]
        if voting_token != current_token:
            vote = Vote(current_first_name, current_last_name, choices=current_choices, time_stamp=current_timestamp,
                        location=current_location)
            votes.append(vote)
            current_token = voting_token
            current_first_name = choice_tuple[0]
            current_last_name = choice_tuple[1]
            current_location = ""
            current_timestamp = choice_tuple[6]
            current_choices = []
        question_id = choice_tuple[2]
        option_id = choice_tuple[4]
        order_position = choice_tuple[5]
        choice = Choice(question_id, option_id, order_position)
        current_choices.append(choice)
    return votes[1:]


def asses_auth_for_election(org_id, uid):
    privilege_tuple = db.get_privilege(org_id, uid)
    if privilege_tuple is None:
        raise Unauthorized("You are not authorized to access the requested election")
    privilege = privilege_tuple[0]
    if privilege < PrivilegeLevels.MEMBER:
        raise Unauthorized("You are not authorized to access the requested election")


def get_election_results(election_id, token_info):  # noqa: E501
    """Get election voting results

    Get the voting results for an election. If the election is private, and the user is not a member of the org, then will respond 401: Unauthorized If there are several results for the same election, the latest version will be  # noqa: E501


    :rtype: ElectionResults
    """
    election = get_election_with_results(election_id)

    if not election.public_results:
        asses_auth_for_election(election.org_id, token_info[JwtTokenKeys.UID])

    votes = get_votes(election_id)

    user_org = get_org(election.org_id)
    org = Org(user_org.org_id, user_org.name)

    if org is None:
        raise NotFound("The organization info for this election was not found")

    if election.anonymous:
        result_model = ElectionResults(org_info=org, election_info=election)
        return result_model
    result_model = ElectionResults(user_votes=votes, org_info=org, election_info=election)
    return result_model
