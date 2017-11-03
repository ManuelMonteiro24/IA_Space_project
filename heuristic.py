"""File that contains the heuristic's functions"""

def heuristic_1(node, vertices, launches):
	modules_on_earth = set(vertices).difference(node.modules_in_space)
	total_weight = 0
	var_cost = []

	if node.weight == 0:
		return 0

	for n in modules_on_earth:
		total_weight += vertices[n].weight

	for l in launches.launch_dict.values():
		var_cost.append(l.variable_cost)
	return total_weight*min(var_cost)


def EBF(N, d):
	b=1
	delta = 10
	while delta > 0.1:
		N_aux = 0
		for i in range(1, d+1):
			N_aux += b**i
		delta = abs(N_aux - N)
		b += 0.000001

	return b
