""" one is Function with No Arguments, and No Return Value

In this type of function , While defining, declaring, or calling the function,
We won’t pass any arguments to the function."""

# example

print('This is the example of Function with No Arguments, and No Return Value')

def add():  # function defining no argument pass in this function
    a=10
    b=20
    sum=a+b
    print('sum of two number is:',sum)
add()  # function calling

# another example
def test():  # fun definition
    print('test function')
test() # function calling once we call the function execute the body of the function otherwise its waste
print("*"*100)


"""Second one is Function with no argument and with a Return value
In this type of function , We won’t pass any arguments to the function while defining, declaring, 
or calling the function. 
When we call the function, this type of function returns some value."""


# example

print("This is the example of Function with no argument and with a Return value ")

def division(): # funcion defining
    a=10
    b=2
    div=a/b
    return div # in return statements pass the results of this function
print('the division is:',division()) # function call

# Another example

def multiplication(): # fun define
    a=10
    b=20
    mul=a*b
    return mul
print('the multiplication is:',multiplication()) # function call

print('*'*100)

"""Third one is Function with argument and No Return value
This type of function  allows us to pass the arguments to the function while calling the function. But, 
This type of function won’t return any value when we call the function."""

#Example

def square(num):# function definition with  parameter

    res=num*num
    print('the square of the given number is:',res)

num=int(input('enter the number for square:'))
square(num)# function calling
print()

# Another example

def factorial(num):  # function define
    res=1

    for i in range(1,num):
        res=res*i
    print('the factorial of the given number is:',res)

num=int(input('enter yhe number for factorial:'))
factorial(num) # function calling

print('*'*100)



"""Fourth one is Function with argument and Return value
This type of python function allows us to pass the arguments to the function while calling the function. 
This type of functions in Python returns some value when we call the function."""

# example

def square(num): # function define
    return num*num

print('the square of the given number is:',square(10)) # function call

print('the square of the given number is:',square(12)) # function call
print()




#Another example

def sum(a,b): # function definition
    return a+b

print('the sum is:',sum(10,20)) # function calling