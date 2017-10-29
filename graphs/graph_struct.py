from itertools import combinations
from utils import file_functions

class Vertex:
    def __init__(self, id_vertex, weight = -1):
        self.id = id_vertex
        self.neighbors = []
        self.weight=weight

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.id not in self.neighbors:
                self.neighbors.append(neighbor.id)
                neighbor.neighbors.append(self.id)

        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.id not in self.neighbors:
                    self.neighbors.append(neighbor.id)
                    neighbor.neighbors.append(self.id)

            else:
                return False

    def get_neighbors(self):
        return self.neighbors

    #TODO understand
    def __repr__(self):
        return str(self.neighbors)



class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        i=1


    def add_vertex(self, vertex_id, vertex_weight = -1):
        if self.get_vertex(vertex_id) is None:
            self.num_vertices += 1
            if vertex_weight == -1:
                new_vertex = Vertex(vertex_id)
            else:
                new_vertex = Vertex(vertex_id, vertex_weight)
            self.vertices[vertex_id] = new_vertex
            return new_vertex
        if self.vertices[vertex_id].weight == -1:
            self.vertices[vertex_id].weight = vertex_weight


    def get_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


    def add_edge(self, vertex_1_id, vertex_2_id):
        if self.get_vertex(vertex_1_id) != None:
            self.add_vertex(vertex_1_id)
        if self.get_vertex(vertex_2_id) != None:
            self.add_vertex(vertex_2_id)

        self.vertices[vertex_1_id].add_neighbor(self.vertices[vertex_2_id])
        self.vertices[vertex_2_id].add_neighbor(self.vertices[vertex_1_id])


    def find_path(self, start_vertex, end_vertex, path = []):
        path += [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in list(self.vertices.keys()) or end_vertex not in list(self.vertices.keys()):
            return None
        for n in self.vertices[start_vertex].neighbors:
            if n not in path:
                extended_path = self.find_path(n, end_vertex, path)
                if extended_path:
                    return extended_path

        del path[-1]
        return None


    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ", " + str(self.vertices[key].weight) + " :" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()


    def __str__(self):
        """ Function to print a graph as adjacency list and adjacency matrix. """
        return str(self.adjacencyList())# + '\n' + '\n' + str(self.adjacencyMatrix())



class Node():
    def __init__(self):
        self.launch_id = 0
        self.launch_payload = -1
        self.weight = 0
        self.path_cost = 0
        self.modules_in_space = []
        self.launch_cost = 0
        self.launched = set()
        self.ancestor = None

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __cmp__(self, other):
        return cmp(self.path_cost, other.path_cost)

    def __str__(self):
        return "l_id: %d l_pay: %f wei: %f path_cost: %f modules in space: %s" % (self.launch_id, self.launch_payload, self.weight, self.path_cost, str(self.modules_in_space))


class Problem(Graph):
    def __init__(self, vertices_input):
        self.goal_state = set(vertices_input)
        self.vertices = vertices_input
        self.neighbors_modules_in_space = set()


    def path_cost_calculator(self, current_node, new_node, launch_obj):
        return (current_node.path_cost + launch_obj.launch_dict[new_node.launch_id].fixed_cost + new_node.weight*(launch_obj.launch_dict[new_node.launch_id].variable_cost))


    def launch_cost(self, new_node, launch_obj):
        new_node.launch_cost = launch_obj.launch_dict[new_node.launch_id].fixed_cost + new_node.weight*(launch_obj.launch_dict[new_node.launch_id].variable_cost)
        return  new_node.launch_cost

    def goal_test(self, current_node):
        if not self.goal_state.difference(set(current_node.modules_in_space)):
            print("\n Goal achieved!\n")
            return True
        else:
            return False

    # Calculates total weight od the nodes on Earth and the sum of the launches'payloads
    def weight_calculator(self, current_node, launch_obj):
        unlaunched_modules_weight = 0
        launches_weight = 0
        for i in set(self.vertices).difference(set(current_node.modules_in_space)):
            unlaunched_modules_weight += (self.vertices[i]).weight

        for key in set(launch_obj.launch_dict):
            if key > current_node.launch_id:
                launches_weight += (launch_obj.launch_dict[key]).max_payload

        if current_node.weight == 0 and current_node.launch_id != 0:
            launches_weight += launch_obj.launch_dict[current_node.launch_id].max_payload

        return unlaunched_modules_weight, launches_weight


    def check_if_neighbor_in_space(self, combination):
        for i in combination:
            if i in self.neighbors_modules_in_space:
                yield True


    def modules_connected(self, current_node, combination):
        neigh = set()
        extra_modules = set()

        for i in combination:
            neigh = neigh.union(set(self.vertices[i].neighbors))

        neigh = neigh.union(self.neighbors_modules_in_space)
        path_max = []

        for i in combinations(combination, 2):
            path = []
            self.find_path(list(i)[0], list(i)[1], path)
            if len(path) > len(path_max):
                path_max = path

        for j in path_max:
            if (j not in list(combination)):
                if current_node.modules_in_space and (j not in current_node.modules_in_space):
                    return False
                if not current_node.modules_in_space:
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


    def find_successor(self, launch_obj, current_node):
        count_successors = 0
        modules_on_earth = set(self.vertices).difference(set(current_node.modules_in_space))
        '''
        print("\n----------- NEW SUCCESSORS -----------\n")
        print("Modules on earth: ", modules_on_earth)
        print("Modules in space ", current_node.modules_in_space)
        print("Launches available")

        for key in launch_obj.launch_dict.keys():
            if key > current_node.launch_id:
                print("\tLaunch ", key, ": ", launch_obj.launch_dict[key])
        '''
        successors = dict()
        self.neighbors_modules_in_space = set()

        for i in current_node.modules_in_space:
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

            for x in combinations(modules_on_earth, n+1):
                count_comb += 1
                successors_id = set()


                #Checks if there is at least a module that is a neighbor of a module already in space, except for the first node with modules to be sent
                if current_node.modules_in_space and list(self.check_if_neighbor_in_space(x)) == []:
                    continue

                #Check if there is connection between modules
                if self.modules_connected(current_node, x) == False and n>0:
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
                    new_node = Node()
                    new_node.launch_id = current_node.launch_id + 1
                    new_node.launch_payload = launch_max_payload
                    new_node.weight = total_weight
                    new_node.path_cost = self.path_cost_calculator(current_node, new_node, launch_obj)
                    new_node.launch_cost = self.launch_cost(new_node, launch_obj)
                    new_node.launched = successors_id
                    new_node.ancestor = current_node
                    new_node.modules_in_space = current_node.modules_in_space + list(successors_id)
                    successors[frozenset(new_node.modules_in_space)] = new_node
                    total_weight = 0

            #if for a combination of n modules there are no successors to add there won't be for combinations with higher than n modules (weight is greater)
            if count_breaks == count_comb:
                break

        count_successors += 1
        new_node = Node()
        new_node.launch_id = current_node.launch_id + 1
        new_node.launch_payload = launch_max_payload
        new_node.weight = 0
        new_node.path_cost = self.path_cost_calculator(current_node, new_node, launch_obj)
        new_node.launch_cost = 0
        new_node.ancestor = current_node
        new_node.modules_in_space = current_node.modules_in_space
        successors[frozenset(new_node.modules_in_space)] = new_node

        return successors
