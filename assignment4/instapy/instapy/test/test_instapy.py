# class being tested
import instapy.filters.python_color2gray as python_color2gray
import instapy.filters.numpy_color2gray as numpy_color2gray
import instapy.filters.numba_color2gray as numba_color2gray
import instapy.filters.python_color2sepia as python_color2sepia
import instapy.filters.numpy_color2sepia as numpy_color2sepia
import instapy.filters.numba_color2sepia as numba_color2sepia
import numpy as np
import pytest


# UNIT TESTS FOR GRAYSCALE FILTERS

def test_grayscale_python():
	'''Test that random pixel in grayscale image aligns with expected weighted values.'''


	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	grayscale_result = python_color2gray.grayscale_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = grayscale_result[i][j]
	expected = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


def test_grayscale_numpy():
	'''Test that random pixel in grayscale image aligns with expected weighted values.'''


	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	grayscale_result = numpy_color2gray.grayscale_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = grayscale_result[i][j]
	expected = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


def test_grayscale_numba():
	'''Test that random pixel in grayscale image aligns with expected weighted values.'''

	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	grayscale_result = numba_color2gray.grayscale_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = grayscale_result[i][j]
	expected = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


# UNIT TESTS FOR SEPIA FILTERS

def test_sepia_python():
	'''Test that random pixel in sepia image aligns with expected weighted values.'''

	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	sepia_result = python_color2sepia.sepia_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = sepia_result[i][j][:]
	expected1 = min(255, (image[i][j][0]*0.272 + image[i][j][1]*0.534 + image[i][j][2]*0.131))
	expected2 = min(255, (image[i][j][0]*0.349 + image[i][j][1]*0.686 + image[i][j][2]*0.168))
	expected3 = min(255, (image[i][j][0]*0.393 + image[i][j][1]*0.769 + image[i][j][2]*0.189))
	expected = [expected1, expected2, expected3]

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


def test_sepia_numpy():
	'''Test that random pixel in sepia image aligns with expected weighted values.'''

	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	sepia_result = numpy_color2sepia.sepia_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = sepia_result[i][j][:]
	expected1 = min(255, (image[i][j][0]*0.272 + image[i][j][1]*0.534 + image[i][j][2]*0.131))
	expected2 = min(255, (image[i][j][0]*0.349 + image[i][j][1]*0.686 + image[i][j][2]*0.168))
	expected3 = min(255, (image[i][j][0]*0.393 + image[i][j][1]*0.769 + image[i][j][2]*0.189))
	expected = [expected1, expected2, expected3]

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


def test_sepia_numba():
	'''Test that random pixel in sepia image aligns with expected weighted values.'''

	image = np.random.randint(0, 255, size=(400,300,3),dtype=np.uint8) # random rgb image
	sepia_result = numba_color2sepia.sepia_filter(image)

	i = np.random.randint(0, 400)
	j = np.random.randint(0, 300)

	actual = sepia_result[i][j][:]
	expected1 = min(255, (image[i][j][0]*0.272 + image[i][j][1]*0.534 + image[i][j][2]*0.131))
	expected2 = min(255, (image[i][j][0]*0.349 + image[i][j][1]*0.686 + image[i][j][2]*0.168))
	expected3 = min(255, (image[i][j][0]*0.393 + image[i][j][1]*0.769 + image[i][j][2]*0.189))
	expected = [expected1, expected2, expected3]

	assert actual == pytest.approx(expected, 2) # allowing to some grace due to averaging


