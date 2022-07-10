def main():
    get_int()

def parse_input(cmdline):
    var1 = 0
    var2 = 0

    for i in range(len(cmdline)):
        if (cmdline[i] == "/"):
                var1 = int(cmdline[:i])
                var2 = int(cmdline[i+1:])
    return var1,var2


def get_int():
    while True:
        try:
            var1,var2 = parse_input(input("Fraction: ").strip())
            answer = var1/var2
            if answer >= .9 and answer <= 1:
                print("F")
                return
            elif answer <= .1:
                output = "E"
                print("E")
                return output
            elif answer > 1:
                get_int()
            else:
                output = str(round(answer * 100)) + "%"
                print(output)
                return

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
main()