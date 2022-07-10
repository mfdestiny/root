def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    size = len(s)
    found = -1 #digit not found yet
    punctuation = [" ", ".", " !"," ?"]
    if size <=6 and size >= 2:
        if s[0].isalpha() and s[1].isalpha():
            for i in range(size):
                if s[i] in punctuation:
                    return False
                number = s[i].isdecimal()
                if found == -1 and number:
                    if s[i] == "0":
                        return False #numbers can't start with zero
                    else:
                        found = 1
                else:
                    if (s[i].isalpha() and found != -1):
                        return False
        else:
            return False
    else:
        return False
    return True




main()