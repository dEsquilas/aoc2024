from itertools import product

def read_input(filename):
	map = [[c for c in line] for line in open(filename).read().splitlines()]
	antennas_by_type = {}

	for y, x in product(range(len(map)), range(len(map[0]))):
		if map[y][x] != '.':
			if map[y][x] not in antennas_by_type:
				antennas_by_type[map[y][x]] = []
			antennas_by_type[map[y][x]].append((y, x))

	return antennas_by_type, len(map), len(map[0])

def day_8_p1(filename):

	antennas_by_type, h, w = read_input(filename)

	antinodes_p1 = set()
	antinodes_p2 = set()

	for (key, antennas) in antennas_by_type.items():
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
					if validate_node(n, w, h) and n != current and n != next:
						antinodes_p1.add(n)

				antinodes_p2.add(current)
				antinodes_p2.add(next)

				for d in [0, 1]:
					current_pt = antennas[i]
					while True:
						direction = 1 if d == 1 else -1
						potencial_antinode = (
							current_pt[0] + direction * director_vector[0],
							current_pt[1] + direction * director_vector[1])
						if not validate_node(potencial_antinode, w, h):
							break
						antinodes_p2.add(potencial_antinode)
						current_pt = potencial_antinode

	return len(antinodes_p1), len(antinodes_p2)

def validate_node(node, width, height):
	return 0 <= node[0] < height and 0 <= node[1] < width

def test_day_8():
	assert day_8_p1("test.txt") == (14, 34)

test_day_8()

p1, p2 = day_8_p1("input.txt")
print("Part 1: ", p1)
print("Part 2: ", p2)
