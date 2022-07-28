## Prerequisites

**Installing Python**

Make sure you have Python3 installed on your machine. This program is confirmed to work on version 3.8.10.

You may check your Python version by running:
```bash
python3 --version
```

**Installing dependencies**

Install all dependencies that are required for the project by running:
```bash
pip install -r requirements.txt
```

## Testing the Code

Tests are made using pytest framework.

To run the tests call the following command in the folder containing this project:
```bash
pytest
```

## Usage

This package defines a class Array that can be used as follows:

```python
shape = (4 ,)
# define my_array
my_array = Array (shape, 2, 3, 1, 0)
# __getitem__ should be implemented correctly .
assert my_array[2] == 1
# Printing the array prints the array values nicely .
# For example : [2 , 3 , 1, 0]
print (my_array)
```

Array class can be initialized by `Array(shape, *values)`, where `shape` is a tuple of dimensions of the array, and `*values` are values contained within it. Only up to 2-dimensional Arrays are supported.

Arrays can be added, subtracted and multiplied by each other or by numbers (float, int). They can also be compared to each other with `==`. Printing yelds a pretty output.

```python
array1 = Array((3, 2), 1, 2, 3, 4, 5, 6)
array2 = Array((3, 2), 11, 12, 13, 14, 15, 16)
x = 7

print(array1+array2)
print(array1+x)
```


```bash
$ example.py
[
[12, 14]
[16, 18]
[20, 22]
]
[
[8, 9]
[10, 11]
[12, 13]
]
```

```python
print(array1-array2)
print(array1*array2)

```
```bash
$ example.py
[
[-10, -10]
[-10, -10]
[-10, -10]
]
[
[-6, -5]
[-4, -3]
[-2, -1]
]
```

```python
print(array1-x)
print(array1*x)
```
```bash
$ example.py
[
[11, 24]
[39, 56]
[75, 96]
]
[
[7, 14]
[21, 28]
[35, 42]
]
```

```python
print(array1==array2)
```
```bash
$ example.py
False
```


**`Array.is_equal(variable)`**

Compares an Array element-wise with another Array or number. 'variable' can be either an Array, float, int or bool. 
Returns an Array of booleans with True where the two arrays match and False where they do not. If `variable` is a number, it returns True where the array is equal to the number and False where it is not.

```python
$ example.py
array1 = Array((3, 2), 1, 2, 3, 4, 5, 6)
array2 = Array((3, 2), 1, 12, 3, 14, 5, 16)
x = 7

print(array1.is_equal(array2))
print(array1.is_equal(x))
```
```bash
[
[True, False]
[True, False]
[True, False]
]
[
[False, False]
[False, False]
[False, False]
]
```


**`Array.min_element()`**

Returns the smallest value of the array as a float. Only works for Arrays containing types int and float.

```python
array1 = Array((3, 2), 1, 2, 3, 4, 5, 6)

print(array1.min_element())
```
```bash
$ example.py
1.0
```