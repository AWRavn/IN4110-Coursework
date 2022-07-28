class Array:

    def __init__(self, shape, *values):
        """
        Initialize an array of 1-dimensionality or 2-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        
       Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.

        Raises:
            ValueError: If the values are not of valid types.
            ValueError: If the number of values does not fit with the shape.
        """

        self._shape = shape
        self._array = list(values)

        if len(self._shape) == 1:
            self._shape_dim = 1
            self._shape_len = len(self._array)
        elif len(self._shape) == 2:
            self._shape_dim = 2
            self._shape_len = self._shape[1]*self._shape[0]
        else:
            print('Unsupported dimensions.')


        # Check if the number of values fits with the shape
        try:
            if not int(self._shape_len) == len(self._array):
                raise ValueError
        except ValueError:
            print('The number of values does not fit with the shape.')

        # Check if the values are of valid type
        try:
            if not all(isinstance(x, (int, float, bool)) for x in self._array):
                raise ValueError
        except ValueError:
            print('The input values are not all of valid types.')

        # Optional: If not all values are of same type, all are converted to floats.
        if not all(isinstance(x, type(self._array[0])) for x in self._array[1:]):
            self._array = [float(i) for i in self._array] # or: map(float, self._array)

    def __getitem__(self, item):
        """Returns value of items in array.

        Args:
            item (int): Index of value to return.

        Returns:
            value: Value of the given item.

        """
        return self._array[item]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        if self._shape_dim == 1:
            return ''.join(str(self._array))
        else:
            output = '[\n'
            for i in range(self._shape[0]):
                output += (''.join(str(self._array[i*self._shape[1]:(i+1)*self._shape[1]])))
                output += '\n'
            output += ']'
            return output


    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        
        # check that the method supports the given arguments (check for data type and shape of array)
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        elif isinstance(other, Array):
            if self._shape == other._shape:
                    return Array(self._shape, *[self._array[i]+other[i] for i in range(len(self._array))])
            else:
                return NotImplemented

        else:
            return Array(self._shape, *[x+other for x in self._array])

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        elif isinstance(other, Array):
            if self._shape == other._shape:
                return Array(self._shape, *[self._array[i]-other[i] for i in range(len(self._array))])
            else:
                return NotImplemented

        else:
            return Array(self._shape, *[x-other for x in self._array])

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if not isinstance(other, (Array, float, int)):
            return NotImplemented

        elif isinstance(other, Array):
            if self._shape == other._shape:
                return Array(self._shape, *[self._array[i]*other[i] for i in range(len(self._array))])
            else:
                return NotImplemented

        else:
            return Array(self._shape, *[x*other for x in self._array])

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """

        # check that the method supports the given arguments (check for data type and shape of arrays)
        if not isinstance(other, Array):
            return False
        
        elif isinstance(other, Array):
            if self._shape == other._shape:
                if self._array == other._array:
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise ValueError('Something unexpected when checking data type.')   


    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        # check that the method supports the given arguments (check for data type and shape of arrays)
        if not isinstance(other, (Array, float, int, bool)):
            return TypeError('Input is of the wring type. Accepted data types: Array, float, int.')
        
        if isinstance(other, Array):
            if not self._shape == other._shape:
                raise ValueError('Array shapes do not match.')


        output = list()
        if isinstance(other, (float, int, bool)):
            for i in range(len(self._array)):
                if (self._array[i] == other):
                    output.append(True)                    
                else:
                    output.append(False) 
        elif isinstance(other, Array):
            for i in range(len(self._array)):
                if (self._array[i] == other[i]):
                    output.append(True) 
                else:
                    output.append(False) 

        output = Array(self._shape, *output)
        return output 
    

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        minVal = float(self._array[0])
        for i in range(len(self._array)):
                if (float(self._array[i])) >= minVal:
                    continue
                elif (float(self._array[i])) <= minVal:
                    minVal = float(self._array[i])
        return minVal

