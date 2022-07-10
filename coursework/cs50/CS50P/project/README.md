# command line journal
#### video demo:  https://youtu.be/Gzv_u7kWwvA
#### description: simple command line journal to save paper and journal ones thoughts and save paper along the way. I seem to always write things down and misplace them or have ideas and no paper/pen. Yes there is freeware out there which already has everything however free comes at a price in terms of privacy. here is something you can control on your own terms and you don't need to install anything other than a few dependencies. The journal is persistant so "closing" the journal or exiting the program still allows you to retrieve your entries from before.

**warning:** the mechanism to keep the journal persistant has a threshold of 2GB; if you
need more space this might not be for you. also, the password mechanism is quite basic so if your wanting something more secure this might not be for you [yet]

### usage:
typing 'entry' begins the journaling proces
typing 'options' displays additional features of your journal
typing 'done' closes journal

### features include:
-password protected
-reading a specific journal entry
-reading the last journal entry written
-deleting the last journal
-showing the size of your journal
-table of contents

### files included:
project.py : the meat of the project, provides the UI via command line
journal.py : Journal class object with some specific methods to manipulate journal entries
entry.py: entry class provides the "pages" of the journal
test_project.py : some tests to verify basic functionality
journal.pickle: when your open your journal the first time


### todo:
journal persistance [completed]
add table of contents (TOC) 'list' function [completed]
add title to entry to display in TOC [completed]
deleting specific journal entries
edit journal entries? maybe save them as a file name to be appended etc
password protection[completed]
maybe segment functionality i.e. todo/reminder list vs. journal
set alerts for reminders via some mechanism? idk cron etc
an add-on to the editing entries; be nice to pop open a text editor instead of just writing directly into the command line
saving journal state even when the program is not closed correctly i.e. 'done'
