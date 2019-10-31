# 1. Determine whether it is a leap year
year = int(input('Please enter a year:'))
if (year % 4 == 0 and year % 100 != 0) | (year % 400 == 0):
    print('The year %s is a leap year.' % year)
else:
    print('The year %s is not a leap year.' % year)