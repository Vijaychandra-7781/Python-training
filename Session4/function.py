"""A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

Once we define a function we can use any number of times
one function may call so many times.
functions are reusable
"""
def test():  # this is the function definition
    print('running test function ')

test()
test()# function calling

# you can create a function must and should call the function otherwise that block of code waste

# another example of the function
def square(num): # this is the function definition and also pass one parameter num
    n1=num*num
    print('the square of num is:',n1)
num=int(input('enter the number for square:'))
square(num) # when we call the function we can pass the parameter value compulsory otherwise it show error

# example
pi=3.14 # global variable
def diameter(r): # fun define

    res=2*r
    print('the diameter is:',res)

def area(r): # function define
    res1=pi*r*r
    print('the area of the circle is:',res1)

def circum(r):# function define
    res2=2*pi*r
    print('the circumference is:',res2)

r=int(input('enter the radius:'))
diameter(r) # function calling
area(r)
circum(r)

#another example
def add(a,b): # fun define

    return a+b  # in return function only gives the result when it function call

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

print('the both value sum is:',add(a,b))# function calling

