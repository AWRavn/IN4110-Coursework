import cv2
import numpy as np
from numba import jit


@jit(nopython=True)
def grayscale_filter(image):
	"""
	This function applies a grayscale filter on the provided image using built-in python
	functions compiled with numba.

	Args:
		image (Array['H,W,C',int]):			Image file with 3 channels in the RGB format.

	Returns:
		grayscale_image (Array['H,W,C', int): 		Grayscale image in the RGB format with 1 channel.

	"""

	# Initialize variables
	image_height = len(image)
	image_width = len(image[1])
	grayscale_image = image # initialization without Numpy 
	#grayscale_image = np.empty([len(image), len(image[1])]) # better initialization using NumPy. 
															 # Throws error.


	# Apply weights to each channel and sum.
	for i in range(image_height):
		for j in range(image_width):
			grayscale_image[i][j] = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07


	# Correct output format
	grayscale_image = grayscale_image.astype(np.uint8)

	return grayscale_image


def main():
	"""
	Example implementation of the module.

	"""

	filename = "rain.jpg"
	image = cv2.imread("../../images/" + filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	grayscale_image = grayscale_filter(image)
	cv2.imwrite('../../images/{}_numba_grayscale.jpg'.format(filename[:-4]), grayscale_image)


if __name__ == '__main__':
	main()
