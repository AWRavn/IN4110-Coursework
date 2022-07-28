"""
This module tests the runtimes of the functions in test_slow_rectangle using cProfile module.

Example:

	$ python3 cProfile_timing.py

Prints the output values to command line.

"""

def main():
	"""
	Runs functions in test_slow_rectangle.

	"""

	array = tsr.random_array(1e5)
	filtered_array_snack = tsr.loop(array)
	filtered_array = tsr.snake_loop(array)


if __name__ == '__main__':
	import cProfile, pstats
	import test_slow_rectangle as tsr

	# Test runtimes of the functions in test_slow_rectangle.
	profiler = cProfile.Profile()
	profiler.enable()
	main()
	profiler.disable()
	stats = pstats.Stats(profiler).sort_stats('ncalls')

	# Print results
	stats.print_stats()