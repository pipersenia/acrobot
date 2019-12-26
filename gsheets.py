import gspread
from oauth2client.service_account import ServiceAccountCredentials


SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SECRETS_FILE = 'client_secret.json'


def connect():
    # use creds to create a client to interact with the Google Drive API
    creds = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPE)
    client = gspread.authorize(creds)
    return client


def get_records(client):
    sheet = client.open("Acronyms").sheet1
    # Extract and print all of the values
    return sheet.get_all_records()
