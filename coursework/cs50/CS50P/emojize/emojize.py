import emoji

sign = input("Input: ")

for i in range(len(sign)):
    if sign[0] == ":" and sign[-1] == ":": #basecase: one emoji
        if sign[-1] == ":":
                print("Output: " + emoji.emojize(sign))
                break
    elif sign[0] != ":" and sign[-1] == ":":#case 1: phrase + emoji
        if sign[i] == ":":
            emoj = sign[i:]
            phrase = sign[:i]
            print("Output: " + phrase + emoji.emojize(emoj))
            break
    elif sign[0] == ":" and sign[-1] != ":":#case 2: emoji + phrase
        if i == 0:
            continue
        if sign[i] == ":":
            emoj = sign[:i+1]
            phrase = sign[i+1:]
            print("Output: " + emoji.emojize(emoj) + phrase)
            break
    elif sign[0] != ":" and sign[-1] != ":":#case 3: emoji in middle of sentence
        first = sign.find(":")
        second = sign.find(":",first+1)
        print("Output: " + sign[:first] + emoji.emojize(sign[first:second+1] + sign[second+1:]))
        break


