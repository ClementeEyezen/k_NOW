from data import Token

class Node:
    #a node for the graph class
    #tokens store names
    #nodes represent the actual information
    def __init__(self,token1=None,parent1=None,connection_list=[]):
        global token
        token = token1
        global parent
        parent = parent1
        global connections
        connections = connection_list
        print token
        print parent
    
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
    
    def setToken(self,token1):
        global token
        token = token1
    
    def toString(self):
        string = token.toString()
        return string