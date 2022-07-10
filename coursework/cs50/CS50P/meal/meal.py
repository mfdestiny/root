def main():
    time = input("What time is it? ")
    food = convert(time)
    if food >= 7 and food <= 8:
        print("breakfast time")
    if food >= 12 and food <= 13:
        print("lunch time")
    if food >=18 and food <= 19:
        print("dinner time")

def convert(time):
    converted = -1
    if len(time) == 4: #morning
        hour = int(time[0])
        minutes = int(time[2:])
        converted = hour + minutes/60
    if len(time) == 5: #noon and beyond
        hour = int(time[:2])
        minutes = int(time[3:])
        converted = hour + minutes/60
    return converted


if __name__ == "__main__":
    main()