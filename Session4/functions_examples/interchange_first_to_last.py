"""write a program to interchange first and last element in a list"""

def interchange_first_to_last(list): # function definition

    res=list[-1:]+list[1:-1]+list[0:1] # interchanging the values

    print('after interchanging first value to last value:',res)


interchange_first_to_last(list=[1,2,4,5,4,6,8,9]) # function calling