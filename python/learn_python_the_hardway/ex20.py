from sys import argv
#passing command line arguments to variables
script, input_file = argv

#outputs file data from f
def print_all(f):
    print(f.read())

#flushes IO buffer to the beginning of f
def rewind(f):
    f.seek(0)

#outputs one line of data from f
def print_a_line(line_count,f):
    print(line_count,f.readline())

#turns input_file into a file object
current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind,kind of like a tape:")
rewind(current_file)

print("Lets print the first 3 lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
