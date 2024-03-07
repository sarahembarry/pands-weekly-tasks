
##References 
##Count number of a letter in a text file:
## https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
##Raising value errors
##https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
##https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
##Filename Pattern Matching
##https://realpython.com/working-with-files-in-python/
## https://www.youtube.com/watch?v=FPSKYi5jUG8 (How to Validate the File Type of a File Using Python (Simple),Max O'Didily)
##Os path exsists method
##https://www.geeksforgeeks.org/python-os-path-exists-method/
##https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/
##https://ioflood.com/blog/python-check-if-file-exists/#:~:text=One%20of%20the%20simplest%20ways,writing%20to%20the%20file%20system.
##Command line arguments
## https://www.youtube.com/watch?v=rJCl7t3IIbA (Run Python Scripts With Command Line Arguments Using sys.argv (With Examples,Fabio Musanni - Programming Channel)
## https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
##https://discuss.codecademy.com/t/reading-files-from-command-line/597287


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
