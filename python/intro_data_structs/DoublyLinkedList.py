class ListNode:
    def __init__(self,data,prev = None,link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self #sets node befores link to self
        if link is not None:
            self.link.prev = self #sets node aheads backlink to self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self,item):
        if len(self) == 0: #list is empty
            self._head = ListNode(item)
            self._tail = self._head
        else: #not empty
            newNode = ListNode(item, None, self._head) #intializing new head node
            self._head.prev = newNode #insert newNode at beginning
            self._head = newNode #give newNode the head title
        self._length += 1

    def addlast(self,item):
        if len(self) == 0: #list is empty
            self.addfirst(item)
        else:
            newNode = ListNode(item, self._tail, None) #newNode only link should be current tail
            self._tail.link = newNode #setup link to newnode from old tail
            self._tail = newNode
        self._length += 1

    def __len__(self):
        return self._length
