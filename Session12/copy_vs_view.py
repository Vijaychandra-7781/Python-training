"""The copy owns the data and any changes made to the copy will not affect original array,
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array,
and any changes made to the original array will affect the view.



Example
Make a copy, change the original array, and display both arrays:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print('after copying:',arr)#The copy SHOULD NOT be affected by the changes made to the original array.
print(x)

print('*'*100)
"""Example
Make a view, change the original array, and display both arrays:"""


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print('after view method is apply:',arr)
print('original also affected :',x)