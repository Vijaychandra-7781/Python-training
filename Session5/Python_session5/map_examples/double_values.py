
"""WAP to double all the value in a list with map (without lambda exresssion)"""



# Return double of n
def addition(n):# function definition
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))