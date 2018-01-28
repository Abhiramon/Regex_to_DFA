from make_DFA import *

regex=raw_input("Enter a regex: ")
g=get_DFA(regex,True)
print("DFA: ")
print_graph(g)