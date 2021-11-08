"""Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

If the value at an index is True that element is contained in the filtered array,
if the value at that index is False that element is excluded from the filtered array.

Filtering an array means to getting some elements out of the original array and creating a newer one.

In NumPy, the Boolean index list is used to filter an array.

If the value at an index is True that element is appended in the filter array otherwise
it's is excluded from the filtered array.

Example
Create an array from the elements on index 0 and 2:"""

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

print('*'*100)

#The example above will return [41, 43], why?

#Because the new filter contains only the values where the filter array had the value True, in this case, index 0 and 2.


"""Example
Create a filter array that will return only values higher than 42:"""

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print('*'*100)


"""Example
Create a filter array that will return only even elements from the original array:"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
