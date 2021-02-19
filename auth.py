import os
import ee
import oauth2client
from ee import oauth


def get_token():
    token = os.getenv("EE_TOKEN")
    # print(token)
    tokenEE = ee.oauth.request_token(token)
    """
    if token:
      tokenEE = oauth2client.client.OAuth2Credentials(
        None, 
        oauth.CLIENT_ID, 
        oauth.CLIENT_SECRET, 
        token,
        None, 
        'https://accounts.google.com/o/oauth2/token', 
        None
      )
    else:
      tokenEE = None
    """

    return tokenEE


def initialize():
    token = get_token()
    print(token)

    if token:
        ee.Initialize(token)
    else:
        url = ee.oauth.get_authorization_url()
        print("""
    Open 

    {} 

    in a brower tab and copy the code. Then create a file in this repository called '.env' (don't forget the leading dot). Inside that file write:

    EE_TOKEN=THE_CODE_YOU_JUST_COPIED

    """.format(url))