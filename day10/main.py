from itertools import product

def read_input(filename):
	map = [[-1 if c == "." else int(c) for c in line] for line in open(filename).read().splitlines()]
	
	return map

def validate_node(node, map):
	w = len(map[0])
	h = len(map)

	if 0 <= node[0] < h and 0 <= node[1] < w:
		return True
	else:
		return False

def navigate_next_node(map, visited, current):

	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	paths = []
	current_value = map[current[0]][current[1]]
	visited.add(current)

	#print(current, " -> ", current_value)

	if current_value == 5:
		return [[current]]

	for d in directions:
		next_node = current[0] + d[0], current[1] + d[1]
		if not validate_node(next_node, map):
			continue
		next_node_value = map[next_node[0]][next_node[1]]
		if (
				next_node_value == current_value + 1 and
				next_node not in visited
		):
			new_paths = navigate_next_node(map, visited, next_node)
			if new_paths != False:
				for p in new_paths:
					paths.append(p)

	if len(paths) == 0:
		return False

	for p in paths:
		p.append(current)

	return paths




def day_10(filename):

	map = read_input(filename)
	zeros = set()

	for (x, y) in product(range(len(map)), range(len(map[0]))):
		if map[y][x] == 0:
			zeros.add((y, x))

	t = 0
	for zero in zeros:
		paths = navigate_next_node(map, set(), zero)
		print("Paths founded")
		for p in paths:
			print(p)
		t += len(paths)

	return t,0
#
# def test_day_10():
# 	assert day_10("test.txt") == (36, 0)
#
# test_day_10()
# #
# p1, p2 = day_10("input.txt")
# print("Part 1: ", p1)
# print("Part 2: ", p2)

print(day_10("test2.txt"))
