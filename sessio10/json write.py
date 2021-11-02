"""Java script object notation

json is a light weight format for storing and transporting the data

Writing JSON to a file in python

Serializing JSON refers to the transformation of data into a series of bytes (hence serial) to be stored or
transmitted across a network.

To use dump() or dumps()
dictionary – name of dictionary which should be converted to JSON object.

indent – defines the number of units for indentation.

"""


# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"age" : 56,
	"gender" : "male",
	"phonenumber" : "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)

print('*'*100)

#another example

# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

with open("sample1.json", "w") as outfile:
	json.dump(dictionary, outfile)


"""Reading JSON from a file using python
Using json.load()

The JSON package has json.load() function that loads the json content from a json file into a dictionary."""


# Python program to read JSON
# from a file


import json

# Opening JSON file
with open('sample.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

print(json_object)
print(type(json_object))


print('*'*100)

import json
try:
	fh=open('sample.json','r')
	company_obj=json.load(fh)
	print(type(company_obj))
	print(company_obj)
except Exception:
	print('error occured')
finally:
	fh.close()




print('*'*100)

import json

emp_details={'id':121,'empname':'vijay','salary':12000,'gender':'male'}

emp_obj=json.dumps(emp_details)

print(emp_obj)
