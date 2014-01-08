####################################
# Test application for Calendar API.
# Usage:
#   $ python gcal_event_tester.py
####################################

import argparse
import httplib2
import os
import sys

from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

from datetime import time
from datetime import datetime
from datetime import timedelta


# Parser for command-line arguments.
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])


# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret. You can see the Client ID
# and Client secret on the APIs page in the Cloud Console:
# <https://cloud.google.com/console#/project/921888933653/apiui>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
  scope=[
      'https://www.googleapis.com/auth/calendar',
      'https://www.googleapis.com/auth/calendar.readonly',
    ],
    message=tools.message_if_missing(CLIENT_SECRETS))


def main(argv):
    # Parse the command-line flags.
    flags = parser.parse_args(argv[1:])
    # If the credentials don't exist or are invalid run through the native client
    # flow. The Storage object will ensure that if successful the good
    # credentials will get written back to the file.
    storage = file.Storage('sample.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)
    
    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Construct the service object for the interacting with the Calendar API.
    service = discovery.build('calendar', 'v3', http=http)

    try:
        print "Success! Now add code here."
        
        page_token = None
        while True:
            calendar_list = service.calendarList().list(maxResults=100,
                                                        minAccessRole='reader',
                                                        pageToken=page_token,
                                                        ).execute()
            for calendar_list_entry in calendar_list['items']:
                if calendar_list_entry['summary']=='[k]NOW Cal':
                    temp_name = calendar_list_entry['summary']
                    print temp_name
                    temp_id = calendar_list_entry['id']
                    print temp_id
                    start_time = (str(datetime.now())).replace(' ','T')
                    start_time = start_time[0:len(start_time)-3]+'-05:00'
                    print 'start = ' + start_time
                    end_time = (str(datetime.now()+timedelta(0,3600))).replace(' ','T')
                    end_time = end_time[0:len(end_time)-3]+'-05:00'
                    print 'end   = ' + end_time
                    event = {
                             'summary': 'TestEven1',
                             'location': 'Somewhere surprisingly close',
                             'start': {
                                       'dateTime': start_time
                                       },
                             'end': {
                                     'dateTime': end_time
                                     },
                             'attendees': [
                                           {
                                            'email': 'mobile.wbaskin@gmail.com'
                                            #add self for the following reason
                                            #when my email is added as an attendee, it will give me the option
                                            # to say yes, no or maybe to events, so it will automatically get 
                                            # feedback on where I am, and the AI's predictions for my events
                                            },
                                           #Other attendee's data...
                                          ],
                             'description': 'At the time this test was run,\nthis event was created,\nand will last for one hour'
                            }
                    try:
                        sent_event = service.events().insert(calendarId=temp_id, body=event).execute()
                    except:
                        print 'Error while setting event'
                    
            filename = 'cal_event-set_test.txt'
            mode = 'w' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
            file1 = open(filename,mode)
            print file1
            file1.write('__calendar__'+'\n')
            file1.write(str(temp_name)+"\n")
            file1.write(str(temp_id)+"\n")
            file1.write('__events__\n')
            event_list = service.events().list(calendarId=temp_id,
                                                       singleEvents=True,
                                                       orderBy='startTime').execute()
            for event in event_list['items']:
                try:
                    print event['summary']+' '+event['id']
                    write_str = 'name:{'+(event['summary']+'          ')[0:10]+'} id:{'+(str(event['id']))+'} \n'
                    file1.write(write_str)
                except KeyError,ke:
                    print "Key Error "+str(ke)
            file1.close()
                 
            
#            page_token = calendar_list.get('nextPageToken')
#            if not page_token:
#                break
            break        
        print "Still a success. Code added"
        #from here, now that I can access GCal from here, I now can add code to talk to the API, get info

    except client.AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


# For more information on the Calendar API you can visit:
#
#   https://developers.google.com/google-apps/calendar/firstapp
#
# For more information on the Calendar API Python library surface you
# can visit:
#
#   https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/
#
# For information on the Python Client Library visit:
#
#   https://developers.google.com/api-client-library/python/start/get_started
if __name__ == '__main__':
  main(sys.argv)
