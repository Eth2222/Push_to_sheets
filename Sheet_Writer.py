from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import keys
from pprint import pprint
import datetime

def main():
    #setup
    #The starting row
    i=2
    #infinite loop
    while True:
        studentID = input("swipe StudentID")
        #parse the student ID from the raw swiped data


        currentDT = datetime.datetime.now()

        rowData = [str(currentDT), studentID]
        insert_New_Name (rowData,i)
        i = i+1

def insert_New_Name(rowDataArr,i):
    #writeValues= [[u'Zellea1', u'Zelleb1'],]
    writeValues= [[rowDataArr[0], rowDataArr[1]],]
    writeRange = "Sheet1!A"+str(i)+":B"
    sheet_Write(keys.SheetId, writeValues, writeRange)
    #write to a local file for redundancy
    #check to see if file exists, if not make one

    #write to file

def sheet_Write(spreadsheet_ID, rowEntryArr, location):
    #call the token.pickle file which was generated using the quickstart code and is the api key
    with open('token.pickle', 'rb') as token:
       creds = pickle.load(token)
    #open and setup the api 
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    #what will be pasted into the sheet
    myBody = {u'range': location, u'values': rowEntryArr, u'majorDimension': u'ROWS'}
    rangeOutput = location
    response = sheet.values().update( spreadsheetId=spreadsheet_ID, range=rangeOutput, valueInputOption='RAW', body=myBody ).execute()


if __name__ == '__main__':
    main()


