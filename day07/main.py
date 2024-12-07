from itertools import product

def day_7_p1(filename):
    # Read equations from the file
    equations = [line for line in open(filename).read().splitlines()]
    operators = ["+", "*"]
    t = 0
    c = 0

    for (i, equation) in enumerate(equations):

        result = int(equation.split(":")[0])
        items = [int(x) for x in equation.split(":")[1].strip().split(" ")]
        result_found = False
        # Generate all combinations of operators
        for ops in product(operators, repeat=len(items) - 1):
            # Build the expression using numbers in the original order
            expression = str(items[0])
            cr = 0
            for i, op in enumerate(ops):
                expression += f"{op}{items[i + 1]}"
                cr = eval(expression)
                expression = str(cr)

            # Evaluate the expression
            if result == eval(expression):
                result_found = True
                break

        if result_found:
            t += result

    return t


def day_7_p2(filename):
    # Read equations from the file
    equations = [line for line in open(filename).read().splitlines()]
    operators = ["+", "*", "|"]
    t = 0

    for (i, equation) in enumerate(equations):

        print("Processing ", i)

        result = int(equation.split(":")[0])
        items = [int(x) for x in equation.split(":")[1].strip().split(" ")]
        result_found = False
        # Generate all combinations of operators
        for ops in product(operators, repeat=len(items) - 1):
            # Build the expression using numbers in the original order
            expression = str(items[0])
            cr = 0
            for i, op in enumerate(ops):
                if op == "|":
                    expression = str(int(f"{expression}{str(items[i + 1])}"))
                else:
                    expression += f"{op}{items[i + 1]}"
                    cr = eval(expression)
                    expression = str(cr)

            # Evaluate the expression
            if result == eval(expression):
                result_found = True
                break

        if result_found:
            t += result

    return t

def test_day_7():
    #assert day_7_p1("test.txt") == 3749
    assert day_7_p2("test.txt") == 11387

test_day_7()

#p1, p2 = day_7("input.txt")
p2 = day_7_p2("input.txt")
#print("Part 1: ", p1)
print("Part 2: ", p2)