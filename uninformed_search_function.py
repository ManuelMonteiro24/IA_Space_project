import strategy.stack
import graphs.graph_struct

def general_search(problem, strategy, launches):


    initial_node = Node()
    strategy.add(initial_node.path_cost, initial_node)
    explored = set()

    while:
        if strategy.empty():
            return False

        node = strategy.get()

        if problem.goal_test(node):
            return node
        explored.add(node.modules_in_space)

        successors = problem.find_successor(launches, node)

        for child_node in successors.values():
            explored.add(child_node.modules_in_space)

            for node in strategy.queue:
                if node.modules_in_space == child_node.modules_in_space and child_node.path_cost <= node.path_cost :
                        strategy.queue.remove(node)
                        strategy.add(child_node.path_cost, child_node)
                        break
