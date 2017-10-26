import sys
#import uninformed_search_function
from graphs import graph_struct
from graphs.graph_struct import Vertex
from graphs.graph_struct import Graph
from graphs.graph_struct import Problem
from graphs.graph_struct import Node
from utils import file_functions

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

inputdata = file_functions.read_input_file(sys.argv[2])

if inputdata == None:
    print("Error: Input file does not appear to exist.")
    sys.exit(1)

graph_obj = inputdata[0]
print("Graph print: \n", graph_obj.toString())
launch_obj = inputdata[1]
launc_obj_output = launch_obj

print(str(launch_obj))

if sys.argv[1] == "-i":

    strategy_obj = strategy.stack.PriorityQueue()
    problem_obj = graphs.Problem(graph_obj.vertices)
    uninformed_search_function.general_search(problem_obj,strategy_stack_obj, launch_obj)
else:
    print("run uninformed search mode TODO...\n")
    #receive output from function and send to generate_output_file function


current_node = Node()
problem = Problem(graph_obj.vertices)
successors = problem.find_successor(launch_obj, current_node)
aux1 = 0

if successors == False:
	print("Ups!\n")
else:
	for i in successors.keys():
		aux1 += 1
		print(i, ":\n\tLaunch ID: ", (successors[i]).launch_id, "\n\tLaunch payload: ", successors[i].launch_payload, "\n\tTotal weight: ", successors[i].weight, "\n\tPath cost: ", successors[i].path_cost, "\n\tModules in space: ", successors[i].modules_in_space, "\n\tList of launches: ", list(launch_obj.launch_dict), "\n")

print("Number of successors: ", aux1)
