
#strategy struct for Dfs or iterative Dfs
class Stack:

    def __init__(self):
        self.lifo = []

    def add(self,node):
        self.lifo.append(node)

    def remove(self):
        return self.lifo.pop()
