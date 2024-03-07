
#See README.md for references > Credits and References >Program :Weekday.py



#Here I am importing the function
from datetime import date

#Here I am Setting the variable 'Today' as todays date
today = date.today()

#Here i am getting what day of the week my date is
#I am using an if statement : If today is a Monday (0), Tuesday(1),Wednesday(2),Thursday(3) or Friday(4) print "Yes, unfortunately today is a weekday"
if today.weekday() in (0, 1, 2,3,4):
  
  print("Yes, unfortunately today is a weekday")

# Else (If it's Saturday (5) or Sunday(6) print "It is the weekend, yay!")
else:

    print("It is the weekend, yay!")