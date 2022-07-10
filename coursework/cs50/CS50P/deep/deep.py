answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?").strip()

if (answer == "42" or answer == "forty-two" or (answer.casefold() == "forty two".casefold())):
    print("Yes")
else:
    print("No")
