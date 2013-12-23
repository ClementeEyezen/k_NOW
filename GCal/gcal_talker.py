"""Command-line skeleton application for Calendar API.
Usage:
  $ python gcal_talker.py

You can also get help on all the command-line flags the program understands
by running:

  $ python sample.py --help

"""

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
            filename = 'cal_write_'+str(datetime.now())+'.txt'
            mode = 'w' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
            file1 = open(filename,mode)
            print file1
            calendar_list = service.calendarList().list(maxResults=100,
                                                        minAccessRole='reader',
                                                        pageToken=page_token,
                                                        ).execute()
            for calendar_list_entry in calendar_list['items']:
                file1.write((str(calendar_list_entry['summary'])+'          ')[0:10]+'   '+str(calendar_list_entry['id'])+"\n")
                print calendar_list_entry['summary']
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
