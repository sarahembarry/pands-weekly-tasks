
#Here i am creating the input as an interger
number = int(input("Please enter a positive interger"))

#Here i am printing in input number so it will be the first number that outputs.
print (int(number))
#Here I'm stating that i wish the loop to continue while the number is not equal to one.
while number!=1:
    #Here I am stating that if the number is even it is to be divided by 2.
    if number%2 ==0:
        number=number/2
    #Here I am stating that if the number is not even it is to be multiplied by 3 then add 1.    
    else:
        number = 3* number+1
    #Here i am printing the output of the loop.    
    print (int(number))    

     
           


        


 