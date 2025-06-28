'''
A leap year is a year that has 366 days instead of the usual 365. 
The extra day (February 29) accounts for the fact that a year is not 
exactly 365 days—it’s about 365.2422 days (due to Earth's orbit around the sun). 
To keep our calendars aligned with Earth's revolutions, we follow this rule:

A year is a leap year if:
  It is divisible by 4,
    and
  Not divisible by 100,
    unless
  It is also divisible by 400.
'''

def isLeapYear(year):
  return (year % 100 == 0) and (year % 400 != 0) or (year % 100 != 0 and year % 4 == 0)