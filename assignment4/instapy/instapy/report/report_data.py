import instapy.filters.python_color2gray as python_color2gray
import instapy.filters.numpy_color2gray as numpy_color2gray
import instapy.filters.numba_color2gray as numba_color2gray
import instapy.filters.python_color2sepia as python_color2sepia
import instapy.filters.numpy_color2sepia as numpy_color2sepia
import instapy.filters.numba_color2sepia as numba_color2sepia
import time
import cv2


def get_report_info(image, filter_type, implementation, runtime_python=None, runtime_numpy=None):
	"""
	Applies grayscale and sepia filter functions on the output and provides the report including parameters of the
	tested image as well as relevant runtime of the implementation.

	Args:
		image (np.Array['H,W,3',int]):		Image file with 3 channels in the RGB format.
		filter_type (string): 			Filter to be applied. Choose between 'grayscale' and 'sepia'.
		implementation (string): 		Implementation version. Choose between 'python', 'numpy' and 'numba'.
		runtime_python (float): 		Previous result of python implementation for comparison. Optional.
		runtime_numpy (float): 			Previous result of numpy implementation for comparison. Optional.

	Returns:
		average (float): 			Average runtime of the selected function.

	Raises:
		ValueError				If filter_type and/or implemenattion are not a string.
		InvalidInputError:			If chosen filter_type and/or implemenattion are not implemented.

	Outputs results to a txt file in the reports directory.

	"""


	# Select implementation based on input.
	if isinstance(filter_type, str) and isinstance(implementation, str):
		if filter_type=='grayscale' or filter_type=='greyscale':
			if implementation=='python':
				filter = python_color2gray.grayscale_filter
			elif implementation=='numpy':
				filter = numpy_color2gray.grayscale_filter
			elif implementation=='numba':
				filter = numba_color2gray.grayscale_filter
			else:
				raise InvalidInputError('Unsupported implementation type. Available options: python, numpy, numba.')

		elif filter_type=='sepia':
			if implementation=='python':
				filter = python_color2sepia.sepia_filter
			elif implementation=='numpy':
				filter = numpy_color2sepia.sepia_filter
			elif implementation=='numba':
				filter = numba_color2sepia.sepia_filter
			else:
				raise InvalidInputError('Unsupported implementation type. Available options: python, numpy, numba.')

		else:
			raise InvalidInputError('Unsupported filter type. Available options: grayscale, sepia.')
	else:
		raise ValueError('Unsupported variable type. filter_type and implementation must be a string.')


	# Initialize variables
	times = []
	n = 10

	# Test runtime using time.time() n times and get the average.
	for i in range(n):
		start = time.time()
		filtered_image = filter(image)
		end = time.time()
		times.append(end-start)
	average = sum(times)/len(times)


	# Get report data
	image_height = len(image)
	image_width = len(image[1])

	# Save output to file
	report = open("../../reports/" + implementation + "_report_color2" + filter_type + ".txt", "w")
	report.write('Timing: {}_color2{}\n'.format(implementation, filter_type))
	report.write('Average runtime running {}_color2{} after {} runs: {}\n'.format(implementation, filter_type, n, average))
	if runtime_python!=None:
		difference=float(runtime_python)/average
		report.write('Average runtime for running {}_color2{} is {} times faster than python_color2{}\n'.format(implementation, filter_type, difference, filter_type))
	if runtime_numpy!=None:
		difference=float(runtime_numpy)/(average)
		report.write('Average runtime for running {}_color2{} is {} times faster than numpy_color2{}\n'.format(implementation, filter_type, difference, filter_type))
	report.write('Timing performed using: time.time()\n')
	report.write('Dimensions of the filtered image: H={}, W={}, C=3\n'.format(image_height, image_width))
	if implementation=='numba' and filter_type=='grayscale':
		report.write('The biggest advantage of using Numba over NumPy is it superior computation speed. especially for larger input data\n')
	report.close()

	return average


def main():
	"""
	Create reports for the current implementations.

	"""
	
	filename = "rain.jpg"
	image = cv2.imread("../../images/" + filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	average_gray_python = get_report_info(image, 'grayscale', 'python')
	average_gray_numpy = get_report_info(image, 'grayscale', 'numpy', average_gray_python)
	average_gray_numba = get_report_info(image, 'grayscale', 'numba', average_gray_python, average_gray_numpy)

	average_sepia_python = get_report_info(image, 'sepia', 'python')
	average_sepia_numpy = get_report_info(image, 'sepia', 'numpy', average_sepia_python)
	average_sepia_numba = get_report_info(image, 'sepia', 'numba', average_sepia_python, average_sepia_numpy)


if __name__ == '__main__':
	main()
