def main():
    greeting = input("Greeting: ").strip()
    money = value(greeting)
    print(money)

def value(greeting):
    if ("Hello".casefold() in greeting.casefold()):
        return 0
    elif (greeting[0].casefold() == "H".casefold()):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()