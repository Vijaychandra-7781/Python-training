"""The time Module
There is a popular time module available in Python which provides functions for working
with times and for converting between representations.

"""


import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)


print('*'*100)
"""Getting current time
To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, 
pass the floating-point value to a function
 (e.g., localtime) that returns a time-tuple with all nine items valid."""


import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)



"""Getting formatted time
You can format any time as per your requirement, 
but simple method to get time in readable format is asctime() """

print('*'*100)
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)