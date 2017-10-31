from graphs.graph_struct import *
from heuristic import *

class MyPriorityQueue():
    """ Implementation of a Priority Queue with methods adapted to our problem """

    def __init__(self):
        self.list = list()
        self.list_size = 0

    def add_node(self, new_node, heuristic = None, launches = None):
        if self.list_size == 0:
            self.list.append(new_node)
            self.list_size = self.list_size + 1
        else:
            count = 0
            for node in self.list:
                if heuristic == None:
                    if new_node < node:
                        self.list.insert(count,new_node)
                        self.list_size = self.list_size + 1
                        return
                else:
                    if (new_node.path_cost + heuristic(new_node, launches)) < (node.path_cost + heuristic(node,  launches)):
                        self.list.insert(count,new_node)
                        self.list_size = self.list_size + 1
                        return
                count += 1
            self.list.append(new_node)
            self.list_size = self.list_size + 1
            return

    def update(self, new_node, heuristic = None, launches = None):
        if self.list_size == 0:
            return False
        else:
            for node in self.list:
                if len(node.modules_in_space) == len(new_node.modules_in_space) and not new_node.modules_in_space.difference(node.modules_in_space):
                    if heuristic == None:
                        if new_node < node:
                            self.list.remove(node)
                            self.list_size = self.list_size - 1
                            self.add_node(new_node)
                            return True
                    else:
                        if (new_node.path_cost + heuristic(new_node, launches)) < (node.path_cost + heuristic(node, launches)):
                            self.list.remove(node)
                            self.list_size = self.list_size - 1
                            self.add_node(new_node)
                            return True
            return False

    def search(self, node):
        for n in self.list:
            if len(n.modules_in_space) == len(node.modules_in_space):
                if not node.modules_in_space.difference(n.modules_in_space):
                    return True
        return False

    def get_node(self):
        priority_node = self.list[0]
        self.list.remove(priority_node)
        self.list_size = self.list_size - 1
        return priority_node

    def __str__(self):
        return_str = ""
        for node in self.list:
            return_str += str(node) + " "
        return return_str
