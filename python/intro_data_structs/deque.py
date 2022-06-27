class ListDeque: #double-ended queue. precursor to LinkedLists
    def __init__(self):
        self._L = []

    def addfirst(self,item):
        self._L.insert(0,item)

    def addlast(self, item):
        self._L.append(item)

    def removefirst(self):
        return self._L.pop(0)

    def removelast(self):
        return self._L.pop()

    def __len__(self):
        return len(self._L)

#inserting and popping at front is O(n). There is no way to change beginning of List
#without shifting all items after.
