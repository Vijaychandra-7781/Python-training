"""Shape of an Array
The shape of an array is the number of elements in each dimension.

NumPy arrays have an attribute called shape that returns a tuple with each
index having the number of corresponding elements.

Example
Print the shape of a 2-D array:"""

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

print('*'*100)




"""Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.


Example
Convert the following 1-D array with 12 elements into a 2-D array.

The outermost dimension will have 4 arrays, each with 3 elements:"""



import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
print('*'*100)



"""Example
Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension 
(will raise an error):"""


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)  #will get an error because  value is less

print(newarr)
print('*'*100)


"""Example
Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:"""


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)