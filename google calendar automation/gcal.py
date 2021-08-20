from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from datetime import datetime,timedelta

scope = ["https://www.googleapis.com/auth/calendar"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
API_NAME = 'calendar'
API_VERSION = 'v3'

# google calendar service
service = build(API_NAME, API_VERSION, credentials=creds)

calendar_id = "YOUR_CALENDAR_ID"

time_min = datetime.now()
time_max = time_min + timedelta(hours=20)


# freebusy
payload = {
    "timeMin": time_min.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
    "timeMax": time_max.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
    # "timeZone": timezone,
    "items": [{ "id": calendar_id }],
}
print(payload)

freebusy = service.freebusy().query(body=payload).execute()

print(freebusy)

#insert
time_min = datetime.now()
time_max = time_min + timedelta(hours=1)
event = {
    'summary': 'test summary',
    'description': "description test",
    'start': {
        'dateTime': time_min.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
        # 'timeZone': timezone,
    },
    'end': {
        'dateTime': time_max.strftime("%Y-%m-%dT%H:%M:%S+05:30"),
        # 'timeZone': timezone,
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'popup', 'minutes': 30},
        ],
    },
}
print(service.events().insert(calendarId=calendar_id, body=event).execute())

#delete
events = service.events().list(calendarId=calendar_id,timeMin=time_min.strftime("%Y-%m-%dT%H:%M:%S+05:30"),timeMax=time_max.strftime("%Y-%m-%dT%H:%M:%S+05:30")).execute()
print(events)
for reservation in events["items"]:
    print(service.events().delete(calendarId=calendar_id,eventId = reservation["id"]).execute())
    