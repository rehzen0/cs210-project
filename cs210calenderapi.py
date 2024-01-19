#!/usr/bin/env python
# coding: utf-8

# In[10]:


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os.path
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    creds = None
    # Update the path to your client secret file
    client_secret_file = 'C:/Users/berke/Downloads/client_secret_900848127428-954qjap2p4li5t4p5quda3mfd76lf6t7.apps.googleusercontent.com.json'
    
    # The file token.pickle stores the user's access and refresh tokens.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def main():
    service = get_calendar_service()
    # Calculate the date 3 months ago from now
    now = datetime.datetime.utcnow()
    three_months_ago = (now - datetime.timedelta(days=90)).isoformat() + 'Z'

    print('Getting events from the last 3 months')
    events_result = service.events().list(calendarId='primary', timeMin=three_months_ago, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

if __name__ == '__main__':
    main()


# In[ ]:




