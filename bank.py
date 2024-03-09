#See README.md for references > Credits and References >Program :bank.py
#Week 2 weekly task.



#Creating the inputs for the 2 integer values

amount1 =int(input('Enter amount 1 (in cent):'))
amount2 =int(input('Enter amount 2 (in cent):'))


#2 Creating the sum of these 2 values
# Then dividing by 100 to bring it from a cent format to a euro format.

sum1 =(amount1+amount2)
sum2 =(sum1/100)


#3 Printing the program response and formatting the number value to 2 decimal places.

print(f'The sum of these is € {sum2:.2f}')



 