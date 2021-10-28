"""The constructor overloading is done by checking conditions for the arguments passed and performing required actions.
For example, consider passing an argument to the class sample,

 If the parameter is an int, the square of the number should be the answer.
If the parameter is a String, the answer should be “Hello!!”+string.
If the parameter is of length greater than 1, the sum of arguments should be stored as the answer."""



class Example:

    # constructor overloading based on args
    def __init__(self, *args):

        # if args are more than 1 sum of args
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

        # if arg is an integer square the arg
        elif isinstance(args[0], int): #The isinstance() function returns True if the specified object is of the specified type, otherwise False .
            self.answer = args[0] * args[0]

        # if arg is string Print with hello
        elif isinstance(args[0], str):
            self.answer = "Hello! " + args[0] + "."


e1 = Example(1, 2, 3, 6, 8)
print("Sum :", e1.answer)

e2 = Example(6)
print("Square :", e2.answer)

e3 = Example("Python")
print("String :", e3.answer)


# This is the example of overriding


class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


# this is another example of the overriding


class Individual:
#      Constructor#1
    def __init__(self):
        self.Enrolled_Name = input( " Enter Name of the Enrolled : " )
        self.Enrolled_age = input( " Enter age of the Enrolled : " )
        self.Enrolled_gender = input( " Enter gender of the Enrolled : " )
# Method
    def display(self):
        print( " \n \n Enter Name of the Enrolled : " , self.Enrolled_Name )
        print( " Enter age of the Enrolled : " , self.Enrolled_age )
        print( " Enter gender of the Enrolled : " , self.Enrolled_gender )
#      Define a class as 'Estimated_Marks'
class Estimated_Marks:
#      Constructor#2
    def __init__(self):
        self.stuClass = input( " Class of the Enrolled : " )
        print( " Estimated Marks per subject : " )
        self.Science = int(input( " Mark in Science: " ))
        self.maths = int(input( " Mark in Math: " ))
        self.history = int(input( " Mark in history: " ))
        self.hindhi = int(input( " Mark in Hindi: " ))
# Method
    def display(self):
        print( " Study in : " ,self.stuClass)
        print( " Total Estimated_Marks : " , self. Science + self.maths + self.history+ self.hindhi)
class Enrolled(Individual, Estimated_Marks):
    def __init__(self):
# Call ' Individual ' super class constructor
        Individual.__init__(self)
# Call ' Estimated_Marks ' super class constructor
        Estimated_Marks.__init__(self)
    def result(self):
# Call method of class 'Individual'
        Individual.display(self)
# Call method of class 'Estimated_Marks'
        Estimated_Marks.display(self)
#      Objects of class 'Enrolled'
Enrolled_1 = Enrolled()
Enrolled_2 = Enrolled()

print( " Note : The instances get initialized with the given valuesuccessfully " )