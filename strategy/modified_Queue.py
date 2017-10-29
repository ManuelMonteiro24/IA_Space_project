from graphs.graph_struct import Node

class MyPriorityQueue():
    """Our implemented version of a PriorityQueue, where the priority element is the node.path_cost and the nodes with the lowest path cost get in begging of the list"""

    def __init__(self):
        self.list = list()
        self.list_size = 0

    def add_node(self, new_node):
        if self.list_size == 0:
            self.list.append(new_node)
        else:
            for node in self.list:
                if new_node <= node:
                    self.list.insert(0,new_node)
                    self.list_size = self.list_size + 1
                    break

    def search_node(self, new_node):
        """search the list for node with the same state (modules_in_space)"""
        if self.list_size == 0:
            return False
        else:
            for node in self.list:
                if new_node.modules_in_space == node.modules_in_space:
                        if new_node < node:
                            self.list.remove(node)
                            self.add_node(new_node)
                        break
