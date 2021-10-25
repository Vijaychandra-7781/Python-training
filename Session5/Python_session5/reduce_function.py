"""The reduce function is a functool module.
The reduce() function accepts a function and a sequence and returns a single value

Reduce function it accepts two arguments one is fun and iterable type or sequence"""


# example
import functools

def do_sum(x1, x2): # function definition
    return x1 + x2

print(functools.reduce(do_sum, [1, 2, 3, 4])) # the reduce function
print('*'*100)

# the output will show 4+3+2+1=10 is the output will show


# another example

def do_mul(a,b): # function definition

    return a*b  # this example like factorial

print(functools.reduce(do_mul,[2,3,4,5,6])) # reduce function it give result in single value
