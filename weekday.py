## Resoource 1: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday).
## Resource 2: https://pythontic.com/datetime/date/weekday
## Resource 3: https://ioflood.com/blog/python-get-current-date/#:~:text=To%20get%20the%20current%20date%20in%20Python%2C%20you%20can%20use,function%20from%20the%20datetime%20module.




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