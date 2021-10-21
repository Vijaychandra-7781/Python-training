"""
The function calling itself is called recursion.
Recursion is made for solving problems that can be broken down into smaller.
Recursion is a common mathematical and programming concept.
"""

# example

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1: # if x value is equal to one comes out of the condition otherwise x is not equal to 1 goto else
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is:", factorial(num))