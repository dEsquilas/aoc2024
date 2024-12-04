def read_input(filename):
    lines = [list(line.strip()) for line in open(filename, "r")]
    return lines

def day_3_p1(filename):
    matrix = read_input(filename)

    positions = [
        [(0, 1),(0, 2),(0, 3)],
        [(1, 0),(2, 0),(3, 0)],
        [(1, 1),(2, 2),(3, 3)],
        [(0, -1), (0, -2), (0, -3)],
        [(-1, 0), (-2, 0), (-3, 0)],
        [(-1, -1), (-2, -2), (-3, -3)],
        [(1, -1), (2, -2), (3, -3)],
        [(-1, 1), (-2, 2), (-3, 3)],
    ]

    t = 0

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            for position in positions:
                try:
                    if (matrix[x][y] == 'X' and
                        matrix[validateIndex(x, position[0][0])][validateIndex(y, position[0][1])] == "M" and
                        matrix[validateIndex(x, position[1][0])][validateIndex(y, position[1][1])] == "A" and
                        matrix[validateIndex(x, position[2][0])][validateIndex(y, position[2][1])] == "S"

                    ):
                        t += 1
                except Exception as e:
                    pass

    return t


def day_3_p2(filename):
    matrix = read_input(filename)
    positions = [
        [(1, 1),(-1,-1)],
        [(-1, -1),(1,1)],
        [(1, -1),(-1,1)],
        [(-1, 1),(1,-1)],
    ]

    t = 0

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == 'A':
                founded = 0
                for position in positions:
                    try:
                        if (matrix[validateIndex(x, position[0][0])][validateIndex(y, position[0][1])] == "M" and
                            matrix[validateIndex(x, position[1][0])][validateIndex(y, position[1][1])] == "S"):
                            founded += 1

                    except Exception as e:
                        pass
                if founded >= 2:
                    t += 1
    return t

def validateIndex(o, c):
    if o + c < 0:
        raise Exception("Invalid index")
    return o + c

def test_day_3():
    assert day_3_p1("test.txt") == 18
    assert day_3_p2("test.txt") == 9

test_day_3()

p1 = day_3_p1("input.txt")
p2 = day_3_p2("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
