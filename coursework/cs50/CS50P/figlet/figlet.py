import sys
from pyfiglet import Figlet as fig


def main():
    prompt()

def prompt():
    while True:
        if len(sys.argv) == 1: #random
            f = fig()
            req = input("Input: ")
            print(f.renderText(req))
            return
        elif len(sys.argv) == 3: #user attempted to chose font
            second = sys.argv[1]
            if second == "-f" or second == "--font":
                try:
                    f = fig(font=sys.argv[2])
                except:
                    sys.exit("Invalid usage")
                else:
                    req = input("Input: ")
                    print(f.renderText(req))
                    return
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

main()