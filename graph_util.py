def get_start_state(g):
	for n in g[0]:
		if n.is_start_state==True:
			return n
	return -1

def get_accept_states(g):
	l=[]
	for n in g[0]:
		if n.is_accept_state==True:
			l.append(n)

	return l

def print_graph(g):
	nodes=g[0]
	edges=g[1]
	accept_states=[]
	print ("vertices are: ")
	for i in nodes:
		if (i.is_accept_state):
			accept_states.append(i)
		if (i.is_start_state):
			start_state=i
		print(i.name)
	print("edges:")
	for i in edges:
		print(i[0].name,i[1].name,i[2])
	print("accept states:",[i.name for i in accept_states])
	print("start state ",start_state.name)


class Node:
	#each time Node object is created, it will have a different name by default
	num=1
	def __init__(self,_adj_list,_is_start_state=False,_is_accept_state=False,_name=""):
		if (_name==""):
			self.name=str(Node.num)
		else:
			self.name=_name
		self.adj_list=_adj_list
		self.is_start_state=_is_start_state
		self.is_accept_state=_is_accept_state
		# print(Node.num)
		if self.name==str(Node.num):
			Node.num+=1
	def unique_outgoing_edges(self):
		num=0
		lst=[]
		for i in range(len(self.adj_list)):
			if self.adj_list[i][1] not in lst:
				num+=1
				lst.append(self.adj_list[i][1])
		return lst

	def add_edge(self,e,c):
		self.adj_list.append((e,c))

	def set_start(self):
		self.is_start_state=True

	def unset_start(self):
		self.is_start_state=False

	def set_accept(self):
		self.is_accept_state=True

	def unset_accept(self):
		self.is_accept_state=False

	def add_to_name(self,n):
		#Adds a character to node's name, if it does not already exist
		i=0
		check=True
		for i in range(len(self.name)):
			if (self.name[i]==n):
				check=False

		if (check==True):
			self.name+=n

	def get_states(self):
		#return list of characters in node's name
		l=[]
		for i in range(len(self.name)):
			l.append(self.name[i])
		return l

