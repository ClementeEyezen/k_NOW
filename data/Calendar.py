from datetime import time
from datetime import date
from Token import Token

class Event():
    def __init__(self,event_name,event_date,start_time,end_time=None):
        global name
        name = event_name
        global date 
        date = event_date
        global s_time
        s_time = start_time
        global e_time
        e_time = end_time
    
    def addToken(self,item):
        #adds tokens that are associated with this event
        #returns true if successfully added
        #returns false if the item was not a token
        global token_list
        if item is Token:
            token_list.append(item)
            return True
        else:
            return False
    
    def addToken_list(self,item_list):
        #adds tokens from a list
        #returns true if item_list is a list and items were considered for adding
        #returns false if item_list is not a list
        #returns false if one or more items were not Tokens
        bool_test = True
        if isinstance(item_list, list):
            for tok in item_list:
                bool_test = bool_test and self.addToken(tok)
            return bool_test
        else:
            return False
        
    def setDescription(self,desc=''):
        try:
            global description
            description = str(desc)
            return True
        except:
            return False
        
#A Calendar is a list of events
class Calendar():
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