def read_input(filename):
    lines = [line.strip() for line in open(filename, "r")]

    l = [int(x.split('   ')[0]) for x in lines]
    r = [int(x.split('   ')[1]) for x in lines]

    return l, r



def day_1_p1(filename):
    l, r = read_input(filename)

    l.sort()
    r.sort()

    total = 0

    for i in range(len(l)):
        total += abs(r[i] - l[i])

    return total


def day_1_p2(filename):
    l, r = read_input(filename)
    total = 0

    for i in range(len(l)):
        total += l[i] * r.count(l[i])

    return total


def test_day_1_p1():
     assert day_1_p1("test.txt") == 11

def test_day_1_p2():
     assert day_1_p2("test.txt") == 31



test_day_1_p1()
test_day_1_p2()

p1 = day_1_p1("input.txt")
p2 = day_1_p2("input.txt")


print("Part 1: ", p1)
print("Part 2: ", p2)
