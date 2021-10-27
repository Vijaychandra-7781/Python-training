"""Normal functional programming
The price is 50
quantity is 100

def total(price,quantity):
    return price*quantity
print(total(10,100))  This is the normal functional programming

In object oriented programming

what is object oriented programming
Object-oriented programming is a programming based on the concept of "objects",
which can contain data and code: data in the form of fields, and code, in the form of procedures.
A feature of objects is that an object's own procedures can access and often modify
the data fields of itself.

example

the price is 50 which price is 50 that is called object or entity

another example
color is black    color is var_name  black is value

which color is black that is called as object or entity





Class is a keyword is used to represent the object is called as calss.
or
The class is a definition block which is used to defined states and behaviour of object

Class decalration

class classname

Attribute types
1) Classs atributes
2)Instance attributes
"""

#Example

a=100   # this is not the class attributes

class demo1:   # class creation


    x=100   # these two are class attributes
    y=200

print('the value of a is:',a)  # it is working because it is not a class attribute it is global variable

#print(x)# it is not working because name error will occur

""" How to accesss class variable  with using class name we access class variable"""

#example

class test: # class name

    x=100
    y=200

print('the class attribute value of x:',test.x) # this is the way to access class variable

print('the class attribute value of y:',test.y)

"""We can modify the class variable with using class name"""
test.x=200
test.y=289

print('aftre modifyng the value of x:',test.x)

print('after modifying the value of y :',test.y)


class test2: # in this class not defining tany attribute
    pass

#print(test2.x)

test2.x=192  # addding the value to the class any part of the program

print('after adding the value x:',test2.x)

print(test2.__dict__)




