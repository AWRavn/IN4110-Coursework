import cv2
import numpy as np


def sepia_filter(image, level):
	"""
	This function applies a sepia filter on the provided image using built-in python
	functions.

	Args:
		image (Array['H,W,C',int]):		  	Image file with 3 channels in the RGB format.
		level (float):					Constant between 0 and 1 determining sepia level.

	Returns:
		sepia_image (Array['H,W,C', int):		Grayscale image in the RGB format with 3 channels.

	"""


	# Initialize variables
	image_height = len(image)
	image_width = len(image[1])
	sepia_image = image # initialization without Numpy 
	#sepia_image = np.empty([len(image), len(image[1])]) # better initialization using NumPy. 
														 # Throws error.


	# Apply weights to each channel and sum. Image values are not scaled for simplicity.
	for i in range(image_height):
		for j in range(image_width):
			sepia_red = min(255, (image[i][j][0]*0.393*level + image[i][j][1]*0.769*level + image[i][j][2]*0.189*level))
			sepia_green = min(255, (image[i][j][0]*0.349*level + image[i][j][1]*0.686*level + image[i][j][2]*0.168*level))
			sepia_blue = min(255, (image[i][j][0]*0.272*level + image[i][j][1]*0.534*level + image[i][j][2]*0.131*level))

			sepia_image[i][j][:] = [sepia_blue, sepia_green, sepia_red]


	# Correct output format
	sepia_image = sepia_image.astype("uint8")

	return sepia_image


def main():
	"""
	Example implementation of the module.

	"""
	
	filename = "rain.jpg"
	image = cv2.imread("../../images/" + filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	sepia_image = sepia_filter(image, 1.0)
	cv2.imwrite('../../images/{}_python_sepia.jpg'.format(filename[:-4]), sepia_image)


if __name__ == '__main__':
	main()
