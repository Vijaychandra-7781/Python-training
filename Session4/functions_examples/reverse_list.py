"""write a program to reverse the list using for loop"""


def reverse_list(list):# function definition
    l1=[]

    for i in range(len(list)-1,-1,-1):
        l1.append(list[i])
    print('the reverse list is:',l1)



reverse_list(list=[10,20,30,40,50])# function calling
