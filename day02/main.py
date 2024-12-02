def read_input(filename):
    lines = [line.strip() for line in open(filename, "r")]
    return lines

def day_2(filename):

    matrix = read_input(filename)
    countP1 = 0
    countP2 = 0

    for line in matrix:
        valid = False
        report = [int(x) for x in line.split()]
        valid = test_reports(report)
        if valid:
            countP1 += 1
            countP2 += 1

        if not valid:
            for i in range(0, len(report)):
                new_report = report.copy()
                new_report.pop(i)
                valid = test_reports(new_report)
                if valid:
                    countP2 += 1
                    break

    return countP1, countP2

def test_reports(report):

    if report[0] < report[1]:
        report = report[::-1]

    valid = True
    for i in range(0, len(report) - 1):

        diff = abs(report[i] - report[i + 1])

        if report[i] < report[i + 1]:
            valid = False
            break
        if diff < 1 or diff > 3:
            valid = False
            break

    return valid

def test_day_2():
     assert day_2("test.txt") == (2, 4)

test_day_2()

p1, p2 = day_2("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
