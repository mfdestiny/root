def main():
    d = {}
    make_list(d)

def make_list(todo_list):
    while True:
        try:
            todo = input().strip()
            if todo not in todo_list:
                todo_list[todo] = 1
            else:
                val = todo_list[todo]
                val += 1
                todo_list[todo] = val
        except EOFError:
            print_list(todo_list)
            return

def print_list(todo_list):
    sorted_list = sorted(todo_list.keys())
    for item in sorted_list:
        print(f"{todo_list[item]} {item.upper()}")
    #print alphabetically

main()