import re

def read_input(filename):
    lines = [line.strip() for line in open(filename, "r")]
    return "".join(lines)


def calculate(substring):
    matches = re.findall(r"mul\(\d+,\d+\)", substring)
    t = 0

    for m in matches:
        match = re.search(r"mul\((\d+),(\d+)\)", m)
        if match:
            x, y = map(int, match.groups())
            t += x * y
    return t

def day_3_p1(filename):

    line = read_input(filename)
    t = calculate(line)

    return t

def day_3_p2(filename):

    remaining = read_input(filename)
    t = 0

    while True:
        do = remaining.find("do()")
        dont = remaining.find("don't()")

        if (do == -1 and dont == -1) or (do != -1 and dont == -1):
            t += calculate(remaining)
            break

        if dont != -1 and do == -1:
            to_calculate = remaining[:dont]
            t += calculate(to_calculate)
            break

        if do < dont:
            to_calculate = remaining[:dont]
            t += calculate(to_calculate)
            next_fragment = remaining[dont+7:]
            next_do = next_fragment.find("do()")
            if next_do == -1:
                break
            else:
                remaining = next_fragment[next_do+4:]

        if dont < do:
            to_calculate = remaining[:dont]
            t += calculate(to_calculate)
            remaining = remaining[do+4:]

    return t

def test_day_3():
     assert day_3_p1("test.txt") == 161
     assert day_3_p2("test2.txt") == 48

test_day_3()

p1 = day_3_p1("input.txt")
p2 = day_3_p2("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
