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
    data = slots_sheet.get_all_records()
    print(data)

    row = slots_sheet.row_values(2)
    print(row)
    col = slots_sheet.col_values(2)
    print(col)
    cell = slots_sheet.cell(1,2).value
    print(cell)
    currentDate = str(datetime.utcnow().date())
    print(currentDate)

    # insert_row = [currentDate,1,"learnt to access google sheets using python"]
    # slots_sheet.insert_row(insert_row,3)

    # slots_sheet.delete_rows(3)

    return data

pprint(lambda_handler("",""))