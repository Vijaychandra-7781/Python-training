"""WAP to filter even number in a list with filter and lambda expression"""


def even(num): # function name wih define

    l1=filter(lambda num : num%2==0,num) # in this condition it is even it is printed otherwise rejected
    print(list(l1))

num=[12,13,34,33,45,56] # list
even(num) # function calling