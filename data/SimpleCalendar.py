from data.Event import Event

class SimpleCalendar():
    def __init__(self,name_="",id_='',list_of_events=[]):
        global event_list
        event_list = []
        self.addEvents(list_of_events)
        global name
        name = name_
        global __id__
        __id__ = id_

    def addEvents(self,list_of_events):
        global event_list
        if isinstance(list_of_events, list):
            for e in list_of_events:
                event_list.append(e)
    def addEvent(self,item):
        if isinstance(item,Event):
            
    
    def removeEvent(self):
        pass
    
    def clearEvents(self):
        event_list = []