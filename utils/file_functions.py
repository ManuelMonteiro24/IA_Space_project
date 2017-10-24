from datetime import *
from graphs import graph_struct
import operator


class Launch:

    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost

    def __str__(self):
        return "launch: %s %s %s %s" % (self.date, str(self.max_payload), str(self.fixed_cost), str(self.variable_cost))

class Launches:

    def __init__(self):
        self.launch_list = []
        self.launch_dict = {}

    def ordered_insertion_on_list(self, launch):

        try:
            launch_date_to_insert = date(int(launch.date[4:]),int(launch.date[2:4]),int(launch.date[:2]))
        except:
            return

        aux_index = 0
        if len(self.launch_list) == 0:
            self.launch_list.append(launch)
            return

        for x in self.launch_list:
            launch_date_to_compar = date(int(x.date[4:]),int(x.date[2:4]),int(x.date[:2]))
            if launch_date_to_insert <= launch_date_to_compar:
                launch_list.insert(aux_index,launch)
                return
            aux_index = aux_index + 1

        self.launch_list.append(launch)
        return

    def generate_dictionary_trough_list(self):
        aux_index = 1
        for x in self.launch_list:
            self.launch_dict[aux_index] = x
            aux_index = aux_index + 1

        return

    def __str__(self):

        return_str = "Launches dictionary:"

        for key, value in self.launch_dict.items():
            return_str += " key-- " + str(key) + " value-- "+ str(value)

        return_str += "\nLaunches list:"

        for value in self.launch_list:
            return_str += " " +str(value)

        return return_str

def read_input_file(file_name):
    "Function that receives name of file to read from and returns a structure with list of vertex, edges and launches"

    graph_obj = graph_struct.Graph();

    #data structs to test
    obj_launches = Launches()

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
                    launch_obj = Launch(splitted_line[1],float(splitted_line[2]),float(splitted_line[3]),float(splitted_line[4]))
                    obj_launches.ordered_insertion_on_list(launch_obj)
                else:
                    continue

        obj_launches.generate_dictionary_trough_list()

        return [graph_obj, obj_launches]
        input_file.close()

    except IOError:
        return None


#needs adaptation
def generate_output(launches,solved_launch):
    "Function that receives a list with the solved launch data and generates the proper output file"

    if solved_launch == False:
        print("0")
        return

    aux_str = ""

    cost_sum = 0

    sorted_x = sorted(solved_launch, key=operator.attrgetter('score'))

    for node in sorted(solved_launch.values(), key=operator.attrgetter('launch_id')):
        aux_str = launches.launch_dict[node.launch_id].date

        for module in node.modules_in_space:
            aux_str += " " + module + " "

        aux_str += " " + node.launch_cost
        cost_sum += node.launch_cost
        print(aux_str)

    print(cost_sum)
    return
