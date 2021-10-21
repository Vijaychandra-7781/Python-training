"""write a program to given range of cube"""


def cube_range(num):# function definition

    cube = [] # empty list
    for i in range(1, num): # range of cube
        cube.append(i ** 3)
    print('the cube of given range list is:',cube)

cube_range(10) # function calling
