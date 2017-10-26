import strategy.stack
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
                if frozenset(child_node.modules_in_space) not in explored:
                    print(child_node.path_cost)
                    for i in strategy.items()
                        temp = strategy.queue.get()
                        queue.put(temp)
                        print temp
                    strategy.put((child_node.path_cost, child_node))
                else:
                    for node in strategy.queue:
                        node = node = list(node)[1]
                        if node.modules_in_space == child_node.modules_in_space and child_node.path_cost <= node.path_cost :
                            strategy.queue.remove(node)
                            strategy.put((child_node.path_cost, child_node))
                            break
