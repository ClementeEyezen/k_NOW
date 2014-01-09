####################################
# Test application for Calendar API.
# Usage:
#   $ python gtask_list-get_tester.py
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

from data.Task import Task
from data.Task import TaskList
from data.Task import TaskManager 


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
      'https://www.googleapis.com/auth/tasks',
      'https://www.googleapis.com/auth/tasks.readonly',
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
    service = discovery.build('tasks', 'v1', http=http)

    try:
        print "Success! Now add code here."
        
        page_token = None
        while True:
            filename = 'task_list_test.txt'
            mode = 'w' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
            file1 = open(filename,mode)
            print file1
            tasklists = service.tasklists().list(maxResults=100,
                                                pageToken=page_token,
                                                ).execute()
            for task_list_entry in tasklists['items']:
                temp_name = task_list_entry['title']
                print temp_name
                temp_id = task_list_entry['id']
                print temp_id
                file1.write('__taskList__\n')
                file1.write(str(temp_name)+"\n")
                file1.write(str(temp_id)+"\n")
                file1.write('__tasks__\n')
                task_list = service.tasks().list(tasklist=task_list_entry['id'],
                                                 maxResults=100,
                                                 showCompleted=True
                                                 ).execute()
                for task in task_list['items']:
                    try:
                        print task['title']
                        write_str = 'task:{'+(task['title']+'          ')[0:10]+'} id:{'+(str(task['id']))+'} \n'
                        file1.write(write_str)
                    except KeyError,ke:
                        print "Key Error "+str(ke)
                 
            
#            page_token = calendar_list.get('nextPageToken')
#            if not page_token:
#                break
            file1.close()
            break
        print "Still a success. Code added"
        #from here, now that I can access GCal from here, I now can add code to talk to the API, get info

    except client.AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")

if __name__ == '__main__':
  main(sys.argv)
