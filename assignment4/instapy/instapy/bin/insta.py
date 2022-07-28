#! /usr/bin/python

import instapy.filters.python_color2gray as python_color2gray
import instapy.filters.numpy_color2gray as numpy_color2gray
import instapy.filters.numba_color2gray as numba_color2gray
import instapy.filters.python_color2sepia as python_color2sepia
import instapy.filters.numpy_color2sepia as numpy_color2sepia
import instapy.filters.numba_color2sepia as numba_color2sepia
import os
import sys
import cv2
import argparse
import time


def check_input(input_filename):
	'''
	Checks validity of the input into the parser.

	Args:
		input_filename (string):			Path to the image.

	Returns:
		input_filename (string):			Path to the image.

	Raises:
		argparse.ArgumentTypeError:			If input file doesn't exist or has invalid extension.
		
	'''

	if not os.path.isfile(input_filename):
		raise argparse.ArgumentTypeError('File not found.')

	if not input_filename.lower().endswith(('.jpg', '.jpeg')):
		raise argparse.ArgumentTypeError('Unsupported extension on input. Required: .jpg, .jpeg')
	return input_filename


def check_output(output_filename):
	'''
	Checks validity of the output filename from the parser.

	Args:
		output_filename (string):			Path to the image.

	Returns:
		output_filename (string):			Path to the image.

	Raises:
		argparse.ArgumentTypeError:			If output file has invalid extension.
		
	'''

	if not output_filename.lower().endswith(('.jpg', '.jpeg')):
		raise argparse.ArgumentTypeError('Unsupported extension on output. Required: .jpg, .jpeg')
	return output_filename


def check_level(level):
	'''
	Checks validity of the level of sepia filter.

	Args:
		level (float):					Level of the sepia filter.

	Returns:
		level (float):					Level of the sepia filter.

	Raises:
		argparse.ArgumentTypeError:			If level is not a float or har invalid value.
		
	'''

	if float(level)>1.0 or float(level)<0.0:
		raise argparse.ArgumentTypeError('Level must be a float between 0 and 1.')
	return float(level)


