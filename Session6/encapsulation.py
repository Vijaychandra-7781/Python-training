"""Encapsulation is the proces of binding data to its associate method to the class or entity with using the
relevant access specifier is called as encapsulation

What is access specifier

It restricts the access of variable or any thing it is called as access specifier
In access specifier 3 types

1.private (__): It is used only inside the classs.

2.protected(_):It can be used in another class with using the inheritance.

3.public:It can be used any where .

Uses:
It describes the idea of wrapping data and the methods that work on data within one unit.

This puts restrictions on accessing variables and methods directly and can prevent the accidental
 of data.
"""

#Example for private access specifier

class demo1:

    def __init__(self):
        self.__var1=100
        self.__var2=200  # this is the private variable onlu used in this class only outside the class doen't access
    def print_atributes(self):
        print('this is the private variable:',self.__var1)

d1=demo1()
d1.print_atributes()



#example for the public


class student:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.studentName = name
        self.studentAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.studentAge)


# creating object of the class
obj = student("R2J", 20)

# accessing public data member
print("Name: ", obj.studentName)

# calling public member function of the class
obj.displayAge()



"""this is the example for protected"""


class Student:


    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class demo(Student):  # inheritance

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        # self._displayRollAndBranch()


# creating objects of the derived class
obj = demo("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()
obj._displayRollAndBranch()



""" This is the example of private"""


class student:
    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):
        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self):
        # accesing private member function
        self.__displayDetails()

    # creating object


obj = student("R2J", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()