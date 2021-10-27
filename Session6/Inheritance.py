"""A class acquiring the properties of another class is called inheritance

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Uses:
Inheritance allows us to define a class that inherits all the methods and properties from another class.
"""

# Example

class demo1:
    x=10
    y=20

class disp(demo1):# inherit
    print('the x value is:',demo1.x)
    print('the y value is:',demo1.y)

d1=disp()




class Person:  # class name

    # Constructor
    def __init__(self, name,age,gender):
        self.name = name
        self.age=age
        self.gender=gender

    # To get name
    def display(self):
        print('the name is:',self.name)
        print('the age is:',self.age)
        print('the gender is:',self.gender)

class employee(Person):  # inherit person

    def __init__(self,name,age,gender,id,salary,designation):
        super().__init__(name=name,age=age,gender=gender)
        """ This is compulsory call the super class otherwise inheritance doesn't happen,once you initialize 
         the instance attribute you compulsory using super method"""
        self.id=id
        self.salary=salary
        self.designation=designation

    def disp(self): # instance method
        print('employee name is:',self.name)
        print('employee age is:',self.age)
        print('employee gender is:',self.gender)
        print('employee id is:',self.id)
        print('employee salary is:',self.salary)
        print('employee designation is:',self.designation)

name=input('enter the name:')
age=int(input('enter the age:'))
gender=input('enter the gender:')
id=input('enter the id:')
salary=float(input('enter the salray:'))
designation=input('enter the designatiom:')


e1=employee(name=name,age=age,gender=gender,id=id,salary=salary,designation=designation)

e1.disp()


"""In inheritance 4 types 
1.single inheritance
2.multileve inheritance
3.multiple inheritance
4.heirarchial inheritance"""


