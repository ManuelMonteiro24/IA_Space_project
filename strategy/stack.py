from queue import PriorityQueue
#strategy struct for Dfs or iterative Dfs
class Stack:

    def __init__(self):
        self.lifo = []

    def add(self,node):
        self.lifo.append(node)

    def remove(self):
        return self.lifo.pop()


def strategy(successors,struct):
    min_path_cost = 0
    key_for_min_path_node = ""

    for key,value in successors.items():
        struct.put(value.path_cost,successors[key])

#codigo da estrutura para exportar para outro lado

struct = PriorityQueue()

next_item = struct.get() #pass to successor function
