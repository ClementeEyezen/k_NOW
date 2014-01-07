

class Event():
    def __init__(self,id_,first_name,last_name):
        global fi_name
        fi_name = first_name
        global la_name
        la_name = last_name
        global id
        id = id_
    
    def gen_attendee(self):
        #generate/return an attendee output for calendar events
        pass
    
    def gen_googleCompatible(self):
        #generate/return a contact creation output for Google contacts
        pass
