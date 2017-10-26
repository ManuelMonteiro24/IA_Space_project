import strategy.stack
from queue import PriorityQueue
from graphs.graph_struct import *

def general_search(problem, strategy, launches):


    initial_node = Node()
    strategy.put((initial_node.path_cost, initial_node))
    explored = set()

    while 1:
        if strategy.empty():
            print("false empty")
            return False

        node = strategy.get()
        node = list(node)[1]

        if problem.goal_test(node):
            return node
        explored.add(frozenset(node.modules_in_space))

        successors = problem.find_successor(launches, node)

        if successors == False:
            print("false successors")
            return False
        else:
            for child_node in successors.values():
                print("ola child node: ", node)
                if frozenset(child_node.modules_in_space) not in explored:
                    strategy.put((child_node.path_cost, child_node))
                else:
                    aux_strategy = PriorityQueue()
                    while strategy.empty() != True:
                        node = strategy.get()
                        node = node = list(node)[1]
                        if (node.modules_in_space == child_node.modules_in_space) and (child_node.path_cost <= node.path_cost) :
                            aux_strategy.put((child_node.path_cost, child_node))
                        else:
                            aux_strategy.put((node.path_cost, node))
                            break
                    strategy = aux_strategy
