import sys, copy, utils.file_functions, graphs.graph_struct, uninformed_search_function
import strategy.modified_Queue
if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

inputdata = utils.file_functions.read_input_file(sys.argv[2])

if inputdata == None:
    print("Error: Input file does not appear to exist.")
    sys.exit(1)

graph_obj = inputdata[0]
launch_obj = inputdata[1]
launc_obj_output = copy.deepcopy(launch_obj)

if sys.argv[1] == "-u":
    strategy_obj = strategy.modified_Queue.MyPriorityQueue()
    problem_obj = graphs.graph_struct.Problem(graph_obj.vertices)
    algorithm_result = uninformed_search_function.general_search(problem_obj,strategy_obj, launch_obj)
else:
    print("informed TO DO...")

utils.file_functions.generate_output(launc_obj_output.launch_dict, algorithm_result)
sys.exit()
