from datetime import date
from datetime import time
from datetime import datetime
from data.DayCalendar import DayCalendar
from data.SimpleCalendar import SimpleCalendar
from data.Event import Event

import httplib2
import os
import sys

from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools



class CalendarManager():
    def __init__(self,client_secrets,cal_list=[]):
        global calendar_list
        calendar_list = cal_list
        CLIENT_SECRETS = client_secrets
        FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
                                              scope=[
                                                     'https://www.googleapis.com/auth/calendar',
                                                     'https://www.googleapis.com/auth/calendar.readonly',
                                                     ],
                                              message=tools.message_if_missing(CLIENT_SECRETS))
        storage = file.Storage('sample.dat')
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(FLOW, storage, None)
        http = httplib2.Http()
        http = credentials.authorize(http)
        global service
        service = discovery.build('calendar', 'v3', http=http)
        try:
            #code here
            self.start(service)
        except client.AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")
    
    def addCalendar(self,calendar):
        if (calendar is DayCalendar) or (calendar is SimpleCalendar):
            if self.getCalendar(calendar) == None:
                global calendar_list
                calendar_list.append(calendar)
                return True
            else:
                return False
        else:
            return False
            
    def getCalendar(self,target,indexPlease=False):
        for index, cal in enumerate(calendar_list):
            if target == cal:
                if indexPlease:
                    return index,cal
                else:
                    return cal
        return None
        
    def addEvent(self,calendar,event):
        cal = self.getCalendar(calendar,False)
        cal.addEvent(event)
    
    def addEvents(self,calendar,event_list):
        cal = self.getCalendar(calendar)
        cal.addEvents(event_list)
    
    def removeCalendar(self,target):
        cal,ind = self.getCalendar(target,True)
        calendar_list.remove(ind)
        
    def start(self,cal_api_service):
        page_token = None
        while True:
            calendar_list = cal_api_service.calendarList().list(maxResults=100,
                                                        minAccessRole='reader',
                                                        pageToken=page_token,
                                                        ).execute()
            for calendar_list_entry in calendar_list['items']:
                temp_name = calendar_list_entry['summary']
                print temp_name
                temp_id = calendar_list_entry['id']
                print temp_id
                filename = os.path.join(os.path.dirname(__file__)+'/manager/',
                                        +str(temp_name)+'.cal')
                #filename = '/manager/cal_'+str(temp_name)+'.txt'
                mode = 'w' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
                file1 = open(filename,mode)
                print file1
                file1.write('__calendar__')
                file1.write(str(temp_name)+"\n")
                file1.write(str(temp_id)+"\n")
                file1.write('__events__')
                event_list = service.events().list(calendarId=calendar_list_entry['id'],
                                                       singleEvents=True,
                                                       orderBy='startTime').execute()
                for event in event_list['items']:
                    try:
                        print event['summary']
                        write_str = 'name:{'+(event['summary']+'          ')[0:10]+'} id:{'+(str(event['id']))+'} \n'
                        file1.write(write_str)
                    except KeyError,ke:
                        print "Key Error "+str(ke)
                file1.close()

            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
    def update(self,cal_api_service):
        for cal in calendar_list:
            event_list = cal_api_service.events().list(calendarID=cal.online_id,
                                                       orderBy='startTime',
                                                       minAccessRole='reader'
                                                        ).execute()
            for event in event_list:
                local_event = Event(event_name=event['summary'],
                                    online_id=event['id'],
                                    event_date=event['start']['date'],
                                    start_time=event['start']['datetime'],
                                    end_time=event['end']['datetime'])
                cal.addEvent(local_event)
    
    def printCalendar(self,cal_name):
        for cal in calendar_list:
            if cal.name == cal_name:
                print str(cal.name)
                if cal is SimpleCalendar:
                    print "Simple Calendar"
                elif cal is DayCalendar:
                    print cal.toString()
                    
def test():
    #add the file location
    secret_location = os.path.join(os.path.dirname('..'), 'client_secrets.json')
    cm = CalendarManager(client_secrets=secret_location)
    
if __name__=='__main__':
    test()