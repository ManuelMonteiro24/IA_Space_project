
"""Provides functions for read from file, print output solution"""

import operator, utils.launch, graphs.graph_struct

def read_input_file(file_name):
    """Function that receives the name of file to read, proccess the data in it to a graph structure (composed by the modules and their connections) and a Launch structure both this structures are returned in the end of function. In case of error on opening the file the function returns None"""

    graph_obj = graphs.graph_struct.Graph();
    obj_launches = utils.launch.Launches()

    try:
        with open(file_name, "r") as input_file:
            for line in input_file:
                splitted_line = line.split()

                if len(splitted_line) == 2:
                    #vertex line
                    if splitted_line[0][0] != "V":
                        #vertex invalid line
                        continue
                    try:
                        float(splitted_line[1])
                        #valid vertex line
                        graph_obj.add_vertex(splitted_line[0], float(splitted_line[1]))
                    except ValueError:
                        #vertex invalid line
                        continue

                elif len(splitted_line) == 3:
                    #edge line
                    if splitted_line[0] != "E" or splitted_line[1][0] != "V" or splitted_line[2][0] != "V":
                        #invalid edge line
                        continue
                    #valid edge line
                    graph_obj.add_edge(splitted_line[1], splitted_line[2])

                elif len(splitted_line) == 5:
                    #launch line
                    if splitted_line[0] != "L" or len(splitted_line[1]) != 8:
                        #invalid launch line
                        continue

                    #valid launch line (still need to check date validity, this is done on the insertion on the Launches list)
                    launch_obj = utils.launch.Launch(splitted_line[1],float(splitted_line[2]),float(splitted_line[3]),float(splitted_line[4]))
                    obj_launches.ordered_insertion_on_list(launch_obj)
                else:
                    continue

        obj_launches.generate_dictionary_trough_list()

        input_file.close()
        return [graph_obj, obj_launches]

    except IOError:
        #error on opening the file
        return None

def generate_output(launches,solution_node):
    """Function that receives the output of the search algorithm and the available launces and prints in the terminal the solution Launch by Launch with the total cost of the operation at the end. If a solution is not found '0' is printed """

    #no solution found
    if solution_node == False:
        print("0")
        return

    cost_sum = 0
    aux_node = solution_node

    while (aux_node.ancestor != None):
        if aux_node.weight != 0 or aux_node != None:
            print(launches[aux_node.launch_id].date, " ", print_modules(aux_node.launched), " ",  aux_node.launch_cost)
            cost_sum += aux_node.launch_cost

        aux_node = aux_node.ancestor

    print(cost_sum)
    return

def print_modules(modules_string):
    """ Function that receives the modules in a set string format and returns it in the desired output format """
    return_str = ""

    for x in modules_string:
        if x == '{' or x == '}' or x == "'" :
            continue
    else:
         return_str += x
    return return_str
