""" write a program to print duplicate value in the list"""


def duplicate_values(list):

    for i in range(0,len(list)):
        for j in range(i+1,len(list)-1):
            if list[i]==list[j]:
                print('this is the duplicate values:',list[j])

duplicate_values(list=[1,2,3,43,5,4,1,3,7])