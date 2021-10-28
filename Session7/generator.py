"""A function yielding a value is known as Generator

A generator-function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return. If the body of a def contains yield,
the function automatically becomes a generator function.

Generator is a function that yields an traversable objects

It gives only one value at a time and when it is required


In normal function will use the return  but in generator we use yeild keyword

Python Generator functions allow you to declare a function that behaves likes an iterator,
allowing programmers to make an iterator in a fast, easy, and clean way.

"""

#  normal function example

def myfun():
    print('calling myfun')

    return 1

val=myfun()
print(val)

print('*'*100)


# example of generator

def myfun():
    print('my function')
    yield 1
    yield 2
    yield 3
    yield 4
val=myfun()
print(val)
val1=myfun()
print(val1)
print(type(val1))  # now cheking the type

print(next(val1)) # with using the next method iterate yield values

print(next(val1))
print(next(val1))
print(next(val1)) # once finished the yeild value then stops the iteration

print('*'*100)
# another example

def simpleGeneratorFun():
    yield 'vijay'
    yield 'chandra'
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
print('*'*100)


# Another example

# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
# print(x.next())  # In Python 3, __next__()
# print(x.next())
# print(x.next())
# print(x.next())
# print(x.next())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)



