import random

def main():
    level = get_level()
    generate_integer(level)

def get_level(): #prompt n=1,2,3 only
    while True:
        try:
            number = int(input("Level: "))
            if number < 1 or number > 3:
                raise ValueError("level != 1 2 or 3")
            return number
        except ValueError:
            pass


def generate_integer(level):
    score = 0
    if level == 1:
        r1 = 0
        r2 = 9
    if level == 2:
        r1 = 10
        r2 = 99
    if level == 3:
        r1 = 100
        r2 = 999
    for num in range(10):
        tries = 3
        x = random.randint(r1,r2)
        y = random.randint(r1,r2)
        answer = x + y
        while tries > 0:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                tries -= 1
                print("EEE")
            else:
                if guess == answer:
                    score += 1
                    break
                else:
                    tries -= 1
                    print("EEE")
        if tries == 0:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


    #generate 10 problems X + Y both > 0 with n digits
    #incorrect answer responde with EEE
    #three tries before answer is displayed
    #output score out of 10


if __name__ == "__main__":
    main()