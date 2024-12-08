from itertools import product
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

def process_op(items, ops, result, stop_flag, process_id, total_processes):
    """
    Process a single combination of operators to check if it matches the result.
    Prints process ID and total processes.
    """
    if stop_flag.is_set():
        return None

    #print(f"Process {process_id}/{total_processes} started.")
    expression = str(items[0])
    for i, op in enumerate(ops):
        if op == "|":
            expression = str(int(f"{expression}{str(items[i + 1])}"))
        else:
            expression += f"{op}{items[i + 1]}"
            current_result = eval(expression)
            expression = str(current_result)

    if result == eval(expression):
        stop_flag.set()  # Signal other threads to stop
        return result
    return None

def day_7(filename):
    equations = [line for line in open(filename).read().splitlines()]
    operators_p1 = ["+", "*"]
    operators_p2 = ["+", "*", "|"]
    total_p1 = 0
    total_p2 = 0

    for equation in equations:
        result = int(equation.split(":")[0])
        items = [int(x) for x in equation.split(":")[1].strip().split(" ")]

        # Shared stop flag for both parts
        stop_flag = threading.Event()

        # Part 1
        with ThreadPoolExecutor() as executor:
            operator_combinations = list(product(operators_p1, repeat=len(items) - 1))
            futures = [
                executor.submit(process_op, items, ops, result, stop_flag, i + 1, len(operator_combinations))
                for i, ops in enumerate(operator_combinations)
            ]
            result_found_p1 = False
            for future in as_completed(futures):
                res = future.result()
                if res:
                    total_p1 += res
                    result_found_p1 = True
                    break

        # If P1 found a valid result, reuse it for P2
        if result_found_p1:
            total_p2 += result
            print(f"Reused result from P1 for P2: {result}")
            continue

        # Reset the stop flag for Part 2
        stop_flag.clear()

        # Part 2
        with ThreadPoolExecutor() as executor:
            operator_combinations = list(product(operators_p2, repeat=len(items) - 1))
            futures = [
                executor.submit(process_op, items, ops, result, stop_flag, i + 1, len(operator_combinations))
                for i, ops in enumerate(operator_combinations)
            ]
            for future in as_completed(futures):
                res = future.result()
                if res:
                    total_p2 += res
                    break

    return total_p1, total_p2

def test_day_7():
    assert day_7("test.txt") == (3749, 11387)

test_day_7()

p1, p2 = day_7("input.txt")
print("Part 1: ", p1)
print("Part 2: ", p2)