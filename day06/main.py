from collections import defaultdict
from itertools import product

def day_6(filename):

    matrix = [[c for c in line] for line in open(filename).read().splitlines()]
    t1 = 0
    t2 = 0

    t1 = count_visited_nodes(matrix)

    for (x, y) in product(range(len(matrix[0])), range(len(matrix))):
        if matrix[y][x] != "#" and matrix[y][x] != "^":
            new_blocked_matrix = [row.copy() for row in matrix]
            new_blocked_matrix[y][x] = "#"
            if count_visited_nodes(new_blocked_matrix) == None:
                t2 += 1

    return t1, t2

def count_visited_nodes(matrix, debug=False):

    guard_direction_index = 0  # 0 = up, 1 = right, 2 = down, 3 = left
    guard_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    guard_position = None
    edges = set()
    visited = set()
    horizontal_blocks = {}
    vertical_blocks = {}

    for (x, y) in product(range(len(matrix[0])), range(len(matrix))):
        if matrix[y][x] == "#":
            if not y in horizontal_blocks:
                horizontal_blocks[y] = []
            if not x in vertical_blocks:
                vertical_blocks[x] = []
            horizontal_blocks[y].append(x)
            vertical_blocks[x].append(y)
        if matrix[y][x] == "^":
            guard_position = (y, x)

    while (True):

        initial_guard_position = guard_position
        rge = float('-inf')
        rgs = float('inf')
        new_guard_position = None

        if guard_direction_index == 0 or guard_direction_index == 2:

            if guard_position[1] not in vertical_blocks.keys():
                if guard_direction_index == 0:
                    rgs, rge = float('-inf'), guard_position[0]
                    new_guard_position = (float('-inf'), guard_position[1])
                if guard_direction_index == 2:
                    rgs, rge = guard_position[0], float('inf')
                    new_guard_position = (guard_position[1], float('inf'))
            else:
                interval = find_block_interval(guard_position[0], vertical_blocks[guard_position[1]])
                coord_direction = guard_direction[guard_direction_index][0]
                if guard_direction_index == 0:
                    new_guard_position = (interval[0] + coord_direction, guard_position[1])
                if guard_direction_index == 2:
                    new_guard_position = (interval[1] + coord_direction, guard_position[1])

                rgs = min(initial_guard_position[0], new_guard_position[0])
                rge = max(initial_guard_position[0], new_guard_position[0])

        if guard_direction_index == 1 or guard_direction_index == 3:

            if guard_position[0] not in horizontal_blocks.keys():
                if guard_direction_index == 1:
                    rgs, rge = guard_position[1], float('inf')
                    new_guard_position = (float("-inf"), guard_position[0])
                if guard_direction_index == 3:
                    rgs, rge = float('-inf'), guard_position[1]
                    new_guard_position = (guard_position[0], float('inf'))
            else:
                interval = find_block_interval(guard_position[1], horizontal_blocks[guard_position[0]])
                coord_direction = guard_direction[guard_direction_index][1]
                if guard_direction_index == 1:
                    new_guard_position = (guard_position[0], interval[1] - coord_direction)
                if guard_direction_index == 3:
                    new_guard_position = (guard_position[0], interval[0] - coord_direction)

                rgs = initial_guard_position[1]
                rge = new_guard_position[1]


        if rgs == float('-inf'):
            rgs = 0
        if rgs == float('inf'):
            rgs = len(matrix) - 1

        if rge == float('inf'):
            rge = len(matrix) - 1
        if rge == float('-inf'):
            rge = 0

        for i in range(min(rgs, rge), max(rgs, rge) + 1):
            if guard_direction_index == 0 or guard_direction_index == 2:
                visited.add((i, guard_position[1]))
            if guard_direction_index == 1 or guard_direction_index == 3:
                visited.add((guard_position[0], i))

        if (guard_position, new_guard_position) in edges or (new_guard_position, guard_position) in edges:
            return None


        edges.add((guard_position, new_guard_position))

        guard_position = new_guard_position
        guard_direction_index = turn_guard(guard_direction_index)

        if (guard_position[0] == float('-inf') or
                guard_position[0] == float('inf') or
                guard_position[1] == float('-inf')
                or guard_position[1] == float('inf')):
            break

    return len(visited)

def find_block_interval(guard_position, blocks):

    if guard_position < blocks[0]:
        return float('-inf'), blocks[0]
    if guard_position > blocks[-1]:
        return blocks[-1], float('inf')

    for i in range(len(blocks) - 1):
        if blocks[i] < guard_position < blocks[i + 1]:
            return blocks[i], blocks[i + 1]

    return None


def turn_guard(direction):
    direction += 1
    if direction > 3:
        direction = 0

    return direction


def debug_matrix(matrix, guard_position, guard_direction_index, visited):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (y, x) == guard_position:
                if guard_direction_index == 0:
                    print("^", end="")
                elif guard_direction_index == 1:
                    print(">", end="")
                elif guard_direction_index == 2:
                    print("v", end="")
                elif guard_direction_index == 3:
                    print("<", end="")
            elif (y, x) in visited:
                print("x", end="")

            else:
                print(matrix[y][x], end="")
        print()

    print("============================================")

def test_day_6():
    assert day_6("test.txt") == (41, 6)

test_day_6()

p1, p2 = day_6("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
