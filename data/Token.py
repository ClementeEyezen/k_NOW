class Token():
    #a general token for use primarily with nodes
    name = ""
    def __init__(self, name1=None):
        global name
        name = name1
        print "name set to "+name
    
    def toString(self):
        global name
        return str(name)
    
    def setName(self,name1=None):
        try:
            name = str(name1)
            print "name set to "+str(name1)
            return True
        except ValueError:
            print "Incorrect name type"
            return False