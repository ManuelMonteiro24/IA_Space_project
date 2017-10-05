import sys

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

try:
    with open(sys.argv[2], "r") as input_file:
        for line in openfileobject:
            do_something()
except IOError:
      print("Error: Input file does not appear to exist.")
      sys.exit(1)



if sys.argv[1] == "-i":
    print("run informed search mode TODO...")
else:
    print("run uninformed search mode TODO...")



output_file = open("solver_solution.txt", "w")
output_file.write("Output file TODO...")
output_file.close()
