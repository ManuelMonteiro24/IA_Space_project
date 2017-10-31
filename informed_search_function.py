from strategy.modified_Queue import MyPriorityQueue
from graphs.graph_struct import *
from time import process_time
import heuristic

def print_algorithm_information(iteration_count, elapsed_time):
    print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)

def general_search(problem, frontier, launches, heuristic):
    "Function uniform cost general search algorithm implementation"

    t = process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.add_node(initial_node, heuristic, launches)
    explored = set()

    while 1:
        iteration_count = iteration_count + 1
        if not frontier.list:
            elapsed_time = process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        first_node = frontier.get_node()
        #print(frontier)

        if problem.goal_test(first_node):
            elapsed_time = process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return first_node

        #print("\nFirst node: ", first_node)
        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.find_successor(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):
                #print("Node: ", node)

                if frozenset(node.modules_in_space) not in explored:
                    if frontier.search(node) == True:
                        a = frontier.update(node, heuristic, launches)
                        #print("\tA", a)
                    else:
                        #print("\tB")
                        frontier.add_node(node, heuristic, launches)
                else:
                    if frontier.search(node) == False:
                        #print("\tC")
                        frontier.add_node(node, heuristic, launches)

        if successors == False:
            elapsed_time = process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False
