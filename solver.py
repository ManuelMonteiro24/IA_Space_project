import sys
from utils import file_functions

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

inputdata = file_functions.read_input_file(sys.argv[2])

if inputdata == None:
    print("Error: Input file does not appear to exist.")
    sys.exit(1)


vertex_list = inputdata[0]
edge_list = inputdata[1]
launch_list = inputdata[2]

print("vertex_list: ", vertex_list, "\n")
print("edge_list: ", edge_list, "\n")
print("launch_list: ", launch_list, "\n")

if sys.argv[1] == "-i":
    print("run informed search mode TODO...")
else:
    print("run uninformed search mode TODO...")

file_functions.generate_output_file([])
