class Entry:
    def __init__(self,date,title,entry):
        self.date = date
        self.title = title
        self.entry = entry

    def read(self):
        thoughts = self.entry
        time = self.date
        title = self.title
        return thoughts,time,title