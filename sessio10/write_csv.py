"""Python provides an in-built module called csv to work with CSV files.
 There are various classes provided by this module for writing to CSV:

 Using csv.writer class
Using csv.DictWriter class

csv.writer class is used to insert data to the CSV file.

Syntax: csv.writer(csvfile)

csv.writer class provides two methods for writing to CSV. They are writerow() and writerows().

writerow(): This method writes a single row at a time. Field row can be written using this method.
Syntax:   writerow(fields)

writerows(): This method is used to write multiple rows at a time. This can be used to write rows list.

syntax:  writerows(rows)"""


#Exaample


import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)



"""Using csv.DictWriter class
This class returns a writer object which maps dictionaries onto output rows.

syntax:csv.DictWriter(csvfile, fieldnames)

csv.DictWriter provides two methods for writing to CSV. They are:

writeheader(): writeheader() method simply writes the first row of your
 csv file using the pre-specified fieldnames.
 
 syntax: writeheader()
 
 writerows(): writerows method simply writes all the rows but in each row, 
 it writes only the values(not keys).
 
 syntax: writerows(mydict)"""

# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records1.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)







#another example
print('*'*100)

# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("data.csv")


print(df[0:10:2])

