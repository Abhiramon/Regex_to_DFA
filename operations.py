from graph_util import *

def single_char_graph(c):
	n2=Node([],False,True)
	n1=Node([(n2,c)],True,False)
	return [[n1,n2],[(n1,n2,c)]]


def union(g1,g2):
	n3=Node([],True,False)
	n1=get_start_state(g1)
	n2=get_start_state(g2)
	n1.unset_start()
	n2.unset_start()

	n3.add_edge(n1,'_')
	n3.add_edge(n2,'_')

	nodes=[]
	edges=[]
	for i in range(len(g1[0])):
		nodes.append(g1[0][i])
	for i in range(len(g2[0])):
		nodes.append(g2[0][i])
	nodes.append(n3)	
	for i in range(len(g1[1])):
		edges.append(g1[1][i])
	for i in range(len(g2[1])):
		edges.append(g2[1][i])
	edges.append((n3,n1,'_'))
	edges.append((n3,n2,'_'))

	return [nodes,edges]

def concat(g1,g2):
	nodes = []
	edges = []

	graph_one_accept_states = get_accept_states(g1)
	graph_two_start_state = get_start_state(g2)

	graph_two_start_state.unset_start()

	for node in graph_one_accept_states:
		node.unset_accept()
		node.add_edge(graph_two_start_state, '_')
		edges.append((node, graph_two_start_state, '_'))
		

	for i in range(len(g1[0])):
		nodes.append(g1[0][i])
	for i in range(len(g2[0])):
		nodes.append(g2[0][i])
	for i in range(len(g1[1])):
		edges.append(g1[1][i])
	for i in range(len(g2[1])):
		edges.append(g2[1][i])

	return [nodes,edges]
	
def repetition(g):
	nodes = []
	edges = []

	start_state = get_start_state(g)
	accept_states = get_accept_states(g)

	start_state.unset_start()

	new_start = Node([(start_state,'_')], True, True)
	edges.append((new_start, start_state, '_'))
	nodes.append(new_start)

	for node in accept_states:
		node.add_edge(new_start,'_')
		edges.append((node,new_start,'_'))
	for i in range(len(g[0])):
		nodes.append(g[0][i])
	for i in range(len(g[1])):
		edges.append(g[1][i])

	return [nodes,edges]


if __name__=="__main__":
	print("Testing union:")
	g1=single_char_grah('1')
	g2=single_char_grah('0')
	g3=union(g1,g2)

	print_graph(g3)
	print("accept states: ",[i.name for i in get_accept_states(g3)])
	print('start states: ',get_start_state(g3).name)


