greeting = input("Greeting: ").strip()

if ("Hello".casefold() in greeting.casefold()):
    print("$0")
elif (greeting[0].casefold() == "H".casefold()):
    print("$20")
else:
    print("$100")