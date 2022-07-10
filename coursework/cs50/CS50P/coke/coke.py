coins = input("Amount Due: 50\nInsert Coin: ")

token = int(coins)
owed = 50


while (owed > 0):
    if (token != 25 and token != 10 and token != 5):
        token = int(input(f"Amount Due: {owed}\nInsert Coin: "))
    else:
        owed = owed - token
        if owed <= 0:
            owe = abs(owed)
            print(f"Change Owed: {owe}")
        else:
            token = int(input(f"Amount Due: {owed}\nInsert Coin: "))
