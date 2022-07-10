cmdline = input("Expression: ").strip()

first = 1
exp = ""


for i in range(len(cmdline)):
    if (cmdline[i].isspace()):
        if first:
            var1 = float(cmdline[:i])
            exp = cmdline[i+1:i+2]
            first = 0
        else:
            var2 = float(cmdline[i:])


if (exp == '+'):
    print(var1 + var2)

if (exp == '/'):
    print(var1 / var2)

if (exp == "*"):
    print(var1 * var2)

if (exp == "-"):
    print(var1 - var2)