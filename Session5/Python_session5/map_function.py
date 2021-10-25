"""Map function is the built in function in python
Map function execute a specified function for each item of iterable type is called map

Mpa function it accepts two arguments one is function or fun_name and another one is iterable_type"""


# Example

def square(num):# function definition

    return num*num

numbers=[2,4,6,8,7]# list
map_obj=map(square,numbers)# map function accept two argumnet one is fun name and iterable type
print(list(map_obj)) # add the result to the list
# for val in map_obj:
#     print(val)
print('*'*100)


# Another example

def cities(names):  #function

    return len(names) # return the result len of names

city_names=['bangalore','chennai','mysore','hyderbad','kerala'] # list

map_obj=map(cities,city_names) # map function
print(list(map_obj))
print('*'*100)


# another example

def add_names(a,b): # function definition

    return a+b # concatenate

a=['vijay','amal','abbas','mukund']# list
b=[' chandra',' antony',' ali',' kumar'] # list

map_obj=map(add_names,a,b) # map function
print(list(map_obj))
print('*'*100)

# another example

def is_even(num): # fun defintion

    return num%2==0 # if it is even it give the result in boolean form like true or false

num=[1,23,45,6,8,22]

map_obj=map(is_even,num)
print(list(map_obj))