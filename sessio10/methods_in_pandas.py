"""version
it is used to check the version of pandas"""

import pandas
print(pandas.__version__)

"""series
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type."""
print('*'*100)
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

"""Index
In pandas we can create a index also with using the index method"""

print('*'*100)

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


"""Dataframe
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,
or a table with rows and columns."""

print('*'*100)

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


"""Slicing
this is the slicing in pandas using loc and : method"""

print('*'*100)

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

print(myvar.loc[:])

"""dump() and dumps() these method is used dictinary to normal string type

I am already given the example in json file"""


"""load() method is used to convert the string to dict type or json type"""

"""Head
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top."""


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))



"""Tail()
There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom."""

import pandas as pd

df = pd.read_csv('data.csv')
print(df.tail())


"""info()

The DataFrames object has a method called info(), that gives you more information about the data set."""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.info())