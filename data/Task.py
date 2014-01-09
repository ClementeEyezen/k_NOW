class Task():
    def __init__(self,id_,title,last_updated,selfLink,parent,notes,status,
                 due):
        global __id__
        __id__ = str(id_)
        global url
        url = str(selfLink)
        global task
        task = str(title)
        global time_updated
        #set to datetime item
        global parent
        #set to take in Tasks,etc.
        #check to reference to other nodes
        global note_string
        note_string = str(notes)
        global current_status
        current_status = str(status)
        global due_date
        #set to datetime item
        
    #Tokens, etc.