from datetime import date

def read_input_file(file_name):
    "Function that receives name of file to read from and returns a structure with list of vertex, edges and launches"

    #data structs to test
    vertex_list = []
    edge_list = []
    launch_list = []

    try:
        with open(file_name, "r") as input_file:
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
        return [vertex_list, edge_list, launch_list]
        input_file.close()

    except IOError:
        return None

def generate_output_file(solved_launch_list):
    "Function that receives a list with the solved launch data and generates the proper output file"

    output_file = open("solver_solution.txt", "w")
    for node in solved_launch_list:
        output_file.write("Output file TODO...")
        
    output_file.close()
