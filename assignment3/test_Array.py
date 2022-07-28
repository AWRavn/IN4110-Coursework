# class being tested
from .array import Array


# TEST PRINTING

def test_pretty_print(capsys):
    """Tests that the output is pretty."""
    array = Array((6,), 6, 2, 3, 4, -1, 6)
    print(array)
    result = capsys.readouterr()
    expected = '[6, 2, 3, 4, -1, 6]\n'
    assert result.out == expected

# TEST 1D ADDITION

def test_add_int_to_array():
	"""Test that adding int to array works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array+x
	expected = Array((6,), 12, 8, 9, 10, 5, 12)
	assert result == expected

def test_add_float_to_array():
	"""Test that adding float to array works correctly."""

	array = Array((6,), 6., 2., 3., 4., -1., 6.)
	x = 6
	result = array+x
	expected = Array((6,), 12., 8., 9., 10., 5., 12.)
	assert result == expected

def test_add_array_to_array():
	"""Test that adding array to array works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 6, 2, 3, 4, 5, 1)
	result = array+second_array
	expected = Array((6,), 12, 4, 6, 8, 4, 7)
	assert result == expected


# TEST 1D SUBTRACTION

def test_subtract_int_from_array():
	"""Test that subtracting int from array works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array-x
	expected = Array((6,), 0, -4, -3, -2, -7, 0)
	assert result == expected

def test_subtract_float_from_array():
	"""Test that subtracting float from array works correctly."""

	array = Array((6,), 6., 2., 3., 4., -1., 6.)
	x = 6
	result = array-x
	expected = Array((6,), 0., -4., -3., -2., -7., 0.)
	assert result == expected

def test_subtract_array_from_array():
	"""Test that subtracting array from array works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 6, 2, 3, 4, 5, 1)
	result = array-second_array
	expected = Array((6,), 0, 0, 0, 0, -6, 5)
	assert result == expected


# TEST 1D MULTIPLICATION

def test_multiply_array_by_int():
	"""Test that multiplying array by int works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array*x
	expected = Array((6,), 36, 12, 18, 24, -6, 36)
	assert result == expected

def test_multiply_array_by_float():
	"""Test that multiplying array by float works correctly."""

	array = Array((6,), 6., 2., 3., 4., -1., 6.)
	x = 6
	result = array*x
	expected = Array((6,), 36., 12., 18., 24., -6., 36.)
	assert result == expected

def test_multiply_array_by_array():
	"""Test that multiplying array by array works correctly."""

	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 6, 2, 3, 4, 5, 1)
	result = array*second_array
	expected = Array((6,), 36, 4, 9, 16, -5, 6)
	assert result == expected


# TEST 1D COMPARISON

def test_compare_equal_arrays():
	"""Test that comparing equal arrays works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 6, 2, 3, 4, -1, 6)
	result = array==second_array
	expected = True
	assert result == expected

def test_compare_different_arrays():
	"""Test that comparing different arrays works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 3, 2, 3, 4, 5, 6)
	result = array==second_array
	expected = False
	assert result == expected


 # TEST 1D ELEMENTWISE COMPARISON

def test_compare_equal_arrays():
	"""Test that comparing equal arrays works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 6, 2, 3, 4, -1, 6)
	result = array.is_equal(second_array)
	expected = Array((6,), True, True, True, True, True, True)
	assert result == expected

def test_compare_different_arrays():
	"""Test that comparing different arrays works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	second_array =  Array((6,), 3, 2, 3, 4, 5, 6)
	result = array.is_equal(second_array)
	expected = Array((6,), False, True, True, True, False, True)
	assert result == expected

def test_compare_array_to_number():
	"""Test that comparing array to numbers works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array.is_equal(x)
	expected = Array((6,), True, False, False, False, False, True)
	assert result == expected


# TEST FINDING SMALLEST ELEMENT

def test_finding_smallest__element_int():
	"""Test that finding the smallest element in the array works correctly."""
	array = Array((6,), 6, 2, 3, 4, -1, 6)
	result = array.min_element()
	expected = -1.0
	assert result == expected

def test_finding_smallest_element_float():
	"""Test that finding the smallest element in the array works correctly."""
	array = Array((6,), 6., 1., 3., 4., 15., 6.)
	result = array.min_element()
	expected = 1.0
	assert result == expected





	# TEST 2D ADDITION

def test_add_int_to_array_2d():
	"""Test that adding int to array works correctly."""

	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array+x
	expected = Array((3, 2), 12, 8, 9, 10, 5, 12)
	assert result == expected

def test_add_array_to_array_2d():
	"""Test that adding array to array works correctly."""

	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 6, 2, 3, 4, 5, 1)
	result = array+second_array
	expected = Array((3, 2), 12, 4, 6, 8, 4, 7)
	assert result == expected


# TEST 2D SUBTRACTION

def test_subtract_int_from_array_2d():
	"""Test that subtracting int from array works correctly."""

	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array-x
	expected = Array((3, 2), 0, -4, -3, -2, -7, 0)
	assert result == expected

def test_subtract_array_from_array_2d():
	"""Test that subtracting array from array works correctly."""

	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 6, 2, 3, 4, 5, 1)
	result = array-second_array
	expected = Array((3, 2), 0, 0, 0, 0, -6, 5)
	assert result == expected


# TEST 2D COMPARISON

def test_compare_equal_arrays_2d():
	"""Test that comparing equal arrays works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 6, 2, 3, 4, -1, 6)
	result = array==second_array
	expected = True
	assert result == expected

def test_compare_different_arrays_2d():
	"""Test that comparing different arrays works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 3, 2, 3, 4, 5, 6)
	result = array==second_array
	expected = False
	assert result == expected

def test_compare_array_to_int_2d():
	"""Test that comparing arrays to other types works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array==x
	expected = False
	assert result == expected


 # TEST 2D ELEMENTWISE COMPARISON

def test_compare_equal_arrays_2d():
	"""Test that comparing equal arrays works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 6, 2, 3, 4, -1, 6)
	result = array.is_equal(second_array)
	expected = Array((3, 2), True, True, True, True, True, True)
	assert result == expected

def test_compare_different_arrays_2d():
	"""Test that comparing different arrays works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 2), 3, 2, 3, 4, 5, 6)
	result = array.is_equal(second_array)
	expected = Array((3, 2), False, True, True, True, False, True)
	assert result == expected

def test_compare_array_to_number_2d():
	"""Test that comparing array to numbers works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	x = 6
	result = array.is_equal(x)
	expected = Array((3, 2), True, False, False, False, False, True)
	assert result == expected

def test_value_error_in_comparisons():
	"""Test that comparing unequal arryas works correctly."""
	array = Array((3, 2), 6, 2, 3, 4, -1, 6)
	second_array =  Array((3, 1), 4, 5, 6)
	with pytest.raises(ValueError):
		result = array.is_equal(second_array)