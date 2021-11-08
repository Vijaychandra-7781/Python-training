"""Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.

This is very useful to serch the value of index position.

Example
Find the indexes where the value is 4:"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print('the value index postion is:',x)

print('*'*100)

"""Example
Find the indexes where the values are even:"""


import numpy as np

arr=np.array([12,23,42,44,56,67,88,12])

vijay=np.where(arr%2==0)

print('the even position is:',vijay)

print('*'*100)

"""Example
Find the indexes where the values are odd:"""


import numpy as np

arr=np.array([12,23,42,44,56,67,88,12])

vijay=np.where(arr%2==1)

print('the odd position is:',vijay)
print('*'*100)

"""The searchsorted() method is assumed to be used on sorted arrays.

Example
Find the indexes where the value 7 should be inserted:"""


import numpy as np
arr=np.array([21,22,26,34,12])

vijay=np.searchsorted(arr,12)

print('12 index position is:',vijay)

print('*'*100)


"""Example
Find the indexes where the values 2, 4, and 6 should be inserted:"""

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])  #in this case the value occupy the index postion but not permanently occupy

print(x)