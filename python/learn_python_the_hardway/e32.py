the_count = [1,2,3,4] #number array
fruits = ['apples','oranges','strawberries','watermelon'] #string array
change = [1,'pennies',2,'dimes',3,'quarters'] #number and string array

for number in the_count:
    print(f"This is the number {number}.")

for fruit in fruits:
    print(f"This is the fruit {fruit}.")


#printing a mixed list that we don't know the contents
for i in change:
    print(f"I have {i}")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i) #adds i to the empty elements arary


for i in elements:
    print(f"Element was {i}.")
