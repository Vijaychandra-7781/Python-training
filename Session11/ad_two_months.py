# from datetime import date, timedelta
# import calendar
# start_date = date.today()
# days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
# print(start_date + timedelta(days=days_in_month))

#this is how to add days
from datetime import date, timedelta

today_date = date.today()

print("CURRENT DAY : ", today_date)

# as said earlier it takes argument as day by default
td = timedelta(30)

"""datetime.timedelta() method which processes timedelta object. 
The number of days to be added is passed as an argument to the timedelta function and 
it returns the date in the given format that is year-month-date-hours:minutes:seconds. """


print("AFTER 5 DAYS DATE WILL BE : ", today_date + td)


print('*'*100)




# first instal pip install python-dateutil
"""The relativedelta type is designed to be applied to an existing datetime and can replace 
specific components of that datetime, or represents an interval of time."""
from datetime import date
from dateutil.relativedelta import relativedelta

six_months = date.today() + relativedelta(months=+6)
print(six_months)



print('*'*100)
#another example

