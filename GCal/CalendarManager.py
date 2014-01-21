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
        #Set up authorization
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
        #set the calendar access service
        global __service__
        __service__ = discovery.build('calendar', 'v3', http=http)
        try:
            #code here
            #start up by writing all of the calendar files
            self.start(__service__)
            global __last_update__
            __last_update__ = str(datetime.now())
            print 'updated time time time :'+str(__last_update__)
            __last_update__ = __last_update__.replace(" ", "T")
            __last_update__ = __last_update__[0:len(__last_update__)-3]
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
        
    def start(self,cal_api_service,ignore_existing=False):
        existing_cal_files = False
        directory = os.path.dirname(__file__)+'/manager/'
        #print directory
        for root,dirs,files in os.walk(directory):
            for file1 in files:
                if file1.endswith(".cal"):
                    #try:
                    file1 = os.path.join(os.path.dirname(__file__)+'/manager/',
                                        file1)
                    #print file1
                    if True:
                        f=open(file1, 'r')
                        self.addCalendar(self.calFromFile(f))
                        existing_cal_files = True
                        f.close()
                    #except IOError:
                    #    print 'Error reading file '+str(file1)
                    #    print ' '+str(IOError.message)
        if existing_cal_files:
            print 'files already exist'
        page_token = None
        #while there aren't existing files, or if asked to ignore said files
        while not existing_cal_files or ignore_existing:
            calendar_list = cal_api_service.calendarList().list(maxResults=100,
                                                        minAccessRole='reader',
                                                        pageToken=page_token,
                                                        ).execute()
            for calendar_list_entry in calendar_list['items']:
                self.addCalendar(calendar_list_entry)
                temp_name = calendar_list_entry['summary']
                #print temp_name
                temp_id = calendar_list_entry['id']
                #print temp_id
                filename = os.path.join(os.path.dirname(__file__)+'/manager/',
                                        str(temp_name)+'.cal')
                filename = str(filename).replace(" ", '_')
                mode = 'w' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
                file1 = open(filename,mode)
                #print file1
                file1.write('__calendar__')
                file1.write('name '+str(temp_name)+"\n")
                file1.write('id   '+str(temp_id)+"\n")
                file1.write('__events__')
                event_list = cal_api_service.events().list(calendarId=calendar_list_entry['id'],
                                                       singleEvents=True,
                                                       orderBy='startTime').execute()
                for event in event_list['items']:
                    try:
                        #print event['summary']
                        write_str = 'name:{'+str(event['summary'])+'} id:{'+(str(event['id']))+'} \n'
                    except KeyError,ke:
                        print "Key Error "+str(ke)
                        write_str = 'default'
                    file1.write(write_str)
                file1.close()

            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        global __last_update__
        __last_update__ = str(datetime.now())
        __last_update__ = __last_update__.replace(' ','T')
        __last_update__ = __last_update__[0:len(__last_update__)]
        print 'updated time time time :'+str(__last_update__)
    
    def calFromFile(self,file_):
        count = 0
        try:
            file1 = open(file_,'r')
        except:
            file1 = file_
        meta_cal_mode = False
        temp_name = ''
        temp_id = ''
        list_of_events = []
        for line in file1.readlines():
            if line == '__calendar__':
                meta_cal_mode = True
            elif line == '__events__':
                meta_cal_mode = False
            if meta_cal_mode:
                if line[0:5] == 'name ':
                    temp_name = line[5:len(line)]
                elif line[0:5] == 'id   ':
                    temp_id = line[5:len(line)] 
            else:
                #create events and add to calendar
                try:
                    print 'line processed'+str(self.processLine(line).getName())
                    list_of_events.append(self.processLine(line))
                except AttributeError, ae:
                    print 'aterror '+str(ae)
                    count = count + 1
                    print 'count = '+str(count)
            #lol = 
            #print str(list_of_events)
            #lol.addEvents(list_of_events)
            #print 'lolcats'+str(lol.getName())
        #if temp_name != '' and temp_id != '':
        self.addCalendar(SimpleCalendar(name_=temp_name,id_=temp_id,list_of_events=list_of_events))
        print 'cal list '+str(calendar_list)
        print 'lol'
        
        file1.close()
    
    def update(self,cal_api_service):
        '''for cal in calendar_list:
            #global __last_updated__
            event_list = cal_api_service.events().list(calendarID=cal.online_id,
                                                       orderBy='startTime',
                                                       minAccessRole='reader'#,
                                                       #updatedMin = __last_updated__
                                                        ).execute()
            
            for event in event_list:
                #local_event = Event(event_name=event['summary'],
                #                    online_id=event['id'],
                #                    event_date=event['start']['date'],
                #                    start_time=event['start']['datetime'],
                #                    end_time=event['end']['datetime'])
                cal.addEvent(Event(event_name=event['summary'],
                                    online_id=event['id'],
                                    event_date=event['start']['date'],
                                    start_time=event['start']['datetime'],
                                    end_time=event['end']['datetime']))
                #del local_event
            print '-----------------Test Line-----------------'
            for event in cal.event_list:
                print event.id_
            '''
        page_token = None
        while True:
            calendar_list = cal_api_service.calendarList().list(#maxResults=100,
                                                        minAccessRole='reader',
                                                        pageToken=page_token#,
                                                        ).execute()
            for calendar_list_entry in calendar_list['items']:
                self.addCalendar(calendar_list_entry)
                temp_name = calendar_list_entry['summary']
                #print temp_name
                temp_id = calendar_list_entry['id']
                #print temp_id
                filename = os.path.join(os.path.dirname(__file__)+'/manager/',
                                        str(temp_name)+'.cal')
                filename = str(filename).replace(" ", '_')
                mode = 'a' #'w' for write, 'a' for append, 'r' for read, 'r+' for read/write
                file1 = open(filename,mode)
                #print file1
                #file1.write('__calendar__')
                #file1.write('name '+str(temp_name)+"\n")
                #file1.write('id   '+str(temp_id)+"\n")
                file1.write('__updated__')
                file1.write(str(datetime.now())+'\n')
                file1.write('__events__\n')
                event_list = cal_api_service.events().list(calendarId=calendar_list_entry['id'],
                                                           singleEvents=True,
                                                           orderBy='startTime',
                                                           updatedMin = __last_update__
                                                           ).execute()
                for event in event_list['items']:
                    try:
                        #print event['summary']
                        write_str = 'name:{'+str(event['summary'])+'} id:{'+(str(event['id']))+'} \n'
                    except KeyError,ke:
                        print "Key Error "+str(ke)
                        write_str = 'default'
                    file1.write(write_str)
                file1.close()

            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        global __last_update__
        __last_update__ = str(datetime.now())
        __last_update__ = __last_update__.replace(" ", "T")
        __last_update__ = __last_update__[0:len(__last_update__)-3]
            
    
    def printCalendar(self,cal_name):
        for cal in calendar_list:
            if cal.name == cal_name:
                print str(cal.name)
                if cal is SimpleCalendar:
                    print "Simple Calendar"+cal.name
                elif cal is DayCalendar:
                    print cal.toString()
    def processLine(self,event_line):
        if not isinstance(event_line, str):
            pass
        else:
            if event_line[0:6] == 'name:{':
                summary_start_index = 6
                summary_end_index = str(event_line[6:len(event_line)]).find('}')+6
                if event_line[summary_end_index:summary_end_index+6] == '} id:{':
                    id_start_index = summary_end_index+7
                    id_end_index = str(event_line[summary_end_index+1:len(event_line)]).find('}')+summary_end_index+1
                    print 'name = '+event_line[summary_start_index:summary_end_index]
                    print 'id   = '+event_line[id_start_index:id_end_index]
                    return Event(event_name=event_line[summary_start_index:summary_end_index],id_=event_line[id_start_index:id_end_index])
    def printAllCalendars(self):
        print calendar_list
        for cal_obj in calendar_list:
            print self.printCalendar(cal_obj)
    
    def getService(self):
        return __service__
                    
def test():
    #add the file location
    secret_location = os.path.join(os.path.dirname('..'), 'client_secrets.json')
    cm = CalendarManager(client_secrets=secret_location)
    print 'begin run update'
    cm.update(cm.getService())
    print 'didn\'t clear'
    print '\n\n\n\n\n\n'
    
if __name__=='__main__':
    test()