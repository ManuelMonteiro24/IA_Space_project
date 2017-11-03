"""File that contains the heuristic's functions"""

def heuristic_1(node, vertices, launches):
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	total_weight = 0

	for n in modules_on_earth:
		total_weight += vertices[n].weight

	return total_weight

#melhor ate agora
def heuristic_2(node, vertices, launches):
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	total_weight = 0

	if node.weight == 0:
		return 0

	for n in modules_on_earth:
		total_weight += vertices[n].weight

	launch_id = node.launch_id
	var_cost_max_pay_list = list ()

	while launch_id <= len(launches.launch_dict):
		var_cost_max_pay_list.append(launches.launch_dict[launch_id].variable_cost* launches.launch_dict[launch_id].max_payload)
		launch_id += 1

	return max(var_cost_max_pay_list)
