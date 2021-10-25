"""WAP to double all the value in a list with map (with lambda exresssion)"""


def add(num): # function definition

    map_obj=map(lambda num:num+num,num) # map function it takes two arguments one is lamda fun and iterable type
    print(list(map_obj))

add(num=[1,2,3,4])  #function calling