def grayscale_image(input_filename, output_filename=None, implementation='numpy', scaling=None):
	"""
	This function applies a grayscale filter on the provided image and saves the output to provided path if requested.

	Args:
		input_filename (string):			Path to the image.
		output_filename (string): 			Path to the output image (optional). Default None.
		implementation (string): 			Implamentation type (optional). Availbale options 'python', 
								'numpy' and 'numba'. Default numpy.
		scaling (float):				Scaling to be applied to the image (optional). Defaut None.

	Returns:
		grayscale_image (Array['H,W,1', (unsigned) int): Grayscale image in the RGB format with 1 channel.

	Raises:
		ImplementationTypeError:			If chosen implemenattion doesn't exist.
		ResizeTypeError:				If chosen scaling is not a float.

	"""

	# Convert to RGB
	image = cv2.imread(input_filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# Apply scaling
	if not scaling==None:
		if isinstance(scaling, float):
			image = cv2.resize(image, (0, 0), fx=scaling, fy=scaling)
		else:
			raise ResizeTypeError('Resize needs to be a float.')
			sys.exit(1)		

	# Apply implementation
	if implementation=='python':
		grayscale_image = python_color2gray.grayscale_filter(image)

	elif implementation=='numpy' or implementation==None:
		grayscale_image = numpy_color2gray.grayscale_filter(image)

	elif implementation=='numba':
		grayscale_image = numba_color2gray.grayscale_filter(image)

	else:
		raise ImplementationTypeError('Unsupported implementation type. Use "python", "numpy" or "numba"')
		sys.exit(1)


	if output_filename!=None:
		cv2.imwrite(output_filename, grayscale_image)

	return grayscale_image


def sepia_image(input_filename, output_filename=None, implementation='numpy', scaling=None, level=1.0):
	"""
	This function applies a sepia filter on the provided image and saves the output to provided path if requested.

	Args:
		input_filename (string):			Path to the image.
		output_filename (string): 			Path to the output image (optional). Default None.
		implementation (string): 			Implamentation type (optional). Availbale options 'python',
								'numpy' and 'numba'. Default numpy.
		scaling (float):				Scaling to be applied to the image (optional). Defaut None.
		level (float):					Constant between 0 and 1 determining sepia level.

	Returns:
		sepia_image (Array['H,W,3', (unsigned) int):	Sepia image in the RGB format with 3 channels.

	Raises:
		ImplementationTypeError:			If chosen implemenattion doesn't exist.
		ResizeTypeError:				If chosen scaling is not a float.

	"""

	# Read input
	image = cv2.imread(input_filename)

	# Return as is if level=0.0
	if level==0.0:
		return image

	# Convert to RGB
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# Apply scaling
	if not scaling==None:
		if isinstance(scaling, float):
			image = cv2.resize(image, (0, 0), fx=scaling, fy=scaling)
		else:
			raise ResizeTypeError('Resize needs to be a float.')
			sys.exit(1)	

	# Apply implementation
	if implementation=='python':
		sepia_image = python_color2sepia.sepia_filter(image, level)

	elif implementation=='numpy' or implementation==None:
		sepia_image = numpy_color2sepia.sepia_filter(image, level)

	elif implementation=='numba':
		sepia_image = numba_color2sepia.sepia_filter(image, level)

	else:
		raise TypeError('Unsupported implementation type. Use "python", "numpy" or "numba"')
		sys.exit(1)


	if output_filename!=None:
		cv2.imwrite(output_filename, sepia_image)

	return sepia_image


def main():
	"""
	Creates a rudimentary user interface and applies chosen settings to filters.

	"""
	
	# Create the parser
	instapy_parser = argparse.ArgumentParser(prog='instapy', usage='python3 insta.py [-f FILE] [-se/-g] [-i {python, numba, numpy}] [-o OUT] [-sc SCALE] [-r] [-l LEVEL]',
						description='Applies sepia or grayscale filter to images.')

	# Assign Flags
	instapy_parser.add_argument('-f', '--file', type=check_input, help='The filename of file to apply filter to.' )

	instapy_parser.add_argument('-se', '--sepia', action='store_true', help='Select sepia filter.' )

	instapy_parser.add_argument('-g', '--gray', action='store_true', help='Select gray filter.' )

	instapy_parser.add_argument('-i', '--implement', choices=['python', 'numpy', 'numba'], help='Choose the implementation.' )

	instapy_parser.add_argument('-o', '--out', type=check_output, help='The output filename.' )

	instapy_parser.add_argument('-sc', '--scale', type=float, help='Scale factor to resize image.')

	instapy_parser.add_argument('-r', '--runtime', action='store_true', help='Track average runtime.')
	
	instapy_parser.add_argument('-l', '--level', type=check_level, help='Alter level of sepia between 0 and 1.')

	
	# Get input
	args = instapy_parser.parse_args()


	# Check input arguments
	if args.gray==True and args.sepia==True:
		 raise argparse.ArgumentTypeError('Only one filter can be applied at a time.')


	# Apply input
	if args.runtime==True:
		times = []
		for i in range(3):
			start = time.time()
			if args.sepia==True:
				sepia_image(args.file, args.out, args.implement, args.scale, 1.0)
			elif args.sepia==True and args.level!=None:
				sepia_image(args.file, args.out, args.implement, args.scale, args.level)
			elif args.gray==True:
				grayscale_image(args.file, args.out, args.implement, args.scale)
			times.append(time.time()-start)
		print(f"Average time over 3 runs: " + str(sum(times)/3))

	else:
		if args.sepia==True:
			sepia_image(args.file, args.out, args.implement, args.scale, 1.0)
		elif args.sepia==True and args.level!=None:
				sepia_image(args.file, args.out, args.implement, args.scale, args.level)
		elif args.gray==True:
			grayscale_image(args.file, args.out, args.implement, args.scale)




if __name__ == '__main__':
	main()

