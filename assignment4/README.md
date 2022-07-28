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

To run the tests call the following command in `./instapy/instapy/test` directory:
```bash
pytest
```


## Code Structure
```
README.md
requirements.txt
profiling/
|- cProfile_timing_.py
|- manual_timing_.py
|- timeit_timing_.py
|- test_slow_rectangle.py
|- reports/
	|- cProfile_report.txt
	|- manual_report.txt
	|- timeit_report.txt
instapy/
	__init__.py
	setup.py
	|- images/
		|- __init__.py
		|- rain.jpg
		|- rain_numba_grayscale.jpg
		|- rain_numba_sepia.jpg
		|- rain_numpy_grayscale.jpg
		|- rain_numpy_sepia.jpg
		|- rain_python_grayscale.jpg
		|- rain_python_sepia.jpg
	|- reports/
		|- __init__.py
		|- numba_report_color2grayscale.txt
		|- numba_report_color2sepia.txt
		|- numpy_report_color2grayscale.txt
		|- numpy_report_color2sepia.txt
		|- python_report_color2grayscale.txt
		|- python_report_color2sepia.txt
	|- instapy/
		|- __init__.py
		|- bin/
			|- __init__.py
			|- insta.py
		|- filters/
			|- __init__.py
			|- numba_color2gray.py
			|- numba_color2sepia.py
			|- numpy_color2gray.py
			|- numpy_color2sepia.py
			|- python_color2gray.py
			|- python_color2sepia.py
		|- report/
			|- __init__.py
			|- report_data.py
		|- test/
			|- __init.py__
			|- test_instapy.py
```


## Usage profiling 

The programs in this directory evaluate runtime of functions contained within `test_slow_rectangle.py` each using a different module. Each of them outputs results nicely in terminal. Example usage from the `./profiling` directory:
```bash
python3 manual_timing_.py
python3 timeit_timing_.py
python3 cProfile_timing_.py
```
The outputs can also be found in the `./profiling/reports` directory.


## Usage instapy package

Instapy is a package for applying grayscale and sepia filters onto images and the output can then be saved to a file. Available is runtime tracking, pre-scaling of an image (to decrease said runtime), choice of three implementations per filter: 'python', 'numpy' and 'numba'.

**Installing instapy**

To install instapy module run the following commend in the top instapy directory:
```bash
pip install .
```

**Running instapy**

After installing instapy you will be able to run it in two different ways:
```bash
python3 insta <arguments>
insta <arguments>
```

The following arguments are part of implementation:
```bash
[-f FILE] [-se/-g] [-i {python, numba, numpy}] [-o OUT] [-sc SCALE] [-r] [-l LEVEL]
```
Here `-f FILE` is the path to the input file, `-se/-g` indicates sepia and grayscale filter respectively, `-i {python, numba, numpy}` specifies implementation to be applied (default numpy), `-o OUT` is the path to the output file, `-sc SCALE` indicates scaling to be applied on the image, `-r` will track average runtime and `-l LEVEL` alters level of sepia filter. Example call:
```bash
python3 insta -f "../../images/rain.jpg" -o "../../images/rain_test.jpg" -i "python", -sc 0.8 -r
```

## Function Description

**`instapy.greyscale_image(input_filename, output_filename=None, implementation='numpy')`**

This function applies a grayscale filter on the provided image and saves the output to provided path if provided as argument.'input_filename' is the PATH to the file you wish to change, 'output_filename' is the optional PATH to the saved output. 'implamentation' specifies which method for solving the problem is to be used, chosen among 'python', 'numpy' and 'numba', with 'numpy' being the default option. Example usage:
```python
$ example.py
import instapy.instapy
filename = "../images/rain.jpg"
output = "../images/rain_grayscale.jpg"
image = instapy.instapy.grayscale_image(filename, output, implementation="numba")
```


**`instapy.sepia_image(input_filename, output_filename=None, implementation='numpy')`**

This function applies a sepia filter on the provided image and saves the output to provided path if provided as argument.'input_filename' is the PATH to the file you wish to change, 'output_filename' is the optional PATH to the saved output. 'implamentation' specifies which method for solving the problem is to be used, chosen among 'python', 'numpy' and 'numba', with 'numpy' being the default option. Example usage:
```python
$ example.py
import instapy.instapy
filename = "../images/rain.jpg"
output = "../images/rain_sepia.jpg"
image = instapy.instapy.sepia_image(filename, output, implementation="numba")
```


**`report/report_data.get_report_info(image, filter_type, implementation, runtime_python=None, runtime_numpy=None)`**

Applies grayscale and sepia filter functions on the output and provides the report including parameters of the tested image as well as relevant runtime of the implementation. Example usage from the `./instapy/instapy/report` directory:
```bash
python3 report_data.py
```
The outputs can also be found in the `./instapy/reports` directory.


**Grayscale filters**

`python_color2gray.py`, `numpy_color2gray.py` and `numba_color2gray.py` each implement a `grayscale_filter(image)` function which applies a grayscale filter on the provided image using method indicated in the filename: `python`, `numpy` and `numba` respectively. Intented use is through the `instapy.py` file.


**Sepia filters**

`python_color2sepia.py`, `numpy_color2sepia.py` and `numba_color2sepia.py` each implement a `sepia_filter(image)` function which applies a grayscale filter on the provided image using method indicated in the filename: `python`, `numpy` and `numba` respectively. Intented use is through the `instapy.py` file.

## Additional Comments

**Needs fixing**
- Level adjustment. Currently the luminosity is altered instead of "sepianess". Works fine for value 1.0 and 0.0.
- Script in /bin/ is named insta.py instead of instapy.py due to import errors.

**Not implements**
- Cython implementations
