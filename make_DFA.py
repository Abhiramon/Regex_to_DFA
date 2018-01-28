from read_regex import *

def get_lang(regex):
	lang=[]
	for i in range(len(regex)):
		if (regex[i] not in special_chars):
			if (regex[i] not in lang):
				lang.append(regex[i])
	return lang

def remove_duplicates(lst):
	l=[]
	for i in lst:
		 if i not in l:
		 	l.append(i)
	return l

def add_list_to_name(node,lst):
	for c in lst:
		node.add_to_name(c)

def interpolate(node,lst):
	# print("interpolating",node.name,"adj list is",[(n[0].name,n[1]) for n in node.adj_list])
	# print(node.name)
	for i in range(len(node.adj_list)):
		if (node.adj_list[i][1]=='_' and (node.adj_list[i][0].name not in lst)):
			lst.append(node.adj_list[i][0].name)

			l=interpolate(node.adj_list[i][0],lst)
			for c in l:
				if c not in lst:
					lst.append(c)
	
	return lst

def check_node_exists(nodes,lst):
	for i in range(len(nodes)):
		node=nodes[i]
		l=node.get_states()
		count=0
		for j in lst:
			if j in l:
				count+=1
		if count==len(lst):
			return i
	return -1

def get_DFA(regex,print_nfa=False):
	g=get_NFA(regex)
	if print_nfa:
		print("NFA: ")
		print_graph(g)
	lang=get_lang(regex)

	nodes=[]
	edges=[]

	start_node_nfa=get_start_state(g)
	start_node_dfa=Node([],True,False,start_node_nfa.name)
	add_list_to_name(start_node_dfa,interpolate(start_node_nfa,[]))


	nodes.append(start_node_dfa)
	
	phi=Node([],False,False,'-')  #Phi node called -
	for i in range(len(lang)):
		phi.add_edge(phi,lang[i])
		edges.append((phi,phi,lang[i]))

	nodes.append(phi)
	
	while(len(edges)<len(lang)*len(nodes)):
		for i in range(len(nodes)):
			node_edge_lang=nodes[i].unique_outgoing_edges()
			# print(nodes[i].name,node_edge_lang)
			if (len(node_edge_lang)<len(lang)):
				for e in lang:
					if e not in node_edge_lang:
						connect_to_phi=True
						names_to_add=[]
						# print("For node",nodes[i].name,"edge",e)
						for c in nodes[i].get_states():
							for j in range(len(g[0])):
								if (g[0][j].name==c):
									n=g[0][j]
							for j in range(len(n.adj_list)):
								if (n.adj_list[j][1]==e):
									# print("Found",n.name,"connected by",e)
									connect_to_phi=False
									names_to_add.append(n.adj_list[j][0].name)
									names_to_add.extend(interpolate(n.adj_list[j][0],[]))
									# print("Names to add after interpolate",names_to_add)
						if (connect_to_phi):
							edges.append((nodes[i],phi,e))
							nodes[i].add_edge(phi,e)
							# print("connecting to phi")
						else:
							names_to_add=remove_duplicates(names_to_add)
							pos=check_node_exists(nodes,names_to_add)
							if (pos!=-1):
								edges.append((nodes[i],nodes[pos],e))
								nodes[i].add_edge(nodes[pos],e)
								# print("Added edge from ",nodes[i].name,"to",nodes[pos].name)
							else:
								new_node=Node([],False,False,names_to_add[0])
								if (len(names_to_add)>1):
									add_list_to_name(new_node,names_to_add[1:])
								edges.append((nodes[i],new_node,e))
								nodes[i].add_edge(new_node,e)
								nodes.append(new_node)
								# print("Created new node",new_node.name)

	for node in nodes:
		for c in node.get_states():
			for j in range(len(g[0])):
				if (g[0][j].name==c):
					n=g[0][j]
			if (n.is_accept_state):
				node.set_accept()
	return [nodes,edges]




	



