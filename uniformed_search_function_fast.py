from strategy.Queue_data import Queue, PriorityQueue
from graphs.graph_struct import *

def general_search(problem, frontier, launches):
    "Function uniform cost general search algorithm implementation, without the update section so it could run faster "

    iteration_count = 0

    initial_node = Node()
    frontier.append(initial_node)
    explored = set()

    while frontier:

        iteration_count = iteration_count + 1

        node = frontier.pop()

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
                    frontier.append(child_node)
    print("Iteration Count :", iteration_count)
    return False
