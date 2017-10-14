
class Vertex:
    def __init__(self, id_vertex, weight = -1):
        self.id = id_vertex
        self.neighbors = []
        self.weight=weight
        self.launched=False

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

    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ", " + str(self.vertices[key].weight) + " :" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()

    def toString(self):
        """ Function to print a graph as adjacency list and adjacency matrix. """
        return str(self.adjacencyList())# + '\n' + '\n' + str(self.adjacencyMatrix())



class Node():
     def __init__(self, launch_id_input):
        launch_id = launch_id_input
        modules_sent_to_space = set()



class Problem(graph_obj):
    def __init__(self):
        launches_used = []
        modules_in_space = set()
        goal_state = set(graph_obj.vertices)

    def step_cost(self, f_cost, v_cost, weight):
        return f_cost+v_cost*weight


    def goal_test(self, modules_in_space, goal):
        if not set(goal_state).difference(modules_in_space)
            print("\n Goal achieved!\n")
            return True
        else
            return False

    # Calculates de total maximum payload of the launched unused and the total weight od the nodes on Earth.
    # Operators: info of the available launches
    def weight_calculator(self, operators, current_state):
        unused_launches_weight = 0
        unlaunched_nodes_weight = 0

        for i in operators:
            total_weight +=  operators[list(operators)[i]]

        for i in (modules_in_space).difference(set(vertices)):
            unlaunched_nodes_weight += vertices[i].weight 
        
        return unused_launches_weight, unlaunched_nodes_weight


    def successor_function(self, current_state, operators, current_state):
        if current_state == goal_state
            return None        

        max_payload_launches, unlaunched_nodes_weight = weight_calculator(operators)

        if max_payload_launches >= unlaunched_nodes_weight

            #I can launch 
            for i in operators:
                for j in set


            #update launches in operators, modules_in_space

        else
            #Payload of the launches avaibable is not enough
            print("No solution!\n")
            return False
