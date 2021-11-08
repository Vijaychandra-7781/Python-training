"""Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0,
and the second has index 1 etc.

It supports negative inddexing also"""


"""Get the first element from the following array:"""


import numpy as np

arr=np.array([1,2,3,4,5,6])

print('the first element values is:',arr[0])



"""Get the second element from the following array"""

print('the second element value is:',arr[1])

print('*'*100)


"""In numpy we can index values also."""


import numpy as np

vijay=np.array([12,24,36,48,12,10])

print('adding first index value and last index value is:',vijay[0]+vijay[-1])

print('*'*100)


"""Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing t
he dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the row represents the dimension 
and the index represents the column.


Access the element on the first row, second column:"""

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print('*'*100)


#Access the element on the 2nd row, 5th column:


import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
print('*'*100)


"""Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated integers representing the
 dimensions and the index of the element.
 
 
 Access the third element of the second array of the first array:"""


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])