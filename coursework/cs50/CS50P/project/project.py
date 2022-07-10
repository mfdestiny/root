from os.path import exists
import sys
from datetime import datetime
from journal import Journal as j
from entry import Entry as entry
import dill



def main():

    start_up()

    while True:
        try:
            cmd = parse_input(input("> ")) #unpacks two returns, last one needed only for read command
            border()
            command = cmd[0]
            if command == "write":
                enter_entry()
            elif command == "done":
                leave()
            elif command == "options":
                options()
            elif command == "size":
                journal_size()
            elif command == "last":
                last()
            elif command == "delete":
                delete()
            elif command == "read":
                read(cmd[1])
            elif command == "list":
                listing()
            else:
                print("> sorry i had trouble processing that request; type 'options' for command list")
                border()
        except ValueError:
            print("> sorry i had trouble processing that request; type 'options' for command list")
            border()
        except TypeError:
            print("> sorry i had trouble processing that request; type 'options' for command list")
            border()
        except EOFError:
            print()
            border()
            sys.exit(1)

def start_up():

    global journal

    if exists("journal.pickle"):
        journal = dill.load(open("journal.pickle", "rb"))
        verification()
    else:
        journal = password_set()

    print(f"> welcome to your digital journal")
    print("> type 'write' to write in your journal")
    print("> type 'options' for additional commands")
    print("> type 'done' to leave journal")
    border()

#COMMAND-LINE FUNCTIONS
def parse_input(text):

    cmd = text.split(" ")
    if len(cmd) > 2:
        raise ValueError
    if len(cmd) == 1:
        return cmd[0],None
    if len(cmd) == 2:
        read = cmd[0]
        num = cmd[1]
        try:
            if num:
                if read == "read" and num.isdecimal():
                    return cmd[0],int(cmd[1])
                else:
                    raise ValueError
            else:
                return cmd[0],None
        except:
            raise TypeError

#read specific journal entry
def read(num):

    if num == 0:
        raise ValueError
    page,time,title = read_journal(num)
    print(f"> entry #{num} was written on {time}")
    print(f"> title: {title}")
    print(f"> entry: {page}")
    border()

#displays number of entries
def journal_size():

    size = journal.size
    if size == 0:
        print("0 entries have been written; type 'write'' to start")
    if size == 1:
        print("1 entry is saved")
    elif size > 1:
        print(f"{size} entries have been saved")
    border()

#list of commands available from command-line
def options():

    print('''> available commands:
> - 'write' to write a journal entry
> - 'size' to see # of entries
> - 'list' to see current journal listings
> - 'read #' to read entry #[number] if it exists
> - 'last' to see your last entry
> - 'delete' to delete your last entry if it exists
> - 'done' to close journal''')
    border()

#exit and save journal state
def leave():
    print(f"> until next time {journal.username}, goodbye!")
    border()
    dill.dump(journal, file = open("journal.pickle", "wb"))
    sys.exit(0)

#get last entry and view it
def last():
    idx = journal.last_entry()
    if idx is not None:
        page,time,title = read_journal(idx)
        print(f"> your last entry was at {time}")
        print(f"> title: {title}")
        print(f"> entry: {page}")
    border()

#add entry to journal
def enter_entry():
    title = input("> enter title: ")
    thoughts = input(f"> entry #{journal.size + 1}: ")
    create_entry(title,thoughts)
    border()

#delete last journal entry
def delete():
    last = journal.delete_last()
    if last:
        page,time,title = read_entry(last)
        print(f"> the entry your deleting was written at {time}")
        print(f"> title: {title}")
        print(f"> for reference you wrote: {page}")
        border()
        print("> this page is now deleted")
    border()

def listing():
    table = journal.list()
    print("> TABLE OF CONTENTS")
    if table:
        print("")
        for i,e in enumerate(table,1):
            print(f"> {i} {e.title}")
    else:
        print("")
        print("No entries have been written")
    border()

# HELPER FUNCTIONS
def create_entry(title,input):
    e = entry(datetime.now().strftime("%d-%m-%Y %H:%M:%S"),title,input)
    journal.add_entry(e)

def read_journal(index):
    page = journal.get_entry(index)
    thoughts = read_entry(page)
    words = thoughts[0]
    time = thoughts[1]
    title = thoughts[2]
    return words,time,title

def read_entry(page):
    words,time,title = page.read()
    return words,time,title

def border():
    print("--------------------")

def password_set():
    border()
    print("> first time users need to set password")
    while True:
        try:
            password = input("> enter password: ")
            if password:
                confirmation = input("> please retype for confirmation: ")
                if confirmation == password:
                    name = input("> set username: ")
                    journal = j(name,confirmation)
                    print(f"> password enabled for {journal.username}")
                    border()
                    return journal
        except ValueError:
            pass
        except EOFError:
            print()
            border()
            sys.exit(1)

def verification():
    tries = 3
    while True:
        attempt = input("> Enter password: ")
        if attempt == journal.password:
            print(f"> {journal.username} authenticated; journal entries loaded")
            border()
            break
        else:
            tries -= 1
            if tries == 0:
                print("> verification failed; exiting")
                border()
                sys.exit(0)

if __name__ == "__main__":
    main()