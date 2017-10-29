import operator, launch, graph.graph_struct

def read_input_file(file_name):
    "Function that receives name of file to read from and returns a structure with list of vertex, edges and launches"

    graph_obj = graph.graph_struct.Graph();

    #data structs to test
    obj_launches = Launch.Launches()

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
                        graph_obj.add_vertex(splitted_line[0], float(splitted_line[1]))
                    except ValueError:
                        continue

                elif len(splitted_line) == 3:
                    #edge line
                    if splitted_line[0] != "E" or splitted_line[1][0] != "V" or splitted_line[2][0] != "V":
                        continue
                    #valid edge line
                    graph_obj.add_edge(splitted_line[1], splitted_line[2])

                elif len(splitted_line) == 5:
                    #launch line
                    if splitted_line[0] != "L" or len(splitted_line[1]) != 8:
                        continue

                    #valid launch line (still need to check date validity)
                    launch_obj = Launch.Launch(splitted_line[1],float(splitted_line[2]),float(splitted_line[3]),float(splitted_line[4]))
                    obj_launches.ordered_insertion_on_list(launch_obj)
                else:
                    continue

        obj_launches.generate_dictionary_trough_list()

        return [graph_obj, obj_launches]
        input_file.close()

    except IOError:
        return None


#needs adaptation
def generate_output(launches,solution_node):
    "Function that receives a list with the solved launch data and generates the proper output file"

    if solution_node == False:
        print("0")
        return

    cost_sum = 0
    aux_node = solution_node

    while (aux_node != None):
        if aux_node.weight != 0 or aux_node != None:
            print(launches[aux_node.launch_id].date, " ", aux_node.launched, " ",  aux_node.launch_cost)
            cost_sum += aux_node.launch_cost

        aux_node = aux_node.ancestor

    '''
    for key, value in solution_node.launch_schedule.items():
        if value.weight != 0 or value != None:
            print(launches[value.launch_id].date, " ", key, " ",  str(value.launch_cost))
            cost_sum += value.launch_cost
    '''
    print(cost_sum)
    return
