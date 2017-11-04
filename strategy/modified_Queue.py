from graphs.graph_struct import *

class MyPriorityQueue():
    """ Implementation of a Priority Queue with methods adapted to our problem."""

    def __init__(self):
        self.list = list()
        self.list_size = 0

    def add_node(self, new_node, heuristic = None, vertices = None, launches = None):
        """ Function that adds a node to the queue in regards its Priority."""

        if self.list_size == 0:
            #empty list case, insert in the beggining
            self.list.append(new_node)
            self.list_size = self.list_size + 1
        else:
            count = 0
            for node in self.list:
                #checks if heuristic function has received or not, and so if we have to take it in acount in the Priority of the nodes in the list
                if heuristic == None:
                    if new_node < node:
                        self.list.insert(count,new_node)
                        self.list_size = self.list_size + 1
                        return
                else:
                    if (new_node.path_cost + heuristic(new_node, vertices, launches)) < (node.path_cost + heuristic(node, vertices, launches)):
                        self.list.insert(count,new_node)
                        self.list_size = self.list_size + 1
                        return
                count += 1

            #insert in the end of the list
            self.list.append(new_node)
            self.list_size = self.list_size + 1
            return

    def update(self, new_node, heuristic = None, vertices = None, launches = None):
        """ Function updates a node in the queue for a node with the same state (modules_in_space) but lower priority."""
        if self.list_size == 0:
            #empty list case
            return False
        else:
            for node in self.list:
                #only update the node where state (modules in space) of both nodes are the same
                if len(node.modules_in_space) == len(new_node.modules_in_space) and not new_node.modules_in_space.difference(node.modules_in_space):
                    #checks if heuristic function has received or not, and so if we have to take it in acount in the Priority of the nodes in the list
                    if heuristic == None:
                        if new_node < node:
                            self.list.remove(node)
                            self.list_size = self.list_size - 1
                            self.add_node(new_node)
                            return True
                    else:
                        if (new_node.path_cost + heuristic(new_node, vertices, launches)) < (node.path_cost + heuristic(node, vertices, launches)):
                            self.list.remove(node)
                            self.list_size = self.list_size - 1
                            self.add_node(new_node)
                            return True
            return False
    '''
    def search(self, node):
        """Function that receives a node and checks if it is on the queue. The search is done by state (modules_in_space)."""
        for n in self.list:
            if len(n.modules_in_space) == len(node.modules_in_space):
                if not node.modules_in_space.difference(n.modules_in_space):
                    return True
        return False
    '''

    def search(self, node):
        """Function that receives a node and checks if it is on the queue. The search is done by state (modules_in_space)."""
        for n in self.list:
            if len(n.modules_in_space) == len(node.modules_in_space):
                if node.modules_in_space in n.modules_in_space:
                    return True
        return False
    

    def get_node(self):
        """Function that removes from the list and returns the node with highest priority."""
        priority_node = self.list[0]
        self.list.remove(priority_node)
        self.list_size = self.list_size - 1
        return priority_node

    def __str__(self):
        return_str = ""
        for node in self.list:
            return_str += str(node) + " "
        return return_str
