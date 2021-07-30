#reference - https://developers.google.com/sheets/api/quickstart/python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

slots_sheet = client.open("Daily log sheet").worksheet("logs")

def lambda_handler(event,context):
    # get all records
    data = slots_sheet.get_all_records()
    print(data)

    # get row 2 record
    row = slots_sheet.row_values(2)
    print(row)

    # get column 2 records
    col = slots_sheet.col_values(2)
    print(col)

    # get 1st row 2nd column value
    cell = slots_sheet.cell(1,2).value
    print(cell)

    # insert a record at the 3rd row
    currentDate = str(datetime.utcnow().date())
    # insert_row = [currentDate,1,"learnt to access google sheets using python"]
    # slots_sheet.insert_row(insert_row,3)

    # delete the record at the 3rd row
    # slots_sheet.delete_rows(3)

    return data

pprint(lambda_handler("",""))