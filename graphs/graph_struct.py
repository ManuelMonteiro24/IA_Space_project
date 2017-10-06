class Vertex:
    def __init__(self, id_vertex, weight):
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
        
    def __repr__(self):
        return str(self.neighbors)