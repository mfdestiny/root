import sys
import os
from PIL import Image,ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    allowed = [".jpg",".jpeg",".png"]
    arg = sys.argv[1]
    t1 = os.path.splitext(sys.argv[1])
    t2 = os.path.splitext(sys.argv[2])
    if t1[1] != t2[1]:
        sys.exit("Input and output have different extensions")

    if any(arg.endswith(s) for s in allowed):
        try:
            muppet = Image.open(arg)
            shirt = Image.open("shirt.png")
            m = ImageOps.fit(muppet,shirt.size)
            m.paste(shirt,shirt)
            m.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Invalid input")




if __name__ == "__main__":
    main()