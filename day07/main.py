from itertools import product

def day_7(filename):

    equations = [line for line in open(filename).read().splitlines()]
    operators_p1 = ["+", "*"]
    operators_p2 = ["+", "*", "|"]
    total_p1 = 0
    total_p2 = 0

    for equation in equations:
        result = int(equation.split(":")[0])
        items = [int(x) for x in equation.split(":")[1].strip().split(" ")]

        result_found_p1 = False
        for ops in product(operators_p1, repeat=len(items) - 1):
            expression = str(items[0])
            current_result = 0
            for i, op in enumerate(ops):
                expression += f"{op}{items[i + 1]}"
                current_result = eval(expression)
                expression = str(current_result)
            if result == eval(expression):
                result_found_p1 = True
                break
        if result_found_p1:
            total_p1 += result

        result_found_p2 = False
        for ops in product(operators_p2, repeat=len(items) - 1):
            expression = str(items[0])
            current_result = 0
            for i, op in enumerate(ops):
                if op == "|":
                    expression = str(int(f"{expression}{str(items[i + 1])}"))
                else:
                    expression += f"{op}{items[i + 1]}"
                    current_result = eval(expression)
                    expression = str(current_result)
            if result == eval(expression):
                result_found_p2 = True
                break
        if result_found_p2:
            total_p2 += result

    return total_p1, total_p2

def test_day_7():
    # Test for Part 1 and Part 2
    assert day_7("test.txt") == (3749, 11387)

test_day_7()

p1, p2 = day_7("input.txt")
print("Part 1: ", p1)
print("Part 2: ", p2)