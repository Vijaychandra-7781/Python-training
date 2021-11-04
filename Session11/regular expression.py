"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:"""



"""why it is use
Regular expressions are particularly useful for defining filters.

Regular expressions contain a series of characters that define a pattern of text to be matched—to make a
 filter more specialized,"""

#Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)# * indicates zero or more characters and ^ satrts with and $ ends with



#The re module offers a set of functions that allows us to search a string for a match:

"""findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string"""



import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # if it is match it is printed in the list otherwise it show empty list

print('*'*100)




txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
print('*'*100)


"""Search for the first white-space character in the string:"""




txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

print('*'*100)

#Another example

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print('*'*100)
"""Split at each white-space character:"""


import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

print('*'*100)
"""Split the string only at the first occurrence:"""


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


"""Replace every white-space character with the number 9:"""


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

print('*'*100)


"""Replace the first 2 occurrences:"""



import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)