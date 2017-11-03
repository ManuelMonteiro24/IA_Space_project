"""File that contains the graph and the vertex class used in the search problem"""

class Vertex:
    """Class that represents a vertex of the graph used in the Problem. Each vertex is represented by the Module ID and contains its associated weight and a list of neighbors which represents the vertexes that it is connected to."""
    def __init__(self, id_vertex, weight = -1):
        self.id = id_vertex
        self.neighbors = []
        self.weight=weight

    def add_neighbor(self, neighbor):
        """Method that creates a connection between two vertexes by adding each one to the other neighbors list."""
        if isinstance(neighbor, Vertex):
            if neighbor.id not in self.neighbors:
                self.neighbors.append(neighbor.id)
                neighbor.neighbors.append(self.id)
        else:
            return False



class Graph:
    """Class that represents the graph used in the Problem. It has a dictionary indexed by the vertex id (Module ID) that contains all the vertexes in the graph."""
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        i=1


    def add_vertex(self, vertex_id, vertex_weight = -1):
        """Method that receives the data of a module and checks if it is already in the graph, if it isn't the vertex is created and added to the graph."""
        if self.get_vertex(vertex_id) is None:
            self.num_vertices += 1
            if vertex_weight > 0:
                new_vertex = Vertex(vertex_id, vertex_weight)
                self.vertices[vertex_id] = new_vertex
                return new_vertex
        return


    def get_vertex(self, vertex_id):
        """Method that receives a vertex id (Module name) and checks if it is on the graph"""
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


    def add_edge(self, vertex_1_id, vertex_2_id):
        """Method that receives the module id's from two modules and connects them both in the graph"""

        #the first or sencond module aren't already on the graph
        if self.get_vertex(vertex_1_id) == None or self.get_vertex(vertex_2_id) == None:
            return False

        self.vertices[vertex_1_id].add_neighbor(self.vertices[vertex_2_id])
        self.vertices[vertex_2_id].add_neighbor(self.vertices[vertex_1_id])


    def find_path(self, start_vertex, end_vertex, path = []):
        """Method that tries to find a path in the graph between a the start and the end vertexes received in the arguments. This is simply done through a recursive search through the neighbors as long as we advance in the path. Is no path is found None is returned."""
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

    def __str__(self):
        """Function to print a graph as adjacency list."""
        if len(self.vertices) >= 1:
                return [str(key) + ", " + str(self.vertices[key].weight) + " :" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return "Empty graph!"
