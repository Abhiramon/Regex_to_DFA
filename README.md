# Regex_to_DFA
A program which converts input regex to NFA and further to DFA

**Under Development**
*(Currently works for most regex, but some bugs exist)*

### Usage Instructions: 
Execute run.py program (Use python 3) 

### Output format:
* Vertices: The names of the vertices (as a string of numbers)
* Edges are repesented as ("source", "destination", "weight")
* _ stands for epsilon transition when used as weight (in NFA)
* _ stands for phi state (Discard state) when used as a state (in DFA)

### To do:
* Code needs to be documented
* Bug fixes
* Add functionality to visualize NFA and DFA as graphs 