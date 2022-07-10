phrase = input()

new = ""
final = ""

smile = phrase.split(":)") #check for smiles first
if smile[0] != phrase:
    while True:
        for i in range(len(smile)-1):
            new += smile[i] + '🙂'
        if len(new.split(":)")) == 1:
            new += smile[i+1]
            break

if new: #after smiles check frowns
    frown = new.split(":(")
    if frown[0] != new:
        while True:
            for i in range(len(frown)-1):
                final += frown[i] + '🙁'
            if len(new.split(":)")) == 1:
                final += frown[i+1]
                print(final)
                break
    else:
        print(new)
else:# no smiles check frowns
    frown = phrase.split(":(")
    if frown[0] != phrase:
        while True:
            for i in range(len(frown)-1):
                new += frown[i] + '🙁'
            if len(new.split(":)")) == 1:
                new += frown[i+1]
                print(new)
                break