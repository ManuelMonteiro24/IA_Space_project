"""Function that contains the uniform search, breath search and depth search algorithm's"""

import strategy.modified_Queue, problem.problem, time
from problem.problem import *

def print_algorithm_information(iteration_count, elapsed_time):
    print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)

def uniform_search(problem, launches):
    "Function uniform cost general search algorithm implementation"

    frontier = strategy.modified_Queue.MyPriorityQueue()
    t = time.process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.add_node(initial_node)
    explored = set()

    while 1:
        iteration_count = iteration_count + 1
        if not frontier:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        first_node = frontier.get_node()
        #print(frontier)

        if problem.goal_test(first_node):
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return first_node

        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.actions(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):

                if frozenset(node.modules_in_space) not in explored:
                    if frontier.search(node) == True:
                        a = frontier.update(node)
                    else:
                        frontier.add_node(node)
                else:
                    if frontier.search(node) == False:
                        frontier.add_node(node)

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

def breath_search(problem, launches):
    "Function uniform cost general search algorithm implementation"

    frontier = []
    t = time.process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.append(initial_node)
    explored = set()

    while 1:
        iteration_count = iteration_count + 1
        if not frontier:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        first_node = frontier.pop(0)
        if problem.goal_test(first_node):
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return first_node

        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.find_successor(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):

                if (frozenset(node.modules_in_space) not in explored) and (node not in frontier):
                        frontier.append(node)

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

def depth_search(problem, launches):
    "Function uniform cost general search algorithm implementation"

    frontier = []
    t = time.process_time()
    iteration_count = 0

    initial_node = Node()
    frontier.append(initial_node)
    explored = set()

    while 1:
        iteration_count = iteration_count + 1
        if not frontier:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        first_node = frontier.pop()

        if problem.goal_test(first_node):
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return first_node

        explored.add(frozenset(first_node.modules_in_space))

        successors = problem.find_successor(launches, first_node)

        if successors != None and successors != False:
            for node in list(successors.values()):

                if (frozenset(node.modules_in_space) not in explored) and (node not in frontier):
                        frontier.append(node)

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False
