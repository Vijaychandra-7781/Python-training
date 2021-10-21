"""" First one is Positional Parameter

All function with positional parameter it is compulsory  to pass the value with according to the position.

Compulsory to pass the value to specific position otherwise will get error"""

# Example

def test(x,y):# function define with parameters

    print('the x value is:',x)
    print('the y value is:',y)

test(10,20) # fun calling and also pass the values to arguments

print('*'*100)

""" second one is Default parameter
A fun can be define a default parameter value a parameter defined with the value"""

# example

def add(x=10,y=20):# fun define with deafult parameter value

    sum=x+y
    print('the sum is:',sum)

add() # calling without parameter value

add(25)# calling single parameter value

add(25,30)# calling both parameter value, in java this one is called method overloading

print('*'*100)


""" Third one is Keyword parameter type
The fun treats each parameter as a keywod
When call the function the caller funtion can assign the value to the parameter through key value pair

In this function we can change the order of the parameter """

# Example

def division(a,b):  # function define

    res=a/b
    print('the division result is:',res)

division(a=10,b=2)# this is one type of calling

division(10,b=5)# this is another type of calling

division(b=3,a=10) # this is another way of calling this one is working
print()

# another example

def multiplication(a=10,b=10):# this is another way
    return a*b

print('the multiplication of both number is:',multiplication())

print("*"*100)



"""Fourth one is Varying parameter

* args represents the it take many arguments
** args represents the it takes many argument but it only accept keyword argument like a=10,b=20 like this

"""


# example

def addition(*args): # fun define
   res = 0
   for i in args:
      res += i
   return res
print('the addition is:',addition(10,20))
print('the addition is:',addition(10,20,30))    # calling differnt ways 
print('the addition is:',addition(10,20,40,12))
print('the addition is:',addition(10,20,10,20,30,30))

print('*'*100)



def test(**param):
    print('total parameter',len(param))

test()
test(x=10,y=20) # it accepts only keyword paramter

test(x=10,y=20,z=30) #it is not accepted  only accept keyword parameteer


