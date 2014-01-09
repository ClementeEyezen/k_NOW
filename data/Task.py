from data.Token import Token

class Task():
    def __init__(self,id_,tasklist,title,last_updated,selfLink,parent_,position_,
                 notes,status,due,links_list):
        global task_list
        task_list = tasklist
        global __id__
        __id__ = str(id_)
        global url
        url = str(selfLink)
        global task
        task = str(title)
        global time_updated
        time_updated = last_updated
        global task_parent
        if isinstance(task_parent,Task.Task):
            task_parent = parent_
        #check to reference to other nodes
        global note_string
        note_string = str(notes)
        global current_status
        current_status = str(status)
        global due_date
        due_date = due
        global position
        position = str(position_)
        
        #node properties
        global token_list
        global connections
        global description
        global parent #graph-parent, as opposed to task parent (can be same)
        
    #Tokens, etc.
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
                bool_test = self.addToken(tok) and bool_test
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
        lol = str(task)+" "+str(__id__)
        return lol
        
    def gen_googleCompatible(self):
        g_time_updated = str(time_updated).replace(' ','T')
        g_time_updated = g_time_updated[0:len(g_time_updated)-3]
        g_time_due = str(due_date).replace(' ','T')
        g_time_due = g_time_due[0:len(g_time_due)-3]
        return {
                "kind": "tasks#task",
                "id": __id__,
                "title": task,
                "updated": g_time_updated,
                "selfLink": url,
                "parent": task_parent,
                "position": position,
                "notes": note_string,
                "status": current_status,
                "due": g_time_due,
                "links": [
                          '''{
                           "type": string,
                           "description": string,
                           "link": string
                           }'''
                          ]
                }
    
class TaskList():
    def __init__(self,id_,kind_,title,last_updated,selfLink):
        global kind
        kind = str(kind_)
        global __id__
        __id__ = str(id_)
        global list_title
        list_title = str(title)
        global time_updated
        time_updated = last_updated
        global url
        url = str(selfLink)
        global tasks
        tasks = []
    
    def addTask(self,item):
        if isinstance(item,Task.Task):
            tasks.append(item)
            return True
        else:
            return False
        
    def addTaskSet(self,multiple):
        complete_success = True
        if isinstance(multiple,list):
            for item in multiple:
                complete_success = self.addTask(item) and complete_success
        return complete_success

class TaskManager():
    def __init__(self):
        global listOfLists
    
    def addList(self,task_list):
        if isinstance(task_list,Task.TaskManager):
            global listOfLists
            listOfLists.append(task_list)
            return True
        else:
            return False
    
    def addListSet(self,multiple):
        complete_success = True
        if isinstance(multiple,list):
            for item in multiple:
                complete_success = self.addList(item) and complete_success
        return complete_success