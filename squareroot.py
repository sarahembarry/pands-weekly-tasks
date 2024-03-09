# See README.md for references > Credits and References >Program :squareroot.py
# Weekly task week 6



#1: Define a funtion using Newton's method to find the square root of a number:
def sqrt(number):
    #2: Half the 'number' that has been passed into the function to get an approximation of the square root.
    approx = 0.5 * number
    #3: Use Newton's method for the square root.
    improved = 0.5 * (approx + number / approx)
    #4: Use a while loop : if 'improved' is not equal to 'approx' update the value for 'approx' to the value for 'improved'.
    #The while loop re-runs and Newton's method is executed until 'improved' is equal to or very close to 'aprox'.
    #Then loop terminates.
    while improved != approx:
        approx = improved
        improved = 0.5 * (approx + number / approx)
    return approx



# Main Program

#5: Create an input for a positive number.This can be a float. The variable 'number' will be the parameter/argument for the function.
number = float(input("please enter a positive number:"))

#6: Create a while loop. If the number is less than or equal to 0 it will keep prompting for a positive number.
while number <= 0:

    print(f"That was not a positive number")
    number= float(input("Please enter a positive number:"))



#7: Once a value for 'number' has been entered it will be used as the argument for the function.
#The output of this function will the the variable "result"    
result = (sqrt(number))

#8: Print out the result of the function.
print ((f"The square root of {number} is {result}"))