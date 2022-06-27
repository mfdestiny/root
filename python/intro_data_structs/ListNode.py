class ListNode:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self._head = None

    def addfirst(self, item):
        self._head = ListNode(item, self._head)

    def removefirst(self):
        item = self.head.data
        self._head = self._head.link
        return item

    def addlast(self,item):
        if self._head = None:
            addfirst(item)
        else:
            node = self._head
            while node.link is not None:
                node = node.link
            node.link = ListNode(item)

    def removelast(self):
        if self._head is None: #if there is no nodes yet.
            return None
        elif self._head.link = None: #if only the head node exists
            return self.removefirst
        else:
            node = self._head
            second_to_last = None
            while node.link is not None: #search for last node
                node = node.link
                if node.link.link is None: # save the new end n-1 to update link state
                    second_to_last = node
            item = node.data
            second_to_last.link = None
            return item
