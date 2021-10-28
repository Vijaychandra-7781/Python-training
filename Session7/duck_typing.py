"""Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc.

Duck typing is a concept related to dynamic typing

where the type or the class of an object is less important than the method it defines. Using Duck Typing,

 we do not check types at all. Instead, we check for the presence of a given method or attribute."""


#Example


# duck typing


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("fish swim in sea")


# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(): #We are neglecting fish class
    obj.fly()

#In this example, we can see a class supports some method we can modify it or give them new functionality.
# Duck-typing emphasis what the object can really do, rather than what the object is.



# another example

class VisualStudio:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Spell Check')
        print('Convention Check')


class Desktop:
    def code(self, ide):
        ide.execute()


ide = VisualStudio()
desk = Desktop()
desk.code(ide)