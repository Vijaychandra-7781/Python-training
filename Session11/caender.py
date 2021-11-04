"""Python defines an inbuilt module calendar that handles operations related to the calendar.

The calendar module allows output calendars like the program and provides additional useful
 functions related to the calendar.

 why it is use

 Calendar module in Python has the calendar class that allows the calculations for
 various task based on date, month, and year.

  Python allows you to edit the calendar and use as per your requirement."""

#Example #1: Display the Calendar of a given month.


#import calender

import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))


"""Example #2: Display calendar of the given year."""
print('*'*100)
# importing calendar module
# for calendar operations
import calendar

# using calendar to print calendar of year
# prints calendar of 2018
print("The calendar of year 2018 is : ")
print(calendar.calendar(2018))


"""iterweekdays() method returns an iterator for the week day numbers that will be used for one week. 
The first number from the iterator will be the same as the number returned by firstweekday()."""

"""Syntax: iterweekdays()
Parameter: no parameter
Returns: iterator for the week day numbers"""

# importing calendar module
import calendar

# providing firstweekday = 0
obj = calendar.Calendar(firstweekday=0)

for day in obj.iterweekdays():
    print(day)


"""Operations on the calendar : 
1. calendar(year, w, l, c):- This function displays the year, the width of characters,
 no. of lines per week, and column separations.
2. firstweekday() :- This function returns the first week day number. By default 0 (Monday)."""
print('*'*100)
# importing calendar module for calendar operations
import calendar

# using calendar to print calendar of year
# prints calendar of 2012
print("The calendar of year 2012 is : ")
print(calendar.calendar(2012, 3, 1, 6))

# using firstweekday() to print starting day number
print("The starting day number in calendar is : ", end="")
print(calendar.firstweekday())



"""3. isleap (year):- This function checks if the year mentioned in the argument is a leap or not.

4. leapdays (year1, year2):- This function returns the number of leap days between the specified 
years in arguments."""
print('*'*100)
# importing calendar module for calendar operations
import calendar

# using isleap() to check if year is leap or not
if (calendar.isleap(int(input('enter the year:')))):
    print("The year is leap")
else:
    print("The year is not leap")

# using leapdays() to print leap days between years
print("The leap days between 1950 and 2000 are : ", end="")
print(calendar.leapdays(1950, 2000))


"""5. month (year, month, w, l) :- This function prints the month of a specific year mentioned in arguments. 
It takes 4 arguments, year, month, width of characters and no. of lines taken by a week."""


print('*'*100)
# importing calendar module for calendar operations
import calendar

# using month() to display month of specific year
print("The month 5th of 2016 is :")
print(calendar.month(2016, 5, 3, 2))



"""1. monthrange(year, month) :- This function returns two integers, first, 
the starting day number of week(0 as monday) , second, the number of days in the month.

2. prcal(year, w, l, c) :- This function also prints the calendar of specific year but 
there is no need of “print” operation to execute this."""
print('*'*100)
# importing calendar module for calendar operations
import calendar

# using monthrange() to print start week day and
# number of month
print("The start week number and no. of days of month : ", end="")
print(calendar.monthrange(2008, 2))

# using prcal() to print calendar of 1997
print("The calendar of 1997 is : ")
calendar.prcal(1997, 2, 2, 7)




"""3. prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need 
of “print” operation to execute this.

4. setfirstweekday(num) :- This function sets the day start number of week."""
print('*'*100)
# importing calendar module for calendar operations
import calendar

# using prmonth() to print calendar of 1997
print("The 4th month of 1997 is : ")
calendar.prmonth(1997, 4, 2, 1)

# using setfirstweekday() to set first week day number
calendar.setfirstweekday(4)

print("\r")

# using firstweekday() to check the changed day
print("The new week day number is : ", end="")
print(calendar.firstweekday())