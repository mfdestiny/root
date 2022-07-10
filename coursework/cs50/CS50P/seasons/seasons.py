import sys
import re
from datetime import date
import inflect


def main():
    birthday = input("Date of Birth: ")
    pattern = re.compile(r"\d\d\d\d-\d\d-\d\d")
    match = pattern.finditer(birthday)
    found = 0
    for m in match:
        found = 1
        print(convert(m.group(0)))
    if found == 0:
        sys.exit("Invalid format")


def convert(bday):
    p = inflect.engine()
    today = date.today()
    t = bday.split("-")
    if len(t) != 3:
        return None
    y = int(t[0])
    m = int(t[1])
    d = int(t[2])
    a = date(y,m,d)
    delta = today - a
    min = delta.days * 24 * 60
    words = p.number_to_words(min, andword="")
    result = words + " minutes"
    return result.capitalize()


if __name__ == "__main__":
    main()
