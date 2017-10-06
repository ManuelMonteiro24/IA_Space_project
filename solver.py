import sys
from graphs import graph_struct
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
launch_list = inputdata[1]

print("launch_list: ", launch_list, "\n")

if sys.argv[1] == "-i":
    print("run informed search mode TODO...\n")
else:
    print("run uninformed search mode TODO...\n")

file_functions.generate_output_file([])
