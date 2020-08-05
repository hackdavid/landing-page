import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def add_data(name,country,email):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("client.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("marketing").sheet1  # Open the spreadhseet
    # data=sheet.get_all_records()
    # print(data)
    insertRow = [name,country,email]
    sheet.append_row(insertRow)  # Insert the list as a row at index 4
