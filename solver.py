import sys, utils.file_functions, graphs, informed_search_function, uninformed_search_function, strategy, heuristic

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

inputdata = utils.file_functions.read_input_file(sys.argv[2])

if inputdata == None:
    print("Error: Input file does not appear to exist.")
    sys.exit(1)
if inputdata == False:
    print("0")
    sys.exit()

problem_obj = graphs.graph_struct.Problem(inputdata[0].vertices)
launch_obj = inputdata[1]

if sys.argv[1] == "-u":
    algorithm_result = uninformed_search_function.uniform_search(problem_obj, launch_obj)
else:
    algorithm_result = informed_search_function.a_star_search(problem_obj, launch_obj, heuristic.heuristic_2)

utils.file_functions.generate_output(launch_obj.launch_dict, algorithm_result)
sys.exit()
