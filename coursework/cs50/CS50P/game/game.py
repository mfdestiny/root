import random

def main():
    level = set_level()
    answer = random.randint(1,level)
    guess = set_guess()
    match = compare(guess,answer)
    while match == 0:
        guess = set_guess()
        match = compare(guess,answer)
    if match == 1:
        print("Just right!")

def set_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def set_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except (ValueError,TypeError):
            pass

def compare(guess,answer):
    if guess == answer:
        return 1
    if guess < answer:
        print("Too small!")
        return 0
    if guess > answer:
        print("Too large!")
        return 0

if __name__ == "__main__":
    main()