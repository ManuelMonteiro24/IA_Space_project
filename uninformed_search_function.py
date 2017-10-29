import strategy.stack
from queue import PriorityQueue
from graphs.graph_struct import *

def general_search(problem, strategy, launches):

    initial_node = Node()
    strategy.put(initial_node)
    explored = set()

    while 1:
        if strategy.empty():
            print("false empty")
            return False

        node = strategy.get()

        if problem.goal_test(node):
            return node
        explored.add(frozenset(node.modules_in_space))

        successors = problem.find_successor(launches, node)

        if successors == False:
            print("false successors")
            return False
        else:
            for child_node in successors.values():
                if frozenset(child_node.modules_in_space) not in explored:
                    strategy.put(child_node)
                else:
                    aux_strategy = PriorityQueue()
                    while strategy.empty() != True:
                        node = strategy.get()
                        if (node.modules_in_space == child_node.modules_in_space) and (child_node.path_cost <= node.path_cost) :
                            aux_strategy.put(child_node)
                        else:
                            aux_strategy.put(node)
                            break
                    strategy = aux_strategy
