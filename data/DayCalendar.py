from datetime import time
from datetime import date
from datetime import datetime
from data.Token import Token
from data.Event import Event
from data.Day import Day

#A Calendar is a list of events

class DayCalendar():
    def __init__(self,calendar_name="",id_='',list_of_event=[]):
        global name
        name = calendar_name
        global online_id
        online_id = id_
        self.addEvents(list_of_event)
    
    def addEvents(self,list_of_events):
        if isinstance(list_of_events,list):
            for e in list_of_events:
                self.addEvent(e)
            return True
        else:
            return False
    
    def addEvent(self,item):
        global event_list
        if item is Event:
            add_day = self.getDay(item.day)
            add_day.addEvent(item)
    
    def addDay(self,item):
        global day_list
        if item is Event:
            day = item.day
            add_day = self.getDay(day)
            add_day.addEvent(item)
        elif item is Day:
            day_list.append(item)
            day_list.sort(key=Day.earlyTime())
        else:
            return False
    
    def getDay(self,item):
        if item is Event:
            day = item.day
            global day_list
            search_result = DayCalendar.day_binary_search(day,day_list,0,len(day_list))
            if search_result != None:
                return search_result
            else:
                self.addDay(day)
                return day
        elif item is Day:
            day = item
            search_result = DayCalendar.day_binary_search(day,day_list,0,len(day_list))
            if search_result != None:
                return search_result
            else:
                self.addDay(day)
                return DayCalendar.day_binary_search(day, day_list, 0, len(day_list))
        else:
            return None
    
    def day_binary_search(self,target,target_list,start_index,end_index):
        length = end_index-start_index
        if length < 1:
            return None
        elif length == 1:
            if target.day==target_list[start_index].day:
                return start_index
            else:
                return None
        else:
            midpoint = (start_index+end_index)//2
            if target.day==target_list[midpoint].day:
                return midpoint
            elif target.day<target_list[midpoint].day:
                return DayCalendar.day_binary_search(target,target_list,start_index,midpoint)
            else:
                return DayCalendar.day_binary_search(target,target_list,midpoint,end_index)    
        
    
    def getEvent(self,target):
        pass
    
    def toString(self):
        str = ''
        for day in day_list:
            for event in day.event_list:
                str = (str+" - "+(str(event.name)+'          ')[0,10]+
                       (str(event.online_id)+'          ')[0,10]+
                       (str(event.s_time)+'          ')[0,10]+
                       '/n')
        return str