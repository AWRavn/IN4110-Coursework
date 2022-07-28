import cv2
import numpy as np


def sepia_filter(image, level):
	"""
	This function applies a grayscale filter on the provided image using numpy.

	Args:
		image (Array['H,W,C',int]):			Image file with 3 channels in the RGB format.
		level (float):					Constant between 0 and 1 determining sepia level.

	Returns:
		sepia_image (Array['H,W,C', int):		Grayscale image in the RGB format with 3 channel.

	"""


	# Initialize variables
	image = np.array(image)
	sepia_matrix = np.array([[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]])*level
	sepia_matrix[[0, 2]] = sepia_matrix[[2, 0]]
	

	# Apply weights to each channel and sum.
	sepia_image = image.dot(sepia_matrix.T)
	sepia_image[np.where(sepia_image>255)] = 255


	# Correct output format
	sepia_image = np.uint8(np.clip(sepia_image, 0, 255)) 

	return sepia_image


def main():
	"""
	Example implementation of the python_colour2sepia module.

	"""

	filename = "rain.jpg"
	image = cv2.imread("../../images/" + filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	sepia_image = sepia_filter(image, 1.0)
	cv2.imwrite('../../images/{}_numpy_sepia.jpg'.format(filename[:-4]), sepia_image)


if __name__ == '__main__':
	main()
