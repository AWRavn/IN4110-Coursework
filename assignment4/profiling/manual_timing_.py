"""
This module tests the runtimes of the functions in test_slow_rectangle using time module.

Example:

	$ python3 manual_timing.py

Prints the output values to command line.

"""

def main():
	"""
	Test runtimes of the functions in test_slow_rectangle.

	Prints results to terminal.
	
	"""

	# Initialize variables
	times_random_array = []
	times_loop = []
	times_snake_loop = []
	n = 10

	# Test runtime using time.time() n times.
	for i in range(n):
		start = time.time()
		array = tsr.random_array(1e5)
		end = time.time()
		times_random_array.append(end-start)

		start = time.time()
		filtered_array_snack = tsr.loop(array)
		end = time.time()
		times_loop.append(end-start)

		start = time.time()
		filtered_array = tsr.snake_loop(array)
		end = time.time()
		times_snake_loop.append(end-start)

	# Print results
	print('Timing: test_slow_rectangle.random_array()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(sum(times_random_array)/len(times_random_array)))
	print('Timing performed using: time.time() (manual timing)\n')
	print('Timing: test_slow_rectangle.loop()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(sum(times_loop)/len(times_loop)))
	print('Timing performed using: time.time() (manual timing)\n')
	print('Timing: test_slow_rectangle.snake_loop()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(sum(times_snake_loop)/len(times_snake_loop)))
	print('Timing performed using: time.time() (manual timing)\n')


if __name__ == '__main__':
	import time
	import test_slow_rectangle as tsr

    main()