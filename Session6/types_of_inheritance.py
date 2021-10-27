"""There are 4 types of inheritance

1. single inheritance  : In this type of inheritance the subclass inherits from the one super class
                        is called as single inheritance"""

# Example for single inheritance

# Base class
class Parent:

    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):

    def func2(self):
        print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()


# Another example of single inheritance


class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class employee(person):
    def __init__(self,name,age,gender,id,salary):
        super().__init__(name=name,age=age,gender=gender)
        self.id=id
        self.salary=salary

    def display(self):
        print('employee name is:', self.name)
        print('employee age is:', self.age)
        print('employee gender is:', self.gender)
        print('employee id is:', self.id)
        print('employee salary is:', self.salary)

name=input('enter the name:')
age=int(input('enter the age:'))
gender=input('enter the gender:')
id=input('enter the id:')
salary=float(input('enter the salray:'))

obj=employee(name,age,gender,id,salary)
obj.display()
print('*'*100)

"""2.Multilevel inheritancfre:
In this type of inheritance the subclass inherits from the super class inherit from the another super class
 """

# Example of multilevel

class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)


# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son('vijay', 'chandru', 'shiva')
print(s1.grandfathername)
s1.print_name()

print('*'*100)



"""3.Multiple inheritance:
In this type of inheritance the sub class inherits from the more than one super class is called multiple

"""


class demo1:
    def display(self):

        print('running demo1 function')
class demo2: # method resolution order using
    def __init__(self):
        self.y=20
        print('running demo2 function')

class sample1(demo1,demo2):  # in this one it prefer only first class demo1 because inside this class we using
    #init method that so first class will prefered
    def __init__(self):
        super().__init__()
        self.z=30
        print('running sample function')

s1=sample1()
print('the value of y:',s1.y)
print('the value of z:',s1.z)



print('*'*100)


"""4.Heirarchial inheritance:
In this type of inheritance the super class properties are inherited to more than one sub class 
 is called as heirarchial inheritance"""



# example of heirarchial inheritance

class demo1:
    def __init__(self):
        self.x=10
    def test(self):
        print('running test function')

class demo2(demo1):
    def __init__(self):
        super().__init__()
        self.y=20
        print('running init function')

    def disp(self):
        print('running disp function')

class demo3(demo1):
    def __init__(self):
        super().__init__()
        self.z=30
    def view(self):
        print('running view function')

d1=demo2()
d1.test()
d1.disp()
print(d1.x,d1.y)

d2=demo3()
print(d2.x,d2.z)
d2.test()
d2.view()

print('*'*100)


#another example of heirarchial inheritance

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


# Derivied class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

