"""
This module tests the runtimes of the functions in test_slow_rectangle using timeit module.

Example:

	$ python3 timeit_timing.py

Prints the output values to command line.

"""

def main():
	"""
	Test runtimes of the functions in test_slow_rectangle.

	Prints results to terminal.
	
	"""

	# Initialize variables
	mysetup = 'import test_slow_rectangle as tsr'
	mycode_random_array = 'array = tsr.random_array(1e5)'
	mycode_loop = '''array = tsr.random_array(1e5)
filtered_array_snack = tsr.loop(array)'''
	mycode_snake_loop = '''array = tsr.random_array(1e5)
filtered_array = tsr.snake_loop(array)'''
	n = 10
	
	# Test runtime using timeit.timeit() n times.
	time_random_array = timeit.timeit(setup = mysetup, stmt = mycode_random_array, number = n)
	time_loop = timeit.timeit(setup = mysetup, stmt = mycode_loop, number = n) - time_random_array
	time_snake_loop = timeit.timeit(setup = mysetup, stmt = mycode_snake_loop, number = n) - time_random_array

	# Print results
	print('Timing: test_slow_rectangle.random_array()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(time_random_array))
	print('Timing performed using: timeit.timeit()\n')
	print('Timing: test_slow_rectangle.loop()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(time_loop))
	print('Timing performed using: timeit.timeit()\n')
	print('Timing: test_slow_rectangle.snake_loop()')
	print('Average runtime running test_slow after {} runs: '.format(n) + str(time_snake_loop))
	print('Timing performed using: timeit.timeit()\n')


if __name__ == '__main__':
	import timeit
	import test_slow_rectangle as tsr

    main()