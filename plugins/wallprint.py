from googleapiclient.discovery import build
from google.oauth2 import service_account
from random import choice
from plugins.config import driveid

SCOPES = ['https://www.googleapis.com/auth/drive']  # This is the scope to access drive information
SERVICE_ACCOUNT_FILE = 'src/edelia.json'  # This is my service account file you need to create one with GCP Console

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def randomwall():
    DRIVE = build('drive', 'v3', credentials=credentials)  # This is my discovery API Drive
    page_token = None
    temp = []
    while True:
        response = DRIVE.files().list(q="'{}' in parents".format(driveid),
                                      spaces='drive',
                                      pageSize=100,
                                      fields='nextPageToken, files(id, description)',
                                      pageToken=page_token).execute()
        for file in response.get('files', []):
            temp.append([file.get('id'), file.get('description')])
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return choice(temp)  # We return random choice in temp, so we return id, description in type array
