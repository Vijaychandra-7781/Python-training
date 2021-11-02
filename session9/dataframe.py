"""A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,
or a table with rows and columns.

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
"""



import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


print('*'*100)


#another example

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40,30]  # All arrays must be the same length otherwise vale error occured
}

myvar = pd.DataFrame(data)

print(myvar)
print('vijay')
"""would like to see only one row using loc method """

print(myvar.loc[:])# this is the slicing in pandas using loc and : method

print(myvar.loc[0])# only access selected rows

print(myvar.loc[[0,1]]) #this is two row access

print(myvar.loc[[0,1,2]])


"""we can create our own index values"""

print('*'*100)


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

print(df.loc['day1'])


"""How to access data  in data frame"""

print('*'*100)

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])

print('*'*100)


"""How to add the data to the data frame"""


# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Height': [5.1, 6.2, 5.1, 5.2],
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address

# Observe the result
print(df)


print('*'*100)
