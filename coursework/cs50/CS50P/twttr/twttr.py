phrase = input("Input: ")

new_phrase = ""
"""
for i in range(len(phrase)):
    if (phrase[i].casefold() == "a".casefold() or phrase[i].casefold() == "e".casefold() or phrase[i].casefold() == "i".casefold() or phrase[i].casefold() == "o".casefold() or phrase[i].casefold() == "u".casefold()):
        if i == 0:
            print("index is 0")
            phrase = phrase[1:]
            phrase = phrase + " "
        else:
            phrase = phrase[:i] + phrase[i+1:]
            print(phrase)
            phrase = phrase + " "

print(phrase.strip())
"""


for i in range(len(phrase)):
        if not (phrase[i].casefold() == "a".casefold() or phrase[i].casefold() == "e".casefold() or phrase[i].casefold() == "i".casefold() or phrase[i].casefold() == "o".casefold() or phrase[i].casefold() == "u".casefold()):
            new_phrase += phrase[i]

print(new_phrase)