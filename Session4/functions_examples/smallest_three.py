"""write a program to find the smallest value"""


def smallest_three(a,b,c):  # function definition

    if a < b and a < c: # compare the values for which one is small
        smallest = a
    if b < a and b < c:
        smallest = b
    if c < a and c < b:
        smallest = c
    print('the smallest number is:',smallest)

a=int(input('enter the first number:'))
b=int(input('enter the second number:'))#  user input
c=int(input('enter the third number:'))
smallest_three(a,b,c) #function calling