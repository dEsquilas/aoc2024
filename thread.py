from concurrent.futures import ThreadPoolExecutor
import time

# Define child functions
def child_function_1():
	time.sleep(1)
	print("Child function 1")
	return 10

def child_function_2():
	time.sleep(2)
	print("Child function 2")
	return 20

def child_function_3():
	time.sleep(3)
	print("Child function 3")
	return 30

def child_function_4():
	time.sleep(4)
	print("Child function 4")
	return 40

# Define parent function
def parent_function():
	with ThreadPoolExecutor() as executor:
		# Launch child functions in separate threads
		futures = [
			executor.submit(child_function_1),
			executor.submit(child_function_2),
			executor.submit(child_function_3),
			executor.submit(child_function_4),
		]
		# Wait for all futures to complete and sum their results
		total = sum(future.result() for future in futures)
	return total

# Execute the parent function
result = parent_function()
print(f"The total sum is: {result}")