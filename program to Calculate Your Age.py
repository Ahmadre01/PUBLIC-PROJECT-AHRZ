# A program to Calculate Your Age
import time 
from calendar import isleap

# judge the leap year 
def judge_leap_year(year) :
    if isleap(year):
        return True
    else : 
        return False
# return number of days in each month 
def month_days(month,leap_year) : 
    if month in [1,3,5,7,8,10,12] : 
        return 31
    elif month in [4,6,9,11] : 
        return 30 
    elif month == 2 and leap_year : 
        return 29 
    elif month == 2 and (not leap_year) :
        return 28
Name = input("enter your name ==> ")
age = int(input("enter your age ==> "))
local_time = time.localtime(time.time()) # get local time from system  clock 

year = int(age)
month = year * 12 + local_time.tm_mon
day = 0
begin_year = int(local_time.tm_year) - year 
end_year = begin_year + year
# calculate the days ==> 
for y in range(begin_year,end_year) :
    if (judge_leap_year(y)) : 
        day = day + 366
    else : 
        day = day + 365 
leap_year = judge_leap_year(local_time.tm_year)
for m in range (1,local_time.tm_mon) : 
    day = day + month_days(m,leap_year)
day = day + local_time.tm_mday
print("%s 's age is %d years or " % (Name,year),end=" ")
print("%d months or %d days" % (month,day))
