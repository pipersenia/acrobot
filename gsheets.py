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
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Acronyms").sheet1
    # Extract and print all of the values
    return sheet.get_all_records()

def main():
    data = [{'Acronym': 'ASR', 'Fullform': 'AS Roma'}, {'Acronym': 'INT', 'Fullform': 'Inter Milan'}, {'Acronym': 'ACM', 'Fullform': 'AC Milan'}, {'Acronym': 'MAADU', 'Fullform': 'Maadhav'}]
    master = {}
    for rec in data:
        master[rec['Acronym']] = rec['Fullform']
    print(master)

if __name__ == '__main__':
    main()
    client = connect()
    print(get_records(client))
