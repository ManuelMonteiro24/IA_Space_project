"""File that contains the A* search algorithm"""

import strategy.modified_Queue, heuristic, time
from problem.problem import *

def print_algorithm_information(iteration_count, elapsed_time):
    print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)

def a_star_search(problem, launches, heuristic):
    "Function uniform cost general search algorithm implementation"

    frontier = strategy.modified_Queue.MyPriorityQueue()

    t = time.process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.add_node(initial_node, heuristic, problem.vertices, launches)
    explored = set()

    while 1:
        iteration_count = iteration_count + 1
        if not frontier.list:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        first_node = frontier.get_node()

        if problem.goal_test(first_node):
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return first_node

        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.find_successor(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):

                if frozenset(node.modules_in_space) not in explored:
                    if frontier.search(node) == True:
                        frontier.update(node, heuristic, problem.vertices, launches)
                    else:
                        frontier.add_node(node, heuristic, problem.vertices, launches)
                else:
                    if frontier.search(node) == False:
                        frontier.add_node(node, heuristic, problem.vertices, launches)

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False
