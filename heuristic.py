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
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	weight_on_earth = 0
	total_weight = 0
	var_cost_max_pay_list = list ()

	aux_flag = 0
	aux_node = node

	if node.weight == 0:
		while aux_node.ancestor != None:
			if aux_node.weight != 0:
				launch_id = aux_node.launch_id
				aux_flag = 1
				break
			aux_node = aux_node.ancestor
		if aux_flag == 0:
			launch_id = 1
	else:
		launch_id = node.launch_id

	for n in modules_on_earth:
		weight_on_earth += vertices[n].weight

	for n in vertices.keys():
		total_weight += vertices[n].weight

	aux = launch_id
	while aux <= len(launches.launch_dict):
		var_cost_max_pay_list.append(launches.launch_dict[aux].variable_cost* launches.launch_dict[launch_id].max_payload)
		aux +=1

	index_max = launch_id + var_cost_max_pay_list.index(max(var_cost_max_pay_list))
	return max(var_cost_max_pay_list)*weight_on_earth



def heuristic_3(node, vertices, launches):
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	weight_on_earth = 0
	total_weight = 0
	var_cost_max_pay_list = list ()

	if node.weight == 0:
		if node.launch_id > 1:
			launch_id = node.launch_id - 1
		else:
			return 0
	else:
		launch_id = node.launch_id

	for n in modules_on_earth:
		weight_on_earth += vertices[n].weight

	for n in vertices.keys():
		total_weight += vertices[n].weight

	aux = launch_id
	while aux <= len(launches.launch_dict):
		var_cost_max_pay_list.append(launches.launch_dict[aux].variable_cost*weight_on_earth/total_weight)
		aux += 1

	index_max = launch_id + var_cost_max_pay_list.index(max(var_cost_max_pay_list))
	return launches.launch_dict[index_max].variable_cost*total_weight

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
