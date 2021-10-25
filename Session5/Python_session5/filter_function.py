"""Filter function is a built in function

In this filter function criteria or condition is matching it gives the result otherwise its rejecting or remove

Filter function accepts two arguments one is function and another one is arguments

The filter() method filters the given sequence with the help of a function that tests
 each element in the sequence to be true or not.
"""

# examples

def odd_out(num): # odd out function definition

    if num%2==0:  # in this condition num completely divides two returns otherwise the value remove
        return True

    else:
        return False

list_obj=[1,23,5,7,8,88,12,45,66]

filter_obj=filter(odd_out,list_obj)  # filter takes two arguments one is function_name and and iterable type
print('this is the odd_out result:',list(filter_obj))
print('*'*100)


# Another example

def movies(names) : # function define

    if names.startswith('a'):  # this is the condition movie name starts with a it is printed otherwise remove
        return True

    else:
        return False

movie_list=['anjaan','kotigobba','persuit_of_happiness','ambari','a','Power'] # list

filter_obj=filter(movies,movie_list)  # filter condition

print(list(filter_obj))

print('*'*100)


# another example

ages = [5, 12, 17, 18, 24,21, 32]

def myFunc(x): # function definition

  if x < 18: # if  age less tan 18 it will removes age greterth an 18  it will goes to print
    return False

  else:
    return True

adults = filter(myFunc, ages)

print(list(adults))

# for x in adults:
#   print(x)




