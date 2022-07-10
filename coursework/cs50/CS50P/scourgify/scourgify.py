import sys
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        students = []
        try:
            source = open(sys.argv[1],"r")
            reader = csv.DictReader(source)
            for row in reader:
                last,first = row["name"].split(", ")
                students.append({"first":first,"last":last,"house":row["house"]})
        except IOError:
            sys.exit(f"Could not read {sys.argv[1]}")
        except csv.Error:
            sys.exit("read/write csv error")

        with open(sys.argv[2],"w") as destination:
                    writer = csv.DictWriter(destination, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in students:
                        writer.writerow(row)


    else:
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()