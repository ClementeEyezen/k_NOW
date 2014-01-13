from datetime import datetime
from datetime import timedelta
from data.Token import *
from data.Node import Node

class Event():
    def __init__(self,event_name,id_,
                 event_date=datetime.now(),
                 start_time=datetime.now(),
                 end_time=datetime.now()+timedelta(0,3600),
                 loc='Somewhere'):
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
        global location
        location = loc
        '''if event_date is date:
            global days
            days = event_date.day()
        '''
    
    def getName(self):
        global name
        return name
    
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

    def addConnection(self,connection):
        global connections
        connections.append(connection)
    
    def removeConnection(self,target):
        global connections
        for index,connection in enumerate(connections):
            if target == connection:
                connections.remove(index)
    
    def setParent(self,parent1):
        global parent
        parent = parent1
    
    def toString(self):
        global token_list
        string = ''
        for item in token_list:
            string = string + item.toString()
        return string
    
    def gen_googleCompatible(self):
        g_end_time = str(e_time).replace(' ','T')
        g_end_time = g_end_time[0:len(g_end_time)-3]
        g_start_time = str(s_time).replace(' ','T')
        g_start_time = g_start_time[0:len(g_start_time)-3]
        return {
                'summary': str(name),
                'location': str(location),
                'start': {
                          'dateTime': g_start_time
                          },
                'end':   {
                          'dateTime': g_end_time
                          },
                'attendees': [
                              {
                               #'email': 'mobile.wbaskin@gmail.com',
                               # Other attendee's data...
                               },
                              ],
                }

