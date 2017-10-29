from strategy.queue_data import Queue, PriorityQueue
from graphs.graph_struct import *
from time import process_time

def general_search(problem, frontier, launches):
    """Function uniform cost general search algorithm implementation, without the update section so it could run faster"""

    t = process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.append(initial_node)
    explored = set()

    while frontier:

        iteration_count = iteration_count + 1

        node = frontier.pop()

        if problem.goal_test(node):
            elapsed_time = process_time() - t
            print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)
            return node

        explored.add(frozenset(node.modules_in_space))

        successors = problem.find_successor(launches, node)
        if successors == False:
            elapsed_time = process_time() - t
            print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)
            return False
        else:
            for child_node in successors.values():
                if frozenset(child_node.modules_in_space) not in explored:
                    frontier.append(child_node)
                elif child_node in frontier:
                    test_node = frontier.get(child_node)
                    if child_node < test_node:
                        frontier.delete(test_node)
                        frontier.append(child_node)

    elapsed_time = process_time() - t
    print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)
    return False
