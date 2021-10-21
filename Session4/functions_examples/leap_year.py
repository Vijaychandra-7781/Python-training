
"""Write a program to check whether leap year or not"""


def leap_year(year):# function defining

    if year%4==0 and year%400==0:
        print('it is a leap year')

    elif year%100==0:
        print('it is not a leap year')

    else:
        print('it is not a leap year')

year=int(input('enter the year:'))
leap_year(year) # function calling