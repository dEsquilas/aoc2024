from itertools import product

def read_input(filename):
	map = [[c for c in line] for line in open(filename).read().splitlines()]
	antenas_by_type = {}

	for y, x in product(range(len(map)), range(len(map[0]))):
		if map[y][x] != '.':
			if map[y][x] not in antenas_by_type:
				antenas_by_type[map[y][x]] = []
			antenas_by_type[map[y][x]].append((y, x))

	return antenas_by_type, len(map), len(map[0])

def day_8_p1(filename):

	antenas_by_type, h, w = read_input(filename)

	antinodes_p1 = set()
	antinodes_p2 = set()

	for (key, antennas) in antenas_by_type.items():
		for i in range(len(antennas)):
			for j in range(i+1, len(antennas)):
				current = antennas[i]
				next = antennas[j]
				director_vector = ((current[0] - next[0]), (current[1] - next[1]))

				potencial_antinodes = [
					(current[0] - director_vector[0], current[1] - director_vector[1]),
					(next[0] - director_vector[0], next[1] - director_vector[1]),
					(current[0] + director_vector[0], current[1] + director_vector[1]),
					(next[0] + director_vector[0], next[1] + director_vector[1])
				]

				for n in potencial_antinodes:
					if validate_node(n, w, h) and n not in antennas:
						antinodes_p1.add(n)

	return len(antinodes_p1), 34

def validate_node(node, width, height):
	return 0 <= node[0] < height and 0 <= node[1] < width

def test_day_8():
	assert day_8_p1("test.txt") == (14, 34)

test_day_8()

# p1, p2 = day_8_p1("input.txt")
# print("Part 1: ", p1)
# print("Part 2: ", p2)
