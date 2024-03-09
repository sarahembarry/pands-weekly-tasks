# See README.md for references > Credits and References >Program :accounts.py
# Week 3 weekly task.


#1: Creating the input.

AccountNo= input ('Please enter a 10 digit account number')

#2 :Slicing from digit 6 onward to get the last 4 digits.

SlicedAccountNo= AccountNo[6:]

#3 :Creating a string to go before the 4 digits.

HiddenDigets= str('XXXXXX')

#4: Concatenating both strings so i can use them in the output.

OutPutAccountNo= HiddenDigets+SlicedAccountNo

#5: Formatting and printing the output.

print (F"number is {OutPutAccountNo}")



#If i was to modify this program to deal with account number of 
#any length i would replace step 2 with this:


#(I Would get the length of the inputted account number)
#LengthOfAccountNo = len(AccountNo)

#(I would then subtract that by 4 to get the amount of digits to forward slice)
#LeadingNumbers = (LengthOfAccountNo-4)

#I would then use the above variable to slice
#SlicedAccountNo= AccountNo[(LeadingNumbers):]

