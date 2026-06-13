# 1. Date-Time Module in python

# the datetime module in used to work with dates and times in python.

# Get current date and time
# Create custom dates
# Format dates
# Perform data calculations

#Inporting date time Module

import datetime

now=datetime.datetime.now()

print(now)

# current Date only

today=datetime.date.today()

print(today)

# customdate

custom=datetime.date(2024,12,24)

print(custom)

# Access year,Month,Day

today=datetime.date.today()

print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)

# Strftime () is used to format date and time.

now=datetime.datetime.now()

formatted=now.strftime("%d-%m-%Y%H:%M:%S")

print(formatted)

# date differnce

d1=datetime.date(2002,12,1)
d2=datetime.date(2026,6,11)

difference=d2-d1

print(difference.days)

# 2.time module in python

# working with system time
# Dealys in program
# Mesuring execution time

# Import time module

import time

current=time.time()

print(current)

# It returns seconds from January 1,1970

# Pause Program using Sleep()

print("start")

time.sleep(3)

print("End ofter 3 seconds")

# current localtime

local=time.localtime()

print(local)

# Formate time

current=time.strftime("%H:%M:%S")

print(current)

# Measure Execution Time

start=time.time()

for i in range (1000000):
    pass

end=time.time()

print("Execution Time:",end-start)

# 1.Display Current Date and Time

from datetime import datetime

now=datetime.now()

print(now)
print("year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("second:",now.second)

# 1.datetime.datetime.now()
# retuns current date and time
# 2.datetime.date.today()
# return current date

# 3.datetime.datetime.today()
# return current local date and time

# 4.datetime.datetime.UTC now()
# return curren UTC time.

import datetime

print(datetime.datetime.utcnow)

# 5.strftime()
# format date/time in to string.

# 6.strptime()
# converts string into datetime object.

from datetime import datetime 

date="2025-06-11"

obj=datetime.strptime(date,"%Y-%m-%d")

print(obj)

# 7.timedate

# used to date calculation

from datetime import datetime,timedelta

today=datetime.now()

future=today+timedelta(days=5)

print(future)

# 8.replace

# Replace year/month/day ect......

now=datetime.now()

now_date=now.replace(year=2030)

print(now_date)

# 9.date()

# 10.time()

# Extract only date.

# 11.weekdays()

# return weekday number.

now=datetime.now()

print(now.weekday())

# 12.isoweekday()

# return readable weekdays number(1-7)

now=datetime.now()

print(now.isoweekday())

# 13. Ctime

# return readable date and time

now=datetime.now()

print(now.ctime())

# 14.timestamp()

# return seconds since epoch

now=datetime.now()

print(now.timestamp())

#  15.form timestamp()

# converts timestamp to datetime.

s=1749863000

print(datetime.fromtimestamp(s))

# Python time Module Method

#1.time()
#2.ctime()
#3.sleep()
#4.local time()
#5.gmtime()

# returns UTC time object.

import time

print(time.gmtime())

#6.strftime()
#7.strptime()
#8.mktime()

# converts time.tuple in seconds

import time

t = time.localtime()

print(time.mktime(t))

# 9.asctime()

import time

t = time.localtime()

print(time.asctime(t))

# 10. perf_ciunter()

# 11.process_time()

# 12.monotonic()

# Returns continously increasing clock value

import time

# Record the start time
start_time=time.monotonic()

# put the code you want to mesure here time.sleep(10)

# Record the end time
end_time=time.monotonic()

# Calculate exact duration
duration=end_time-start_time
print(f"The operation took {duration} seconds.")





