import sys
import copy
from queue import PriorityQueue
#import uninformed_search_function
from graphs import graph_struct
from graphs.graph_struct import Vertex
from graphs.graph_struct import Graph
from graphs.graph_struct import Problem
from graphs.graph_struct import Node
from utils import file_functions
from uninformed_search_function2 import general_search

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
launc_obj_output = copy.deepcopy(launch_obj)

print(str(launch_obj))

if sys.argv[1] == "-u":
    strategy_obj = PriorityQueue()
    problem_obj = Problem(graph_obj.vertices)
    algorithm_result = general_search(problem_obj,strategy_obj, launch_obj)

initial_node = Node()
file_functions.generate_output(launc_obj_output.launch_dict, algorithm_result, initial_node)
sys.exit()
