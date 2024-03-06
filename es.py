
##References 
##Count number of a letter in a text file:
## https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
##Raising value errors
##https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
##Filename Pattern Matching
##https://realpython.com/working-with-files-in-python/
##Os path exsists method
##https://www.geeksforgeeks.org/python-os-path-exists-method/
##https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/


import sys

import os





 
# explicit function to return the letter count
def letterFrequency(FILENAME, letter):
    if not FILENAME.endswith(".txt"):
     raise ValueError("File is not a text file.")
    
    if not os.path.exists(FILENAME):
     raise FileNotFoundError("File does not exist.")

    # open file in read mode
    with open(FILENAME, 'r') as file:
 
    # store content of the file in a variable
     text = file.read()
 
    # using count()
    return text.count(letter)
 

FILENAME = "moby-dick.txt"
 
# call the function and display the letter count
print(letterFrequency(FILENAME, 'e'))