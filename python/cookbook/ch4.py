#4.16 replacing infinite while loops with iterator

CHUNKSIZE = 8192
def reader(s): 
	while True:
		data = s.recv(CHUNKSIZE) 
		if data == b'':
			break
		process_data(data)

def reader(s):
	for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
		process_data(data)


#4.14 flatten nested sequence

from collections import Iterable
	def flatten(items, ignore_types=(str, bytes)): 
		for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types): 
			yield from flatten(x)
		else:
			yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flatten(items): 
	print(x)

#4.12 iterating on items in seperate containers
>>> from itertools import chain 
>>> a = [1, 2, 3, 4]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
... 	print(x) 
...
1
2
3
4
x
y
z


# Various working sets of items
    active_items = set()
    inactive_items = set()
    # Iterate over all items
for item in chain(active_items, inactive_items):
	# Process item


#4.11 multi sequence simulatenously
>>> zip(a, b)
<zip object at 0x1007001b8> 
>>> list(zip(a, b))
[(1, 10), (2, 11), (3, 12)]

#4.6 generator function with extra states
from collections import deque
class linehistory:
	def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

	def __iter__(self):
		for lineno, line in enumerate(self.lines,1):
			self.history.append((lineno, line)) 
			yield line

	def clear(self): 
		self.history.clear()

with open('somefile.txt') as f: 
	lines = linehistory(f)
	for line in lines:
		if 'python' in line:
			for lineno, hline in lines.history:
				print('{}:{}'.format(lineno, hline), end='')


>>> f = open('somefile.txt')
>>> lines = linehistory(f)
>>> next(lines)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
    TypeError: 'linehistory' object is not an iterator

>>> # Call iter() first, then start iterating >>> it = iter(lines)
>>> next(it)
'hello world\n'
>>> next(it)
'this is a test\n' 



#4.5 custom reverse
class Countdown:
def __init__(self, start):
    self.start = start
# Forward iterator
def __iter__(self): 
	n = self.start
while n > 0: 
	yield n
	n -= 1
# Reverse iterator
def __reversed__(self): 
	n=1
	while n <= self.start: 
		yield n
		n += 1

#4.4 implementing iterator protocol
class Node:
def __init__(self, value):
    self._value = value
    self._children = []

def __repr__(self):
	return 'Node({!r})'.format(self._value)

def add_child(self, node): 
	self._children.append(node)

def __iter__(self):
	return iter(self._children)

def depth_first(self): 
	yield self
	for c in self:
		yield from c.depth_first()


if __name__ == '__main__': root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
	for ch in root.depth_first(): 
		print(ch)

-----------------

def depth_first(self):
	return DepthFirstIterator(self)

def __init__(self, start_node):
    self._node = start_node
    self._children_iter = None
    self._child_iter = None

def __iter__(self): 
	return self
def __next__(self):
# Return myself if just started; create an iterator for children 
	if self._children_iter is None:
	self._children_iter = iter(self._node) 
		return self._node
# If processing a child, return its next item
	elif self._child_iter: 
		try:
	    	nextchild = next(self._child_iter)
			return nextchild 
		except StopIteration:
			self._child_iter = None 
			return next(self)
            # Advance to the next child and start its iteration
	else:
		self._child_iter = next(self._children_iter).depth_first() 
		return next(self)





  # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

#4.3 custom generator iterator

def frange(start, stop, increment): 
	x = start
	while x < stop: 
		yield x
		x += increment


#4.2 turning an interal object attribute iterable i.e. list tupe etc

class Node:
	def __init__(self, value):
        self._value = value
        self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self, node): 
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

# Example
if __name__ == '__main__': 
	root = Node(0)
	child1 = Node(1) 
	child2 = Node(2) 
	root.add_child(child1) 
	root.add_child(child2) 
	for ch in root:
		print(ch)
# Outputs Node(1), Node(2)


#4.1 more precise iteration than a for loop can provide

with open('/etc/passwd') as f: try:
	while True:
		line = next(f)
		print(line, end='') 
	except StopIteration:
		pass


>>> items = [1, 2, 3] 
>>> # Get the iterator 
>>> it = iter(items) # Invokes items.__iter__()
>>> # Run the iterator 
>>> next(it) # Invokes it.__next__()
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
StopIteration
>>>