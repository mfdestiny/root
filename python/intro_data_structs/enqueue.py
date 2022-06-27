class ListQueueSimple: #similar to stack however FIFO instead of LIFO
    def __init__(self):
        self._queue = []

    def enqueue(self,item):
        self._queue.append(item)

    def dequeue(self):
        return self._queue.pop(0)

    def peek(self):
        return self._queue[0]

    def __len__(self):
        return len(self._queue)

    def isempty(self):
        return len(self) == 0

#this implementation is bad b/c popping from beginning
#is O(n)

class ListIndexQueue:
    def __init__(self):
        self._head = 0
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def peek(self):
        return self._queue[self._head]

    def dequeue(self):
        item = self.peek()
        self._head += 1
        return item

    def __len__(self):
        return len(self._queue) - self._head

    def isempty(self):
        return len(self) == 0

#this one is better yet it never removes old items, we should
#clean up the unneeded items at some point

class ListIndexUpdate(ListIndexQueue):
    def dequeue(self):
        item = self._queue[self._head]
        self._head += 1
        if self._head > len(self._queue)//2: # if we 'pop' over half the items lets reset the queue
            self._queue = self._queue[self._head:] #splices at current index to end and overwrites old queue
            self._head = 0 #reset index
        return item

#this overwriting defeats the purpose of the index only on rare occassions since we don't overwrite
#everytime, only when certain conditions are met. pop and append are implemented in a similar fashion
#and on average take constant time however there will be times when it becomes linear as memory needs to be
#allocated if the current allocation is not enough
