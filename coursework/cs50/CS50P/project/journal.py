class Journal:
    def __init__(self,name,password):
        self.entries = []
        self._size = 0
        self.password = password
        self.username = name

    @property
    def size(self):
        return self._size

    def add_entry(self,entry):
        self.entries.append(entry)
        self._size += 1

    def last_entry(self):
        index = len(self.entries)
        if index == 0:
            print("your journal has no entries! type 'entry' to write one")
            return None
        return index

    def delete_last(self):
        if self.size > 0:
            last = self.entries[-1]
            self.entries = self.entries[:-1]
            self._size -= 1
            return last
        if self.size == 0:
            print("your journal is empty already!")

    def get_entry(self,number):
        if number < 1:
            raise ValueError
        index = number - 1
        if index < self.size:
            entry = self.entries[index]
            return entry
        else:
            raise ValueError

    def list(self):
        return self.entries
