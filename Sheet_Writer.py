from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import keys
from pprint import pprint
import datetime
import re
import csv


def main():
    #setup
    #The starting row
    i=2


    #infinite loop
    while True:
        studentID = input("swipe StudentID")
        #parse the student ID from the raw swiped data
        parsedID = re.search('\d+', str(studentID))
        currentDT = datetime.datetime.now()

        rowData = [str(currentDT), parsedID[0]]
        insert_New_Name (rowData)
        


        #temp = open(path+'\localBackup.csv','w+')%78718746601?;78718746601?+78718746601?

            

def insert_New_Name(rowDataArr):
    #writeValues= [[u'Zellea1', u'Zelleb1'],]
    writeValues= [[rowDataArr[0], rowDataArr[1]],]
    sheet_Write(keys.SheetId, writeValues)

    #write to backup sheet
    #check to see if localbackup file exists, if not make one
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    #open in the 'a' mode to append the file
    with open(path+'\localBackup.csv','a') as localBackup:

        csv_writer = csv.writer(localBackup, delimiter=',',lineterminator='\n',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([str(rowDataArr[0]),str(rowDataArr[1])])   


def sheet_Write(spreadsheet_ID, rowEntryArr):
    #call the token.pickle file which was generated using the quickstart code and is the api key
    with open('token.pickle', 'rb') as token:
       creds = pickle.load(token)

    #open and setup the api 
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    #add below the last value with data
    rowcount = service.spreadsheets().values().get(spreadsheetId = spreadsheet_ID, range ="A:A").execute()
    #throws error if sheet is empty. make the value 1 if this is true:
    try:
        rowcount = (len(rowcount.get("values")))+1

    except TypeError:
        print("no data found, writing to first row")
        rowcount = 1
    
    writeRange = "Sheet1!A"+str(rowcount)+":B"

    #what will be pasted into the sheet
    myBody = {u'range': writeRange, u'values': rowEntryArr, u'majorDimension': u'ROWS'}
    rangeOutput = writeRange
    response = sheet.values().update( spreadsheetId=spreadsheet_ID, range=rangeOutput, valueInputOption='RAW', body=myBody ).execute()


if __name__ == '__main__':
    main()

