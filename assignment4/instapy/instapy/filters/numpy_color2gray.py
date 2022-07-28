import cv2
import numpy as np


def grayscale_filter(image):
	"""
	This function applies a grayscale filter on the provided image using numpy.

	Args:
		image (Array['H,W,C',int]):			Image file with 3 channels in the RGB format.

	Returns:
		grayscale_image (Array['H,W,C', int):		Grayscale image in the RGB format with 1 channel.

	"""


	# Initialize variables
	image = np.array(image)
	weights = np.array([0.21, 0.73, 0.07])
	grayscale_image = np.empty([len(image), len(image[1])])


	# Apply weights to each channel and sum.
	grayscale_image = image[:,:,0]*weights[0] + image[:,:,1]*weights[1] + image[:,:,2]*weights[2]


	# Correct output format
	grayscale_image_ = np.uint8(np.clip(grayscale_image, 0, 255)) 
	#grayscale_image.astype("uint8") rounds negative values to 255 instead of 0

	return grayscale_image


def main():
	"""
	Example implementation of the python_colour2gray module.

	"""

	filename = "rain.jpg"
	image = cv2.imread("../../images/" + filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	grayscale_image = grayscale_filter(image)
	cv2.imwrite('../../images/{}_numpy_grayscale.jpg'.format(filename[:-4]), grayscale_image)


if __name__ == '__main__':
	main()
