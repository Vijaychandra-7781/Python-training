"""wap to add all number from the list using reduce function and lambda expression"""


import functools
scores = [75, 65, 80, 95, 50]

total = functools.reduce(lambda a, b: a + b, scores) # with using lambda and reduce function

print(total)



def do_sum(x1, x2): # function definition
    return x1 + x2

print(functools.reduce(do_sum, [1, 2, 3, 4])) # the reduce function



# numbers=[10,20,30,40]
# sum=functools.reduce(a+b,numbers) # this one is normal reduce
# print(sum)