class SimpleCalendar():
    def __init__(self,calendar_name="",list_of_events=[]):
        global event_list
        event_list = []
        self.addEvents(list_of_events)
        global name
        name = calendar_name

    def addEvents(self,list_of_events):
        global event_list
        if isinstance(list_of_events, list):
            for e in list_of_events:
                event_list.append(e)
