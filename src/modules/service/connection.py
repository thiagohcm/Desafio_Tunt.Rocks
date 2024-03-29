import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
import logging

logger = logging.getLogger()


class Client:
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.creds = None
        self.service = None

    # Load the credentials from service account file
    def get_credentials(self):
        client_secret_filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                              'client_credentials', 'credentials.json')
        try:
            self.creds = service_account.Credentials.from_service_account_file(client_secret_filepath,
                                                                               scopes=self.SCOPES)
            logger.info('Credentials successfully loaded')
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    # Call the Sheets API to build the service
    def call_api(self):
        try:
            self.service = build("sheets", "v4", credentials=self.creds, cache_discovery=False)
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error
