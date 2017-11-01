import re, utils.launch, graphs.graph_struct


def read_input_file(file_name):
    """Function that receives name of file to read from and returns a structure with list of vertex, edges and launches"""

    graph_obj = graphs.graph_struct.Graph();
    obj_launches = utils.launch.Launches()
    count_valid_edges = 0

    try:
        with open(file_name, "r") as input_file:
            for line in input_file:
                splitted_line = line.split()

                if len(splitted_line) == 2:
                    #vertex line
                    if splitted_line[0][0] != "V":
                        #invalid vertex line
                        continue
                    try:
                        float(splitted_line[1])
                        #valid vertex line
                        graph_obj.add_vertex(splitted_line[0], float(splitted_line[1]))
                    except ValueError:
                        #invalid vertex line
                        continue

                elif len(splitted_line) == 5:
                    #launch line
                    if splitted_line[0] != "L" or len(splitted_line[1]) != 8:
                        #invalid launch line
                        continue

                    #valid launch line (still need to check date validity)
                    launch_obj = utils.launch.Launch(splitted_line[1],float(splitted_line[2]),float(splitted_line[3]),float(splitted_line[4]))
                    obj_launches.ordered_insertion_on_list(launch_obj)
                else:
                    #invalid line
                    continue

            input_file.seek(0,0)

            for line in input_file:
                splitted_line = line.split()
                if len(splitted_line) == 3:
                    #edge line
                    if splitted_line[0] != "E" or splitted_line[1][0] != "V" or splitted_line[2][0] != "V":
                        #invalid edge line
                        continue
                    #valid edge line
                    if graph_obj.add_edge(splitted_line[1], splitted_line[2]) == False:
                        continue
                    count_valid_edges += 1 

        if count_valid_edges < len(graph_obj.vertices)-1:
            return False

        obj_launches.generate_dictionary_trough_list()

        input_file.close()
        return [graph_obj, obj_launches]

    except IOError:
        #error in opening the file
        return None

def generate_output(launches,solution_node):
    """Function that receives a list with the solved launch data and generates the proper output file"""

    if solution_node == False:
        #no solution
        print("0")
        return

    #list tha will hold the node launches to print in the correct order
    node_list = list()
    cost_sum = 0
    aux_node = solution_node

    #iterate until we reach the node that corresponds to first launch
    while (aux_node.ancestor != None):
        cost_sum += aux_node.launch_cost
        node_list.insert(0, aux_node)
        aux_node = aux_node.ancestor

    for node in node_list:
        if node.weight != 0:
            print(launches[node.launch_id].date, " ", print_modules(str(node.launched)), " ", node.launch_cost)

    print(cost_sum)
    return

def print_modules(modules_str):
    """Function returns the a string of modules in the valid format"""
    return re.sub("[},'{]", '', modules_str)
