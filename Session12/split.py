"""Splitting NumPy Arrays
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.


Example
Split the array in 3 parts:"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

newarr = np.array_split(arr, 3)
#If the array has less elements than required, it will adjust from the end accordingly.

print(newarr)

print('*'*100)
"""Example
Split the array in 4 parts:"""


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

print('*'*100)
"""Note: We also have the method split() available but it will not adjust the elements when elements are 
less in source array for splitting like in example above, 
array_split() worked properly but split() would fail.


We can access split arrays."""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
print('*'*100)

"""Example
Split the 2-D array into three 2-D arrays."""


import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
print('*'*100)

"""Example
Split the 2-D array into three 2-D arrays along rows."""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
print('*'*100)

"""otherwise we can use hsplit() method for axis """


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)

print('*'*100)

"""Another function is there dsplit() dsplit only works on arrays of 3 or more dimensions

Array_split() and vsplit() both are same it will gives the same result"""