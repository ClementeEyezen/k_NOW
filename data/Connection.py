class Connection:
    def __init__(self,node1=None,weight1=1):
        global node
        node = node1
        global weight
        weight = weight1
        
    def checkConnection(self,target):
        if target==node:
            return weight
        else:
            return None
        