people = 30
cars = 40
trucks = 15

if cars > people:
    print("vroom")
elif cars < people:
    print("need more cars")
else:
    print("not sure")

if trucks > cars:
    print("need more cars")
elif trucks < cars:
    print("need more trucks")
else:
    print("equilibrium")

if people > trucks:
    print("take the trucks")
else:
    print("lets order tacobell")
