class Graph:
#	a class to hold knowledge representations
	def __init__(self,node_list=[],modifier_list=[]):
		global modifiers #adjectives for graph
		modifiers = modifier_list
		global nodes
		nodes = node_list
		nodes = nodes.sort(key=nodes.toString().lower)
	
	def printGraph(self):
		for node in nodes:
			print node.toString()+" --> "+str(node.connection_list)
	
	def addNode(self,node):
		global nodes
		nodes.append(node)
		nodes = nodes.sort(key=nodes.toString().lower)

	def removeNode(self,target):
		global nodes
		for index,node in enumerate(nodes):
			if target == node:
				nodes.remove(index)