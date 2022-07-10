def main():
    while True:
        try:
            fuel = input("Fraction: ").strip()
            answer = convert(fuel)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        except UnboundLocalError:
            continue
        else:
            break

    display = gauge(answer)
    print(display)

def convert(fraction):
    try:
        for i in range(len(fraction)):
            if (fraction[i] == "/"):
                x = int(fraction[:i])
                y = int(fraction[i+1:])

        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if x > y:
            raise ValueError("X > Y")
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

    answer = round(x/y * 100)
    return answer

def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        return "F"
    elif percentage >= 0 and percentage <= 1:
        return "E"
    else:
        conversion = str(percentage) + "%"
        return conversion

if __name__ == "__main__":
    main()