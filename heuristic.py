"""File that contains the heuristic's functions"""

def heuristic_1(node, vertices, launches):
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	total_weight = 0
	avg_var_cost = 0

	if node.weight == 0:
		return 0

	for n in modules_on_earth:
		total_weight += vertices[n].weight

	for l in launches.launch_dict.values():
		avg_var_cost +=  l.variable_cost
	avg_var_cost = avg_var_cost/len(launches.launch_dict)

	return total_weight*avg_var_cost

#melhor ate agora
def heuristic_2(node, vertices, launches):
	total_weight = 0
	if node.weight == 0:
		return 0

	launch_id = node.launch_id
	var_cost_max_pay_list = list ()

	while launch_id <= len(launches.launch_dict):
		var_cost_max_pay_list.append(launches.launch_dict[launch_id].variable_cost* launches.launch_dict[launch_id].max_payload)
		launch_id += 1

	modules_on_earth = set(vertices).difference(node.modules_in_space)
	for n in modules_on_earth:
		total_weight += vertices[n].weight

	return max(var_cost_max_pay_list)*total_weight


def EBF(N, d):
	b=1	
	delta = 10
	while delta > 0.1:
		N_aux = 0
		for i in range(1, d+1):
			N_aux += b**i
		delta = abs(N_aux - N)
		b += 0.00001

	return b 

