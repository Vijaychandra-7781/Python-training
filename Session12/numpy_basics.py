"""NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy stands for Numerical Python.

In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make
working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

Data Science: is a branch of computer science where we study how to store,

use and analyze data for deriving information from it.

Why is NumPy Faster Than Lists?

NumPy arrays are stored at one continuous place in memory unlike lists,
 so processes can access and manipulate them very efficiently.



 Import NumPy
Once NumPy is installed, import it in your applications by adding the import keyword:"""



"""Checking NumPy Version
The version string is stored under __version__ attribute."""


import numpy as np

print(np.__version__)


print('*'*100)
"""How to create numpy arrays


NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function."""


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

print('*'*100)
"""Example
Use a tuple to create a NumPy array:"""


import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))
print('*'*100)

"""Example
Create a 0-D array with value 42"""

import numpy as np

arr = np.array(42)

print(arr)  # This is the zero dimensional array
print(type(arr))
print('*'*100)

"""Example
Create a 1-D array containing the values 1,2,3,4,5:"""

import numpy as np
arr=np.array([1,2,3,4])

print(arr)

print('*'*100)



"""Example
Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:"""


import numpy as np

arr=np.array([[1,2,34,4], [12,24,36,2]])

print(arr)


print('*'*100)



"""Example
Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:"""


import numpy as np
arr=np.array([[[1,2,4],[21,12,12]],[[12,23,21],[12,11,13]]])

print(arr)

print('*'*100)


"""Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us 
how many dimensions the array have.

Example
Check how many dimensions the arrays have:"""

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


print('*'*100)
"""Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

Example
Create an array with 5 dimensions and verify that it has 5 dimensions:"""

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

