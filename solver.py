import sys
from graphs.graph_struct2 import Vertex
from graphs.graph_struct2 import Graph
from graphs.graph_struct2 import Problem
from graphs.graph_struct2 import Node
from utils.file_functions import read_input_file
from utils.file_functions import generate_output_file

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

inputdata = read_input_file(sys.argv[2])

if inputdata == None:
    print("Error: Input file does not appear to exist.")
    sys.exit(1)

graph_obj = inputdata[0]
print("Graph print: \n", graph_obj.toString())
launch_list = inputdata[1]

print("\nlaunch_list: ", launch_list, "\n")

print("\n Vertices: ", list(graph_obj.vertices))

print("\n First vertex: ", list(graph_obj.vertices)[0], "\n")


if sys.argv[1] == "-i":
    print("run informed search mode TODO...\n")
else:
    print("run uninformed search mode TODO...\n")

#generate_output_file([])

launches_dict = {'L2':[30,62,0.4], 'L3':[140,90,1.8]}

problem = Problem(graph_obj.vertices)
current_node = Node()
'''
current_node.launch_id = 'L1'
current_node.launch_payload = 22.8
current_node.weight = 20.4
current_node.path_cost = 70.16
current_node.modules_in_space = {'VCM'}
'''
successors = problem.find_successor(launches_dict, current_node)
aux = 0
if False:
	print("Ups!\n")
else:
	for i in list(successors):
		aux += 1
		print(i, ":\n\tLaunch ID: ", (successors[i]).launch_id, "\n\tLaunch payload: ", successors[i].launch_payload, "\n\tTotal weight: ", successors[i].weight, "\n\tPath cost: ", successors[i].path_cost, "\n\tModules in space: ", successors[i].modules_in_space, "\n\tList of launches: ", list(launches_dict), "\n")

print("Number of successors: ", aux)