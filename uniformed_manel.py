from strategy.stack import Queue, PriorityQueue
from graphs.graph_struct import *

def general_search(problem, strategy, launches):

    iteration_count = 0

    initial_node = Node()
    strategy.append(initial_node)
    explored = set()

    while strategy:

        iteration_count = iteration_count + 1

        node = strategy.pop()

        if problem.goal_test(node):
            print("Iteration Count :", iteration_count)
            return node

        explored.add(frozenset(node.modules_in_space))

        successors = problem.find_successor(launches, node)
        if successors == False:
            print("Iteration Count :", iteration_count)
            return False
        else:
            for child_node in successors.values():
                if frozenset(child_node.modules_in_space) not in explored:
                    strategy.append(child_node)
    print("Iteration Count :", iteration_count)
    return False
