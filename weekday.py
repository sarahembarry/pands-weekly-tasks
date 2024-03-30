
# See README.md for references > Credits and References >Program :Weekday.py
# Week 5 weekly task.



#1: Importing the date module from the datetime library.

from datetime import date

#2: Setting the variable 'Today' as today's date.

today = date.today()

#3:Get what day of the week my date is.
#Using an if statement : If today is a Monday (0), Tuesday(1),Wednesday(2),Thursday(3) or Friday(4) print "Yes, unfortunately today is a weekday"
if today.weekday() in (0, 1, 2,3,4):
  
  print("Yes, unfortunately today is a weekday")

#4: Else (If it's Saturday (5) or Sunday(6) print "It is the weekend, yay!")
else:

    print("It is the weekend, yay!")