"""Abstraction is used to hide the internal functionality of the function from the users.
 The users only interact with the basic implementation of the function, but inner working is hidden.

 The best example is switch inside functionality i dont know but out side its on and off only

 Uses:

 In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity."""

from abc import ABC


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()