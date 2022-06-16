print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Yell at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear gets mad.")
    elif bear == "2":
        print("The bear ignores you.")
    else:
        print("The bear eats you. Game over.")

elif door == "2":
    print("You stare in the mirror.")
    print("You have a booger in your nose.")
    print("""What do you do?\n1.Pick your nose\n2.Let it be""")
    nose = input("> ")

    if nose == "1":
        print("Your crush walks in and yells 'Disgusting!'")
    elif nose == "2":
        print("Your crush walks in and picks your nose for you.")
    else:
        print("You know you still have a booger right?")
else:
    print("You have to go through one of the doors to get out of the dark room. Try again.")
