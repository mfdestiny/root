menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price = take_order(0)


def take_order(total):
    try:
        while True:
            order = input("Item: ")
            price = menu[order.title()]
            total += price
            print(f"Total: ${total:.2f}")
    except KeyError:
        take_order(total)
    except EOFError:
        print()
        return

main()

