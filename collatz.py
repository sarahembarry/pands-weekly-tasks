# See README.md for references > Credits and References >Program :collatz.py
# Week 4 weekly task.

#1: Defining the input ans an int.
number = int(input("Please enter a positive interger"))

#2: Printing in input number so it will be the first number that outputs.
print (int(number))
#3: Stating that the loop is to continue while the number is not equal to one.
while number!=1:
    #4: Stating that while: if the number is even it is to be divided by 2.
    if number%2 ==0:
        number=number/2
    #5: Stating that else: if the number is not even it is to be multiplied by 3 then add 1.    
    else:
        number = 3* number+1
    #6: Here i am printing the output of the loop.    
    print (int(number))    

     
           


        


 