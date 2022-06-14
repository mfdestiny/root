from sys import argv
script,filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN/ENTER.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines.")

l1 = input("line 1: ")
l2 = input("line 2: ")
l3 = input("line 3: ")

print("I'm going to write these to the file.")
line = "{}\n{}\n{}\n"

target.write(line.format(l1,l2,l3))

print("Done writing, now closing the file.")
target.close()
