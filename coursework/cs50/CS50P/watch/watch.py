import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = re.compile(r"youtube.com/embed/")
    encode = ""
    encoding = None
    m = pattern.finditer(s)
    for match in m:
        encode = s[match.end():]

    if encode:
        for i in range(len(encode)):
            if encode[i] == '"':
                encoding = "https://youtu.be/" + encode[:i]

    return encoding



if __name__ == "__main__":
    main()
