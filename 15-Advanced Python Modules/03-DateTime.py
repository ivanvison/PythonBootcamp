import os
from traceback import print_tb
os.system('cls')
import datetime

mytime = datetime.time(18,20,1,20)
print(mytime.minute)
print(mytime.hour)
print(mytime.microsecond)
print(mytime)
print()

today = datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)

print(today.ctime())

mydatetime = datetime.datetime(2021,10,3,14,20,1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

# Date math
date1 = datetime.date(2021,11,3)
date2 = datetime.date(2020,11,3)
result = date1 - date2
print(type(result))
print(result)

# Datetime
datetime1 = datetime.datetime(2021,11,3,22,0)
datetime2 = datetime.datetime(2020,11,3,12,0)
result2 = datetime1 - datetime2
print(result2)
print(result2.seconds)
print(result2.total_seconds())
