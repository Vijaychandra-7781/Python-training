"""Pandas is a Python library used for working with data sets..

Pandas is used to analyze data.

It has functions for analyzing, cleaning, exploring, and manipulating data.

why use pandas?

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.

Data Science: is a branch of computer science where we study how to store,
use and analyze data for deriving information from it.

what can pandas do?

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values.
This is called cleaning the data.

How to install pandas?

If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
pip means PIP is a package manager for Python packages, or modules if you like.

Install it using this command:pip install pandas.

How to check pandas version ?

using __version__ method

"""

import pandas
print(pandas.__version__)

"""what is series in pandas?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

"""
print('*'*100)
print('series example:')

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

"""what is label in pandas?

If nothing else is specified, the values are labeled with their index number. 
First value has index 0, second value has index 1 etc.

This label can be used to access a specified value."""
print('*'*100)

print('example of label:')
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(a[0])


"""In pandas we can create a index also with using the index method"""
print('*'*100)
print('this is the example of how to create index:')

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

#When you have created labels, you can access an item by referring to the label.

print(myvar['y'])

#You can also use a key/value object, like a dictionary, when creating a Series.

print('*'*100)
print('another example using dictionary:')

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


#To select only some of the items in the dictionary, use the index argument and specify
# only the items you want to include in the Series.

print('*'*100)
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

