def main():
    phrase = input("Input: ")
    mod = short(phrase)

def shorten(word):
    new_phrase = ""

    for i in range(len(word)):
            if not (word[i].casefold() == "a" or word[i].casefold() == "e" or word[i].casefold() == "i" or word[i].casefold() == "o" or word[i].casefold() == "u" or word[i].isdecimal() or word[i] == "." or word[i] == "!" or word[i] == "?"):
                new_phrase += word[i]

    return new_phrase

if __name__ == "__main__":
    main()