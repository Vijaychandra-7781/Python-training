"""A lambda function is also called as a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

syntax :  is the syntax of lambda function) """

# Lambda function uses
"""We use lambdlambda arguments : Expression
 (This a functions when we require a nameless function for a short period of time.

A lambda function is typically used to define the filtering logic and is passed as the 
first argument of filter() .

Lambda function is typically used to define the map function and is passed as the first argument map()"""

#Example

x = lambda a : a + 10 # This is the lamda function with one argument a  and x is acts as a function
print(x(10)) # in this line we pass the value to a
print('*'*100)

#example

full_name = lambda first, last:  {first.title(),last.title()} # This title() string method
print(full_name('guido', 'van rossum'))
print('*'*100)

# Example
def myfunc(n):# function definition

  return lambda a : a * n

mydoubler = myfunc(2)# assign to another name

print(mydoubler(11))

print('*'*100)


#Example

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
