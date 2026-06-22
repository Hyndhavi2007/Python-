from datetime import date
"""
Imports the date class from python's built -in datetime module
The date class is used to represent calendar dates (year,month,day)
"""
d1 = date(2026,6,22)
"""
creates a date object named d1
It represents June 22, 2026
The format is 
date (year, month, date)
"""
d2 = date(2026,7,15)
difference = d2 - d1
"""
subtracts d1 from d2
The result is timedelta object, which represents the duration between two dates
"""
print(difference.days, "days")
"""
Accesses the .days attribute of the timedelta object
prints the number of days followed by the word "days"
"""

