
#See README.md for references > Credits and References >Program :es.py


# Importing the 'sys' and 'os' modules
import sys

import os



#Funtion

 # Here I am defining a function which takes in 2 arguments, the filename and the letter to be counted.
def letterFrequency(FILENAME, letter):
    #Here i am checking that the file is a txt file and raising a value error if it is not.
    if not FILENAME.endswith(".txt"):
     raise ValueError("File is not a text file.")
    #Here i am using the 'os.path.exsists' method to check if the file exsists and raising a value error if it does not.
    if not os.path.exists(FILENAME):
     raise ValueError("File does not exist.")

    # Here I am opening the file to read. As i am using 'with open' the file will close automatically.
    with open(FILENAME, 'r') as file:
 
    # Here I am reading the file and making it's contents a variable called 'text'
     text = file.read()
 
    # Here I am returning the count of the letter in the file.
    return text.count(letter)
 

#Main program

#Here i am setting the variable 'FILENAME' to be taken in as an argument from the command linee
#I'm using the format sys.argv[1] as the first argument (sys.argv[0]) will be the name of the program. Then the second argument (sys.argv[1]) will be the filename which is what i want to use in my function.
FILENAME= sys.argv[1]


 



#Here I am printing the result of the function with 'FILENAME' and the letter 'e' as the arguments.
print(letterFrequency(FILENAME, 'e'))
