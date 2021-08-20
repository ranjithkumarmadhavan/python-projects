#reference - https://developers.google.com/sheets/api/quickstart/python
import gspread
from google.oauth2 import service_account
from pprint import pprint
from datetime import datetime

SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "creds.json"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.with_subject('support@luxliving.co')
client = gspread.authorize(delegated_credentials)

slots_sheet = client.open("Alexa Lux Living Skill")
slots_sheet = slots_sheet.worksheet("Sheet1")

# get all records
data = slots_sheet.get_all_records()
print(data)
