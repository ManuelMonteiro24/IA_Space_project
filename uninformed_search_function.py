import strategy.stack
from graphs.graph_struct import *

def general_search(problem, strategy, launches):


    initial_node = Node()
    strategy.put(initial_node, initial_node.path_cost)
    explored = set()

    while 1:
        if strategy.empty():
            return False

        node = strategy.get()

        if problem.goal_test(node):
            return node
        explored.add(frozenset(node.modules_in_space))

        successors = problem.find_successor(launches, node)

        for child_node in successors.values():
            explored.add(frozenset(child_node.modules_in_space))

            for node in strategy.queue:
                if node.modules_in_space == child_node.modules_in_space and child_node.path_cost <= node.path_cost :
                        strategy.queue.remove(node)
                        strategy.put(child_node, child_node.path_cost)
                        break
