
#strategy struct for Dfs or iterative Dfs
class Stack:

    def __init__(self):
        self.lifo = []

    def stack_push(self,node):
        self.lifo.append(node)

    def stack_pop(self):
        return self.lifo.pop()
