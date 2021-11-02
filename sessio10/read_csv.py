"""A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'."""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())


"""use to_string to print the entire DataFrame.

By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows:"""

print('*'*100)
import pandas as pd

df = pd.read_csv('data.csv')

print(df)


"""Read json

Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, 
including Pandas.

In our examples we will be using a JSON file called 'data.json'.

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries."""


#load a python dictionary into a dataframe

print('*'*100)

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)

print('*'*100)


"""Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top."""



import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(6))


print('*'*100)


"""In default it will give the five rows"""

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

"""There is also a tail() method for viewing the last rows of the DataFrame.

The tail() method returns the headers and a specified number of rows, starting from the bottom."""

print('*'*100)

import pandas as pd

df = pd.read_csv('data.csv')

print(df.tail())


"""Info About the Data
The DataFrames object has a method called info(), that gives you more information about the data set."""
print('*'*100)
import pandas as pd

df = pd.read_csv('data.csv')

print(df.info())


