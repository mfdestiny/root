import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith(".csv"):
        try:
            f1 = open(sys.argv[1],"r")
            r1 = csv.reader(f1)
            print(tabulate(r1,headers="firstrow",tablefmt="grid"))
        except IOError:
            sys.exit("File does not exist")

    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()