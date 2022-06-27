class ListStack:
    def __init__(self): #O(1)
        self._L = []

    def push(self, item): #O(1)
        self._L.append(item)

    def pop(self):#O(1)
        return self._L.pop()

    def peek(self):#O(1)
        return self._L[-1]

    def __len__(self): #O(n)
        return len(self._L)

    def isempty(self): #O(n)
        return len(self) == 0
