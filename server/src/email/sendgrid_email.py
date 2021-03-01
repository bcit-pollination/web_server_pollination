import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import time

import six
from jose import jwt, JWTError
from werkzeug.exceptions import Unauthorized

JWT_ISSUER = 'pollination.live'
JWT_SECRET = 'SM94J7p0UYUWfw6RgUC1uqIyg2Mith6JV9dTTCBnYW0hZnyGp0e55x1mKmr1t9S'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def _encrypt_user_info(org_id, user_org_id, user_email):
    """
    Generate a JWT from a given user_id.
    """
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "org_id": str(org_id),
        "email": user_email
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_user_info(token):
    """
    Decode a JWT into object.

    :throws: Unauthorized exception if invalid token
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp() -> int:
    return int(time.time())


def send_registration_email(org_name, org_id, user_email):
    """
    Send a registration email.

    :param: org_id The id of the organization within the pollination system
    :param: user_org_id The id of the user within the organization
    :param: user_email The email of the user
    :throws: RuntimeError if the response status is not 2xx
    """
    encrypted_data = _encrypt_user_info(org_id, user_email)
    message = Mail(
        from_email='registration@pollination.live',
        to_emails=user_email,
        subject=f'Pollination: invitation to register at {org_name}',
        html_content=f'''
        <h1>You have been invited to join: {org_name}</h1>
        To accept follow the link below:<br>
        https://pollination.live/api/org/users/invite/accept?encrypted_data={encrypted_data}''')
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    if response.status_code < 200 or 299 < response.status_code:
        raise RuntimeError
