def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20,30)

print("OR we can use variables from our script.")

cheese = 25
boxes = 35

cheese_and_crackers(cheese,boxes)

print("We can even do math inside too:")
cheese_and_crackers(10+5,5+5)

print("And we can combine the two variables and math:")
cheese_and_crackers(cheese-10,boxes-30)
