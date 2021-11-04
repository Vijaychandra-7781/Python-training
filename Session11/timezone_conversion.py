from datetime import datetime
import pytz

# get the standard UTC time
UTC = pytz.utc

# it will get the time zone
# of the specified location
IST = pytz.timezone('Asia/Kolkata')

# print the date and time in
# standard format
print("UTC in Default Format : ",
      datetime.now(UTC))

print("IST in Default Format : ",
      datetime.now(IST))
datetime_utc = datetime.now(UTC)
print("Date & Time in UTC : ",
      datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))


print('*'*100)

"""anoher example ust means univeersal time co ordinate and ist means indian standard time"""


"""The astimezone() function is used to return a DateTime instance according 
to the specified time zone parameter tz. """

from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))
# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))



print('*'*100)
"""this is the reverse"""



from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_ist = datetime.now(timezone('Asia/Kolkata'))
print(now_ist.strftime(format))
# Convert to Asia/Kolkata time zone
now_universe = now_ist.astimezone(timezone('UTC'))
print(now_universe.strftime(format))