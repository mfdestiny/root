class ListNode:
    def __init__(self,data,prev = None,link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class RefactoredDoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length


    def _addbetween(self,item,before,after):
        newNode = ListNode(item,before,after)
        if after is self._head: #after is linking to self._head so must be new head of list
            self._head = newNode
        if before is self._tail: #before is prev, node will be new tail
            self._tail = newNode
        self._length += 1

    def addfirst(item):
        self._addbetween(item, None, self._head)

    def addlast(item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after #first stitch
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before #second stitch

        self._length -= 1
        return node.data

    def removefirst():
        self._remove(self._head)

    def removelast():
        self._remove(self._tail)
