import os
import ee


def Initialize():
  credentials = get_persistent_credentials()
  ee.Initialize(credentials=credentials)


def get_persistent_credentials():
  """Read persistent credentials from ~/.config/earthengine.

  Raises EEException with helpful explanation if credentials don't exist.

  Returns:
    OAuth2Credentials built from persistently stored refresh_token
  """
  from google.oauth2.credentials import Credentials
  from ee.data import ee_exception

  try:
    # tokens = json.load(open(oauth.get_credentials_path()))
    # refresh_token = tokens['refresh_token']
    refresh_token = os.getenv("refresh_token")
    return Credentials(
        None,
        refresh_token=refresh_token,
        token_uri=ee.oauth.TOKEN_URI,
        client_id=ee.oauth.CLIENT_ID,
        client_secret=ee.oauth.CLIENT_SECRET,
        scopes=ee.oauth.SCOPES)
  except IOError:
    raise ee_exception.EEException(
        'Please authorize access to your Earth Engine account by '
        'running\n\nearthengine authenticate\n\nin your command line, and then '
        'retry.')
