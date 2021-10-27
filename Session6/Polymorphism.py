"""An object showing differnt behaviour in differnt stages of its life cycle is called as Plymorphism

How to acheive Polymorphism
They are two rules :
1.Inheritance
2.Method overriding

What is method overriding

When super class have one method and sub class have one method ,both method have same name is called as
method overriding"""

# Example of method overriding

class demo1:
    def test(self):
        print('running test function')

class demo2(demo1):
    def test(self):
        print('running overriden method')

d1=demo2()
d1.test()


# Another example of method overriding


class Person:  # class name

    # Constructor
    def __init__(self, name,age,gender):
        self.name = name
        self.age=age
        self.gender=gender

    # To get name

    def details(self): # instance method
        print('employee name is:',self.name)
        print('employee age is:',self.age)
        print('employee gender is:',self.gender)

class employee(Person):  # inherit person

    def __init__(self,name,age,gender,id,salary,designation):
        super().__init__(name=name,age=age,gender=gender)
        """ This is compulsory call the super class otherwise inheritance doesn't happen,once you initialize 
         the instance attribute you compulsory using super method"""
        self.id=id
        self.salary=salary
        self.designation=designation

    def details(self): # instance method
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

e1.details()


# example of polymorphism


class animal:

    def noise(self):
        print('animal make noise')

class cat(animal):

    def noise(self):
        print('meow meow')

class dog(animal):

    def noise(self):
        print('bow bow')

class snake(animal):

    def noise(self):
        print('hush hush')

class animal_simulator:

    def makenosie(self,animal):
        animal.noise()

c1=cat()
d1=dog()  # object creation
s1=snake()
a1=animal_simulator()

ans=int(input('type1----->cat \n 2----> dog \n 3-------> snake '))   # this is like switch statement

if ans==1:
    a1.makenosie(c1)

elif ans==2:
    a1.makenosie(d1)

elif ans==3:
    a1.makenosie(s1)

else:
    print('invalid option')





# Another example of  Normal Polymorphism and method overriding


class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()



