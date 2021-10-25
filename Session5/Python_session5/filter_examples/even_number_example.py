"""WAP to filter even number in a list without flter and without lambda expression
"""



def even(num): # even function definition

    if num%2==0:  # in this condition num completely divides two returns otherwise the value remove
        return True

    else:
        return False

list_obj=[1,23,5,7,8,88,12,45,66]

filter_obj=filter(even,list_obj)  # filter takes two arguments one is function_name and and iterable type
print('this is the even number result:',list(filter_obj))



# example


def odd_out(n):
    if n%2==0:
        return True
    else:
        return False
print(odd_out(12))