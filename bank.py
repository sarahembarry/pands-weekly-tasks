## Weekly task week 2 
## Authored by Sarah Barry 

## Here I am creating the prompts for the 2 integer values

amount1 =int(input('Enter amount 1 (in cent):'))
amount2 =int(input('Enter amount 2 (in cent):'))


## Here I am creating the sum of these 2 values
## Then dividing by 100 to bring it to a euro format

sum1 =(amount1+amount2)
sum2 =(sum1/100)


## Here I am creating the text response 
## and formatting the number value to 2 decimal places
## I got this information here : (https://www.w3schools.com/python/python_string_formatting.asp)



print(f'The sum of these is € {sum2:.2f}')



 