from strategy.modified_Queue import MyPriorityQueue
from graphs.graph_struct import *

def general_search(problem, frontier, launches):
    "Function uniform cost general search algorithm implementation"

    initial_node = Node()
    frontier.add_node(initial_node)
    explored = set()

    while 1:
        if not frontier.list:
            print("false empty")
            return False

        first_node = frontier.get_node()

        if problem.goal_test(first_node):
            print("Goal achieved!")
            return first_node

        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.find_successor(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):
                if frozenset(node.modules_in_space) not in explored:
                    if frontier.search(node) == True:
                        frontier.update(node)
                    else:
                        frontier.add_node(node)
                else:
                    if frontier.search(node) == False:
                        frontier.add_node(node)
        if successors == False:
            print("\nAbort! No solution!\n")
            return False
