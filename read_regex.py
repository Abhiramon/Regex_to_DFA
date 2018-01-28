from operations import *
from graph_util import *

special_chars=['+','*','(',')']

def get_NFA(regex):
	#returns NFA from regex
	
	graph_list=[]

	for i in range(0,len(regex)):
		if (regex[i] in special_chars):
			graph_list.append(regex[i])

		else:
			graph_list.append(single_char_graph(regex[i]))

	return read_regex(graph_list,0,len(regex)-1)

def read_regex(graph_list,f,l):
	#Returns NFA from graph_list
	new_list=[]
	i=f
	while(i<=l):
		if (graph_list[i]!='('):
			new_list.append(graph_list[i])

		else:
			j=i+1
			num_unclosed_brackets=0
			while(j<=l):
				if (graph_list[j]=='('):
					num_unclosed_brackets+=1
				if (graph_list[j]==')'):

					if (num_unclosed_brackets==0):
						break
					else:
						num_unclosed_brackets-=1
				j+=1

			new_list.append(read_regex(graph_list,i+1,j-1))
			i=j

		i+=1
	# print("First")
	# print_graph_list(new_list)
	new_list=resolve_star(new_list)
	# print("After resolving star")
	# print_graph_list(new_list)
	new_list=resolve_concat(new_list)
	# print("after concat")
	# print_graph_list(new_list)
	return resolve_plus(new_list)


def resolve_star(glist):
	new_list=[]
	i=len(glist)-1
	while(i>=0):
		if (glist[i]=='*'):
			new_list.append(repetition(glist[i-1]))
			i-=1
		else:
			new_list.append(glist[i])

		i-=1

	new_list.reverse()
	return new_list

def resolve_concat(glist):
	i=1
	g=glist[0]
	new_list=[]
	while(i<len(glist)):
		if glist[i]!='+':
			g=concat(g,glist[i])

		else:
			new_list.append(g)
			new_list.append('+')
			g=glist[i+1]
			i+=1

		i+=1
	new_list.append(g)
	return new_list

def resolve_plus(glist):
	
	g=glist[0]
	i=1
	while(i<len(glist)):
		if (glist[i]=='+'):
			g=union(g,glist[i+1])
			i+=1

		i+=1

	return g

def print_graph_list(glist):
	for i in range(len(glist)):
		if (glist[i] in special_chars):
			print glist[i],", ",
		else :
			print get_start_state(glist[i]).name,", ",
	print ("")


if __name__=="__main__":
	g=get_NFA("10*1+1*0")
	print_graph(g)
