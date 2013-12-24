from datetime import date
from datetime import time
from datetime import datetime
from data import DayCalendar
from data import SimpleCalendar
from data import Event


class CalendarManager():
    def __init__(self,cal_list=[]):
        global calendar_list
        calendar_list = cal_list
    
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