def read_input(filename):
    lines = [line.strip() for line in open(filename, "r")]

    in_orders = True
    orders = []
    to_print = []

    for line in lines:
        if len(line) == 0:
            in_orders = False
            continue

        if in_orders:
            orders.append([int(x) for x in line.split("|")])

        if not in_orders:
            to_print.append([int(x) for x in line.split(",")])

    return orders, to_print


def day_3(filename):

    orders, to_print = read_input(filename)
    t1 = 0
    t2 = 0

    for p in to_print:
        if validate_order(orders, p):
            t1 += p[int(len(p) / 2)]
        else:
            rebuilded = rebuild_order(orders, p)
            t2 += rebuilded[int(len(rebuilded) / 2)]

    return t1, t2

def validate_order(orders, prints):
    valid = True

    for index in range(0, len(prints)):
        current = prints[index]
        remaining_prints = prints[index+1:]

        for order in orders:
            if current == order[0] and order[1] in prints and order[1] not in remaining_prints:
                valid = False
                break

    return valid

def rebuild_order(orders, prints):

    rebuilded = []

    for p in prints:
        if len(rebuilded) == 0:
            rebuilded.append(p)
            continue
        for position in range(len(rebuilded)+1):
            tmp_rebuilded = rebuilded.copy()
            tmp_rebuilded.insert(position, p)
            if validate_order(orders, tmp_rebuilded):
                rebuilded = tmp_rebuilded
                break

    return rebuilded

def test_day_3():
    assert day_3("test.txt") == (143, 123)


test_day_3()

p1, p2 = day_3("input.txt")

print("Part 1: ", p1)
print("Part 2: ", p2)
