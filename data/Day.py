import Event

class Day():
    def __init__(self,list_of_events):
        self.addEvents(list_of_events)
    
    def addEvents(self,list_of_events):
        global earliest_time
        global latest_time
        if isinstance(list_of_events,list):
            for e in list_of_events:
                self.addEvent(e)
                if e.start_time < earliest_time:
                    earliest_time = e.start_time
                if e.end_time > latest_time:
                    latest_time = e.end_time
            return True
        else:
            return False
    
    def addEvent(self,item):
        global event_list
        if item is Event:
            event_list.append(item)
            
    def earlyTime(self):
        return earliest_time
    
