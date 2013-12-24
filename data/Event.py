from datetime import datetime
from data import Token
from data import Node

class Event(Node):
    def __init__(self,event_name,id_,event_date=datetime.now(),start_time=datetime.now().time(),end_time=None):
        global name
        name = event_name
        global online_id
        online_id = id_
        global date 
        date = event_date
        global s_time
        s_time = start_time
        global e_time
        e_time = end_time
        if event_date is date:
            global day
            day = event_date.day()
    
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



