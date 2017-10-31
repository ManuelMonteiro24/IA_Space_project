def heuristic_1(node, launches):
    return node.weight

#melhor ate agora
def heuristic_2(node, launches):

    if node.weight == 0:
        return 0

    launch_id = node.launch_id
    var_cost_max_pay_list = list ()

    while launch_id <= len(launches.launch_dict):

        var_cost_max_pay_list.append(launches.launch_dict[launch_id].variable_cost* launches.launch_dict[launch_id].max_payload)

        launch_id += 1

    return max(var_cost_max_pay_list) * node.weight
