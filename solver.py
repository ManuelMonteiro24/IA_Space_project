import sys
from datetime import date

if (len(sys.argv) != 3) or not ((sys.argv[1] == "-i") or (sys.argv[1] == "-u")):
    print("Usage: solver.py search_flag(-i||-u) path_to_input_file")
    sys.exit(1)

#data structs to test
vertex_list = []
edge_list = []
launch_list = []

try:
    with open(sys.argv[2], "r") as input_file:
        for line in input_file:
            splitted_line = line.split()

            if len(splitted_line) == 2:
                #vertex line
                if splitted_line[0][0] != "V":
                    continue
                try:
                    float(splitted_line[1])
                    #valid vertex line
                    vertex_list.append([splitted_line[0], splitted_line[1]])
                except ValueError:
                    continue

            elif len(splitted_line) == 3:
                #edge line
                if splitted_line[0] != "E" or splitted_line[1][0] != "V" or splitted_line[2][0] != "V":
                    continue
                #valid edge line
                edge_list.append([splitted_line[1], splitted_line[2]])

            elif len(splitted_line) == 5:
                #launch line
                if splitted_line[0] != "L" or len(splitted_line[1]) != 8:
                    continue
                try:
                    int(splitted_line[1])
                    date(int(splitted_line[1][4:]),int(splitted_line[1][2:4]),int(splitted_line[1][:2]))
                    float(splitted_line[2])
                    float(splitted_line[3])
                    float(splitted_line[4])
                    #valid launch line
                    launch_list.append([splitted_line[1], splitted_line[2], splitted_line[3], splitted_line[4]])
                except:
                    continue
            else:
                continue
    input_file.close()

except IOError:
      print("Error: Input file does not appear to exist.")
      sys.exit(1)

print("vertex_list: ", vertex_list, "\n")
print("edge_list: ", edge_list, "\n")
print("launch_list: ", launch_list, "\n")

if sys.argv[1] == "-i":
    print("run informed search mode TODO...")
else:
    print("run uninformed search mode TODO...")

output_file = open("solver_solution.txt", "w")
output_file.write("Output file TODO...")
output_file.close()
