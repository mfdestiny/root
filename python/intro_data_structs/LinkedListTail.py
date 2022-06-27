class ListNode:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

class LinkedListTail:
    def __init__(self):
        self._head = None
        self._tail = None

    def addfirst(self,item):
        if self._head is None:
            self._head = ListNode(item,self._head)
            if self._tail is None:
                self._tail = self._head

    def addlast(self,item):
        if self._head is None:
            self._head = addfirst(item)
        else:
        self._tail.link = ListNode(item) #update old tail link with new node
        self._tail = self._tail.link #set tail to point to node

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None: #if list only had one to begin with, now the list is empty
            self._tail is None
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            item = self._tail.data
            node = self._head
            while node.link is not self._tail: #find node before tail.
                node = node.link
            self._tail = node #set new tail to node before tail
            self._tail.link = None #update new tail status
            return item
