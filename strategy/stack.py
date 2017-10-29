from graphs.graph_struct import *

class Stack:

    def __init__(self):
        self.lifo = []

    def add(self,node):
        self.lifo.append(node)

    def remove(self):
        return self.lifo.pop()

class MyPriorityQueue():

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
        if self.list_size == 0:
            return False
        else:
            for node in self.list:
                if new_node.modules_in_space == node.modules_in_space:
                        if new_node < node:
                            self.list.remove(node)
                            self.add_node(new_node)
                        break
