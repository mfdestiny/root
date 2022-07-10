import inflect
import sys

def main():
    word_list = parse_arg()
    transform(word_list)

def transform(words):
    phrase = "Adieu, adieu, to "
    p = inflect.engine()
    t = p.join(words)
    print(phrase + t)

def parse_arg():
    words = list()
    while True:
        try:
            arg = input("Name: ").strip()
            words.append(arg)
        except EOFError:
            print()
            return words

main()