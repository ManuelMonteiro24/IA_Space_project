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

    #TODO understand
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, vertex_id, vertex_weight = -1):
        if self.get_vertex(vertex_id) is None:
            self.num_vertices += self.num_vertices
            if vertex_weight == -1:
                new_vertex = Vertex(vertex_id)
            else:
                new_vertex = Vertex(vertex_id,vertex_weight)
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
    '''
    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(self.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
            import numpy as np
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in self.vertices[self.vertex_names[i]]:
                        j = self.vertex_indices[el]
                        self.adjacency_matrix[i,j] = 1
            return self.adjacency_matrix
        else:
            return dict()
    '''
    def toString(self):
        """ Function to print a graph as adjacency list and adjacency matrix. """
        return str(self.adjacencyList())# + '\n' + '\n' + str(self.adjacencyMatrix())
