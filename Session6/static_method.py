"""
1.Python doesn’t implicitly pass the cls argument to static methods.

2.Static methods cannot access or modify the class state.

3.Use @staticmethod decorators to define static methods.

"""

from datetime import date

class Person:

    # class constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18


# Driver's code
person1 = Person('Mark', 20)
person2 = Person.details('Rohan', 1992)
person1.details('vijay',2010)
print(person1.name, person1.age)
print(person2.name, person2.age)
print(Person.check_age(25))