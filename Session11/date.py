"""A date in Python is not a data type of its own, but we can import a module named datetime
to work with dates as date objects.

Why its use

How to get current date and time using programatically

and also used some applications because that application shows the current date and time"""

#Import the datetime module and display the current date:


import datetime

x = datetime.datetime.now()
print('the current datetime is:',x)


"""When we execute the code from the example above the result will be:

2021-11-03 12:14:24.742133
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

"""

#Return the year and name of weekday:

print('*'*100)
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) # it is used to get the weekday
#%a this is the short week day version



#Create a date object:
print('*'*100)

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)



#Display the name of the month:

print('*'*100)
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%b"))  # inside strftime %b gives it gives short format




"""

date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, 
in effect. Its attributes are year, month and day.

time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. 
Its attributes are hour, minute, second, microsecond, and tzinfo.

datetime – Its a combination of date and time along with the attributes 
year, month, day, hour, minute, second, microsecond, and tzinfo."""



#Example 1: Date object representing date in Python


# import the date class
from datetime import date


# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

print('*'*100)




#Example 2: Get Current Date


from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

print('*'*100)




#Example 3: Get Today’s Year, Month, and Date


from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

print('*'*100)



"""Example 5: Convert Date to String
We can convert date object to a string representation using two functions isoformat() and strftime()."""

from datetime import date

# calling the today
# function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
print('*'*100)



"""Time class
The time class creates the time object which represents local time, independent of any day. """

from datetime import time

# calling the constructor
my_time = time(13, 24, 56)

print("Entered time", my_time)


# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)
print('*'*100)



#Example 2: Get hours, minutes, seconds, and microseconds


from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)
print('*'*100)

"""Example 3: Convert Time object to String
We can convert time object to string using the isoformat() method."""

from datetime import time

# Creating Time object
Time = time(12, 24, 36, 1212)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))
print('*'*100)



