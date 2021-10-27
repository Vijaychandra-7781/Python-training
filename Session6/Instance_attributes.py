"""Instance attribute
Instance attribute creates inside te function

To access instance attribute and instance method

First we create object class with assigned objectname is called variable

How to craete a object
Instance attribute is used to initialize attribute with using the __init__ method.

var_name=classname()


"""
"""what is object

Any entity having its own atributes and behaviour is called as object

Every objet must have unique identification

 The class is a definition block which is used to defined states and behaviour of object

 __init__() method is used to initialize the instance attributes
 It is also called as constructor
 self keyword is used for which object is currently running that purpose we used self keyword"""


class demo1:

    def __init__(self):  # in this function we have to initialize the instance attributes

        self.x = 10
        self.y = 20


obj = demo1()
print(obj.x)  # with object name we can access the instance attributes


# Example

class demo2:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):   #  this is the instance method
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)


obj1 = demo2('vijay', 22, 'male')  # object creation and also pass argumnet values
obj1.display()

"""note: we are not accessing object attribute with using class name"""


class demo4:
    x = 100
    y = 200

    def __init__(self):
        self.a = 100
        self.b = 29202

    def disp(self): #This is the instance method
        print('A:', self.a)
        print('B:', self.b)


o1 = demo4()
o1.disp()
print('the class value x:', o1.x)  # we can access class atribute values using the object name
print('the class value y:', o1.y)  # but we don't access instance attributes with using the class name


# Example

class circle:  # class
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        dia = 2 * self.radius
        print('diameter of the circle:', dia)

    def area(self):
        area = 2 * circle.pi * self.radius
        print('the area of the circle is:', area)

    def circumference(self):
        circum = 2 * circle.pi * self.radius
        print('the circumference is:', circum)


radius = float(input('enter the radius:'))
obj2 = circle()
obj2.diameter(radius)
obj2.area(radius)
obj2.circumference(radius)