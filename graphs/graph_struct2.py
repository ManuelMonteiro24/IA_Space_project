from itertools import combinations


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


    def check_connection(self, list_vertices, n=0):
        if n < len(list_vertices)-1:
            for i in list_vertices[n+1:]:
                if i in  self.vertices[list_vertices[n]]:
                    continue
                else
                    self.check_connection(list_vertices, n+1)
        return 


    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ", " + str(self.vertices[key].weight) + " :" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()


    def toString(self):
        """ Function to print a graph as adjacency list and adjacency matrix. """
        return str(self.adjacencyList())# + '\n' + '\n' + str(self.adjacencyMatrix())



class Node():
     def __init__(self):
        launch_id = ''
        launch_payload = -1
        weight = -1
        path_cost = 0
        modules_sent_to_space = set()


class Problem(Graph):
    def __init__(self, vertices_input, current_node):
        self.launches_used = []
        self.goal_state = set(vertices_input)
        self.vertices = vertices_input
        self.neighbors_modules_in_space = set()


    def path_cost_calculator(self, current_node, new_node, launches_dict):
        return current_node.path_cost + launches_dict(new_node.launch_id)[1] + new_node.weight*launches_dict(new_node.launch_id)[2] 


    def goal_test(self):
        if not (goal_state.intersection(current_node.modules_in_space)):
            print("\n Goal achieved!\n")
            return True
        else:
            return False

    # Calculates total weight od the nodes on Earth and the sum of the launches'payloads 
    def weight_calculator(self, current_node, launches_dict):

        unlaunched_modules_weight = 0
        launches_weight = 0

        for i in ((self.vertices).difference(current_node.modules_in_space)):
            unlaunched_modules_weight += (self.vertices[i]).weight 

        for i in set(launches_dict):
            launches_weight += (launches_dict[i])[0]
        
        return unlaunched_modules_weight, launches_weight


    def check_if_neighbor_in_space(self, combination): 
        for i in combination:
            if i in self.neighbors_modules_in_space:
                yield True


    def neighborhood(self, combination):
        neigh = set()
        for i in  combination:
            for n in self.vertices[i].neighbors:
                neigh.add(n)

        for i in combination:
            if i not in combination:
                yield False


    def find_successor(self, launches_dict, current_node):
        modules_on_earth = set(self.vertices).difference(current_node.modules_in_space)
        successors = {None: 0}

        unlaunched_modules_weight, launches_weight = self.weight_calculator(current_node, launches_dict)

        #Check if launches available are enough to send the modules on Earth
        if launches_weight < unlaunched_modules_weight
            return False

        launch_max_payload = launches_dict[list(launches_dict.keys())[0]][0]

        for n in range(len(modules_on_earth)):

            total_weight = 0
            count_comb = 0
            count_breaks = 0

            for x in combinations(modules_on_earth, n+1):
                count_comb += 1
                str_successor = ''

                #Checks if there is at least a module that is a neighbor of a module already in space
                if list(self.check_if_neighbor_in_space(x)) == []:
                    count_breaks += 1
                    break

                #Check if there is connection between modules
                if False in set(self.neighborhood(x)):
                    count_breaks += 1
                    break

                #Check if launch max. payload is enough to send the set of modules
                for i in x:
                    total_weight += self.vertices[i].weight              
                    if total_weight > launch_max_payload:
                        total_weight = 0
                        count_breaks += 1
                        break                    
                    str_successor += self.vertices[i].id     

                if total_weight != 0:
                    new_node = Node()
                    new_node.launch_id = list(launches_dict.keys())[0] 
                    new_node.launch_payload = launches_dict[new_node.launch_id][0]
                    new_node.weight = total_weight
                    new_node.path_cost = self.path_cost_calculator(current_node, new_node, launches_dict):
                    successors[str_successor] = new_node
                    del launches_dict[list(launches_dict.keys())[0]]
                    total_weight = 0

            #if for a combination of n modules there are no successors to add there won't be for combinations with higher than n modules (weight is greater)
            if count_breaks == count_comb:
                break

        return successors

