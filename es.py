
#See README.md for references > Credits and References >Program :es.py
# Weekly task week 7

#1: Importing the 'sys' and 'os' modules
import sys

import os



#Function

 #2: Define a function which takes in 2 arguments, the filename and the letter to be counted.
def letterFrequency(FILENAME, letter):
    #3: Check that the file is a txt file and raise a value error if it is not.
    if not FILENAME.endswith(".txt"):
     raise ValueError("File is not a text file.")
    #4: Use the 'os.path.exists' method to check if the file exists and raise a value error if it does not.
    if not os.path.exists(FILENAME):
     raise ValueError("File does not exist.")

    #5: Open the file to read. As I am using 'with open' the file will close automatically.
    with open(FILENAME, 'r') as file:
 
    #6: Read the file and set a variable 'text' to be the file contents.
     text = file.read()
 
    #7: Return the count of the letter in 'text'.
    return text.count(letter)
 

#Main program

#8: Set the variable 'FILENAME' to be taken in as an argument from the command line.
# Use format sys.argv[1] as the first argument (sys.argv[0]) will be the name of the program. Then the second argument (sys.argv[1]) will be the filename which is what we want to take as the argument. 
FILENAME= sys.argv[1]


 



#Here I am printing the result of the function with 'FILENAME' and the letter 'e' as the arguments.
print(letterFrequency(FILENAME, 'e'))
