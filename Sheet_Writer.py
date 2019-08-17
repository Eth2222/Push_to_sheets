from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import keys
from pprint import pprint

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = keys.SheetId
SAMPLE_RANGE_NAME = 'A1:B5'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))
"""
    writeValues= [[u'Zellea1', u'Zelleb1'],]
    writeRange = "Sheet1!A15:C"
    sheet_Write(keys.SheetId, writeValues, writeRange)

def sheet_Write(spreadsheet_ID, rowEntryArr, location):
    with open('token.pickle', 'rb') as token:
       creds = pickle.load(token)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    myBody = {u'range': location, u'values': rowEntryArr, u'majorDimension': u'ROWS'}
    rangeOutput = location
    response = sheet.values().update( spreadsheetId=spreadsheet_ID, range=rangeOutput, valueInputOption='RAW', body=myBody ).execute()

if __name__ == '__main__':
    main()
