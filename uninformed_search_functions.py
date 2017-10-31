import time, graphs.graph_struct, strategy.modified_Queue

def print_algorithm_information(iteration_count, elapsed_time):
    print("Iteration Count :", iteration_count, "Time taken: ", elapsed_time)


def uniform_search(problem, launches):
    """Function uniform cost general search algorithm implementation"""

    frontier = strategy.modified_Queue.MyPriorityQueue()
    t = time.process_time()
    iteration_count = 0

    initial_node = graphs.graph_struct.Node()
    frontier.add_node(initial_node)
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

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        elif successors != None:
            for node in list(successors.values()):

                if frozenset(node.modules_in_space) not in explored:
                    if frontier.search(node) == True:
                        frontier.update(node)
                    else:
                        frontier.add_node(node)
                else:
                    if frontier.search(node) == False:
                        frontier.add_node(node)



def depth_search(problem, launches):
    """Function uniform cost general search algorithm implementation"""

    frontier = []
    t = time.process_time()
    iteration_count = 0

    initial_node = graphs.graph_struct.Node()
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

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        elif successors != None:
            for node in list(successors.values()):

                if frozenset(node.modules_in_space) not in explored:
                    frontier.append(node)
                else:
                    if node not in frontier:
                        frontier.append(node)



def breath_search(problem, launches):
    """Function uniform cost general search algorithm implementation"""

    frontier = []
    t = time.process_time()
    iteration_count = 0

    initial_node = graphs.graph_struct.Node()
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

        if successors == False:
            elapsed_time = time.process_time() - t
            print_algorithm_information(iteration_count, elapsed_time)
            return False

        elif successors != None:
            for node in list(successors.values()):

                if frozenset(node.modules_in_space) not in explored:
                    frontier.append(node)
                else:
                    if node not in frontier:
                        frontier.append(node)
