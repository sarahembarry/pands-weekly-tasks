## Weekly task week 2 
## Authored by Sarah Barry 

## Here I am creating the prompts for the 2 integer values

amount1 =int(input('Enter amount 1 (in cent):'))
amount2 =int(input('Enter amount 2 (in cent):'))


## Here I am creating the sum of these 2 values
sum =(amount1+amount2)

## Here I a, creating the text response 
##and formatting the number value to 2 decimal places
txt = 'The sum of these is € {:.2f}'

## Here i'm using the above to format what i want printed as the reposnse 
## and dividing the sum (cent value) by 100 to bring it to euros.
print(txt.format(sum/100))
      

 