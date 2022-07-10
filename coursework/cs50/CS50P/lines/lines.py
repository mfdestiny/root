import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    count = 0
    file = sys.argv[1].casefold()
    if file.endswith(".py"):
        try:
            with open(file,"r") as target:
                for line in target:
                    if line.startswith("#"):
                        continue
                    if line.strip() == "" or line.lstrip().startswith("#"):
                        continue
                    count += 1
            print(count)
        except IOError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file")


if __name__ == "__main__":
    main()
