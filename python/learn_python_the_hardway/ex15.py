#imports argv from sys module to accept command line arguments
from sys import argv
#assigns variables to these command line arguments
script, filename = argv

#opens file object
txt = open(filename)
#prints filename
print(f"Here's your file {filename}:")
#reads text from file and outputs
print(txt.read())
#asks user for a filename
print("Type the filename again.")
file_again = input("> ")
#opens new file object
txt_again = open(file_again)
#outputs text file
print(txt_again.read())

txt.close()
txt_again.close()
