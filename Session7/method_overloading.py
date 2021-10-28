"""Method overloading is the class having methods are the same name with diffrent arguments.

Arguments different wiil be based on a number of arguments and types of arguments.

It is used in a single classs
It is also used to write the code clarity as well as reduce complexity.

Normally methods are used to reduce the complexity.

It is also used for reusablity.

"""

# Example

class employee:

    def hello_emp(self,e_name=None):

        if e_name is not None:
            print('hello:'+e_name)
        else:
            print('hello')

emp1=employee()
emp1.hello_emp()
emp1.hello_emp('vijay')


print('*'*100)


#Another example

# class area:
#
#     def find_area(self,a=None,b=None):
#
#         if a is not None:
#             print('area of rectangle:',(a*b))
#
#         elif a is not None:
#             print('area of square:',(a*a))
#
#         else:
#             print('nothing to print')
#
# obj1=area()
#
# obj1.find_area()
#
# obj1.find_area(10)
#
# obj1.find_area(10,20)


class Human:

    def sayHello(self, name=None, age=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

        if age is not None:#age!=None
            print( 'Age = ' + str(age))


# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')

# Call with two parameters
obj.sayHello('Guido', 18)




# this is another normal function example


def product(a, b):
    p = a * b
    print(p)


# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b * c
    print(p)


# Uncommenting the below line shows an error
#product(4, 5)

# This line will call the second product method
product(4, 5, 5)
