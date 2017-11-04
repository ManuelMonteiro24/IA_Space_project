"""File that contains the Classes Problem and Node that define the search problem."""

import itertools, graphs.graph_struct

class Node():
    """Class that represents the node type that is utilized in the problem. Each node contains: launch_id, that represents the associated launch;
    launch_payload, with the modules that are carried to space; weight, that represents the total weight of modules to launched; path_cost; modules_in_space, a set with the modules already in space;
    launch_cost, that represents the total cost of the launch with the modules in it; ancestor, that represents the parent node from which this node has expanded, in case of the first node this one is None."""
    def __init__(self, launch_id = 0, launch_payload = -1, weight = 0, path_cost = 0, modules_in_space = [], launch_cost = 0, launched = set(), ancestor = None):
        self.launch_id = launch_id
        self.launch_payload = launch_payload
        self.weight = weight
        self.path_cost = path_cost
        self.modules_in_space = modules_in_space
        self.launch_cost = launch_cost
        self.launched = launched
        self.ancestor = ancestor

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __str__(self):
        return "l_id: %d l_pay: %f wei: %f path_cost: %f modules in space: %s" % (self.launch_id, self.launch_payload, self.weight, self.path_cost, str(self.modules_in_space))


class Problem(graphs.graph_struct.Graph):
    """Class that specifies the characteristics of the search problem "In orbit assembly of large structures". This includes the Full state space, all the combinations of modules in space, the inital state, a empty set represeting no modules in space,
    the operators, set of actions that change the world state the goal test, that represents the condition that has to be satisfied at the goal state and the path cost, that represents the cost associated to a sequence of states/actions (sum of cost used to form the path)."""
    def __init__(self, vertices_input):
        self.goal_state = list(vertices_input)
        self.vertices = vertices_input
        self.neighbors_modules_in_space = set()

    def path_cost_calculator(self, current_node, new_node, launch_obj):
        """Method that receives the node currently on analysis and a child none and returns the path_cost of this new child node. This is done by adding to the path cost of the current node
        the fixed cost of the launch associated with the child none, plus the variable cost of the launch associated times the weight of the module that he is going to carry"""
        aux_node = current_node
        while aux_node.ancestor != None:
            if aux_node.weight != 0:
                path_cost_prev = aux_node.path_cost
                break
            aux_node = aux_node.ancestor
            
        if aux_node.weight == 0:
            path_cost_prev = 0    

        return (path_cost_prev + launch_obj.launch_dict[new_node.launch_id].fixed_cost + new_node.weight*(launch_obj.launch_dict[new_node.launch_id].variable_cost))


    def launch_cost(self, new_node, launch_obj):
        """Method that receives a node a calculates the launch cost associated. This is done by adding the launch fixed cost to the sum of the modules weight in transit times the launch variable cost.
        The atribute launch_cost of the node received gets updated and this value is also returned."""
        new_node.launch_cost = launch_obj.launch_dict[new_node.launch_id].fixed_cost + new_node.weight*(launch_obj.launch_dict[new_node.launch_id].variable_cost)
        return  new_node.launch_cost

    def goal_test(self, current_node):
        """Method that tests if the received node achieved the goal_state. This is done by checking if the modules in space in the node corresponds to all modules in space."""
        if not set(self.goal_state).difference(set(current_node.modules_in_space)):
            return True
        else:
            return False

    def weight_calculator(self, current_node, launch_obj):
        """Method that calculates the weight of all the modules still in land (returned as unlaunched_modules_weight)
        and the sum of max_payload of each launch that can still be used (returned as launches_weight)."""
        unlaunched_modules_weight = 0
        launches_weight = 0
        for i in set(self.vertices).difference(set(current_node.modules_in_space)):
            unlaunched_modules_weight += (self.vertices[i]).weight

        for key in set(launch_obj.launch_dict):
            if key > current_node.launch_id:
                #only sum launches which the launch date is posterior to the current node launch
                launches_weight += (launch_obj.launch_dict[key]).max_payload
        return unlaunched_modules_weight, launches_weight


    def check_if_neighbor_in_space(self, combination):
        """Method that receives a combination of modules that we wish to send to space and for each module received it is going to be checked if it has a neighbor in space.
        This is done to respect the following condition: """
        for i in combination:
            if i in self.neighbors_modules_in_space:
                yield True


    def modules_connected(self, current_node, combination, launch_obj):
        """Method that receives the current_node on analysis and a set of modules (still on Earth) and returns true if it possible to send those modules to the space, else returns false."""
        neigh = set()
        extra_modules = set()

        for i in combination:
            neigh = neigh.union(set(self.vertices[i].neighbors))

        neigh = neigh.union(self.neighbors_modules_in_space)
        path_max = []

        for i in itertools.combinations(combination, 2):
            path = []
            self.find_path(list(i)[0], list(i)[1], path)
            if len(path) > len(path_max):
                path_max = path

        for j in path_max:
            if (j not in list(combination)):
                if in_modules_in_space(current_node, launch_obj) and (j not in current_node.modules_in_space):
                    return False
                if in_modules_in_space(current_node, launch_obj):
                    return False

        if len(path_max) == len(combination):
            if set(path_max) == set(combination):
                return True
            else:
                extra_modules = set(combination) - set(path_max)
                for i in extra_modules:
                    if i in neigh:
                        return True
                    else:
                        return False

        if len(path_max) < len(combination):
            extra_modules = set(combination) - set(path_max)
            for i in extra_modules:
                if i not in neigh:
                    return False
            return True

        if len(path_max) > len(combination):
            extra_modules = set(path_max) - set(combination)
            for i in extra_modules:
                if i not in current_node.modules_in_space:
                    return False
            return True

        return False


    def actions(self, launch_obj, current_node):
        """Method that expands the current node on analysis and returns the expanded child nodes."""

        count_successors = 0
        modules_on_earth = set(self.vertices).difference(set(current_node.modules_in_space))

        successors = dict()
        self.neighbors_modules_in_space = set()

        for i in current_node.modules_in_space:
            if check_launches_id(i, launch_obj) == False:
                self.neighbors_modules_in_space = self.neighbors_modules_in_space.union(set(self.vertices[i].neighbors))

        if not launch_obj.launch_dict:
            return False

        unlaunched_modules_weight, launches_weight = self.weight_calculator(current_node, launch_obj)

        #Check if launches available are enough to send the modules on Earth
        if launches_weight < unlaunched_modules_weight:
            if current_node.launch_id > 0:
                return None
            else:
                return False

        if current_node.launch_id == list(launch_obj.launch_dict.keys())[-1]:
            return None

        launch_max_payload = launch_obj.launch_dict[current_node.launch_id+1].max_payload

        for n in range(len(modules_on_earth)):
            count_comb = 0
            count_breaks = 0
            total_weight = 0

            for x in itertools.combinations(modules_on_earth, n+1):
                count_comb += 1
                successors_id = set()

                #Checks if there is at least a module that is a neighbor of a module already in space, except for the first node with modules to be sent
                if in_modules_in_space(current_node, launch_obj) and list(self.check_if_neighbor_in_space(x)) == []:
                    continue

                #Check if there is connection between modules
                if self.modules_connected(current_node, x, launch_obj) == False and n>0:
                    continue

                #Check if launch max. payload is enough to send the set of modules
                for i in x:
                    total_weight += self.vertices[i].weight
                    if total_weight > launch_max_payload:
                        total_weight = 0
                        count_breaks += 1
                        break
                    successors_id.add(self.vertices[i].id)

                if total_weight != 0:
                    count_successors += 1
                    count = 0
                    for i in current_node.modules_in_space:
                        if i == "":
                            count += 1
                    new_node = Node(current_node.launch_id + 1, launch_max_payload, total_weight, 0, list(), 0, successors_id, current_node)
                    new_node.modules_in_space = list(set(current_node.modules_in_space).union(successors_id))

                    for i in range(0,count):
                        new_node.modules_in_space.append("")
                    
                    new_node.path_cost = self.path_cost_calculator(current_node, new_node, launch_obj)
                    new_node.launch_cost = self.launch_cost(new_node, launch_obj)
                    successors[count_successors] = new_node
                    total_weight = 0

            #if for a combination of n modules there are no successors to add there won't be for combinations with higher than n modules (weight is greater)
            if count_breaks == count_comb:
                break

        count_successors += 1
        new_node = Node(current_node.launch_id + 1, launch_max_payload, 0, 0, list(), 0, set(), current_node)
        new_node.modules_in_space = current_node.modules_in_space + [str(new_node.launch_id)]
        successors[count_successors] = new_node

        return successors


def in_modules_in_space(node, launch_obj):
        for i in node.modules_in_space:
            if check_launches_id(i, launch_obj) == False:
                return True
        return False

def check_launches_id(i, launch_obj):

    aux= 1
    while aux <= len(launch_obj.launch_dict):
        if i == str(aux):
            return True    
        aux += 1
    return False    
