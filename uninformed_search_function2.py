import strategy.stack
from queue import PriorityQueue
from graphs.graph_struct import *

def update_PriorityQueue(frontier, node):
    aux_queue = PriorityQueue()
    for i in frontier.queue:
        if i[1].modules_in_space != node.modules_in_space:
            aux_queue.put((i[0], i[1]))
        else:
            if i[0] > node.path_cost:
                aux_queue.put((node.path_cost, i[1]))
            else:
                aux_queue.put((i[0],i[1]))
    frontier = aux_queue

def in_PriorityQueue(frontier, node):
    for i in frontier.queue:
        if i[1].modules_in_space == node.modules_in_space:
            return True
    return False

def general_search(problem, frontier, launches):

    initial_node = Node()
    frontier.put((initial_node.path_cost, initial_node))
    explored = set()
    aux = 1

    while 1:
        if frontier.empty():
            print("false empty")
            return False

        print("Frontier ", frontier.queue)
        first_el = frontier.get()
    
        if problem.goal_test(first_el[1]):
            return first_el[1]

        print("\n", first_el[1].modules_in_space, "not a goal\n")
        explored.add(frozenset(first_el[1].modules_in_space))
        print("Explored: ", explored, "\n")

        successors = problem.find_successor(launches, first_el[1])

        if successors:
            for node in list(successors.values()):
                print("Node: ", node)
                in_frontier = in_PriorityQueue(frontier, node)
                print("\tIn frontier: ", in_frontier)
                print("\tIn explored: ", frozenset(node.modules_in_space) in explored)

                if frozenset(node.modules_in_space) not in explored:
                    if in_frontier == False:
                        print("\tA")
                        frontier.put((node.path_cost, node))
                    else: 
                        print("\tB")
                        update_PriorityQueue(frontier, node)

                else:
                    if in_frontier == False:
                        print("\tC")
                        frontier.put((node.path_cost, node)) 
                    else:
                        print("\tD")
                        update_PriorityQueue(frontier, node)

            