"""
#1.20 MULTI MAP TO SINGLE MAP

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b) 

print(c['x']) # Outputs 1  (from a)
print(c['y']) # Outputs 2  (from b)
print(c['z']) # Outputs 3  (from a)

will check a and then b if not found hence output 3

>>> len(c)
3
>>> list(c.keys()) 
['x', 'y', 'z']
>>> list(c.values()) 
[1, 2, 3]

mutations will always affect the first mapping listed; in this example that would be a

>>> values = ChainMap()
>>> values['x'] = 1
>>> # Add a new mapping
>>> values = values.new_child() 
>>> values['x'] = 2
>>> # Add a new mapping
>>> values = values.new_child()
>>> values['x'] = 3
>>> values
ChainMap({'x': 3}, {'x': 2}, {'x': 1}) 
>>> values['x']
3
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
2
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
1
>>> values
ChainMap({'x': 1})

#instead of chainMap can use update
>>> a = {'x': 1, 'z': 3 } >>> b = {'y': 2, 'z': 4 } >>> merged = dict(b)
>>> merged.update(a)
>>> merged['x'] 1
>>> merged['y'] 2
>>> merged['z'] 3

#requires new seperate dict and if originals are changed does not reflect. Chain will reflect





------------------------------------------------------------------------------
#1.19 Transforming and Reducing Data at same time
some examples

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

vs 

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums]) == creates extra unncessary list

import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!') 
else:
    print('Sorry, no python.')


s = ('ACME', 50, 123.45) 
print(','.join(str(x) for x in s))


portfolio = [
       {'name':'GOOG', 'shares': 50},
       {'name':'YHOO', 'shares': 75},
       {'name':'AOL', 'shares': 20}
    ]

min_shares = min(s['shares'] for s in portfolio)


# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])

------------------------------------------------------------------------------

#1.18 MAPPING NAMES TO SEQUENCE ELEMENTS
ACCESSING LIST/TUPLE VIA NAME AND NOT POSITION

>>> from collections import namedtuple
>>> Subscriber = namedtuple('Subscriber', ['addr', 'joined']) 
>>> sub = Subscriber('jonesy@example.com', '2012-10-19')
>>> sub
Subscriber(addr='jonesy@example.com', joined='2012-10-19') >>> sub.addr
'jonesy@example.com'
>>> sub.joined
'2012-10-19'
>>> len(sub)
2
>>> addr, joined = sub 
>>> addr 
'jonesy@example.com' 
>>> joined 
'2012-10-19'

def compute_cost(records): 
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

VS
#does not rely on columns if data structure shifts.
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records): 
total = 0.0
for rec in records: 
    s = Stock(*rec)
    total += s.shares * s.price 
    return total


#immutable however can be replaced
>>> s = s._replace(shares=75)
>>> s
Stock(name='ACME', shares=75, price=123.45)
------
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock

def dict_to_stock(s):
    return stock_prototype._replace(**s)
------------------------------------------------------------------------------
#1.17 Extracting a subset of Dictionary

prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}
    # Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
    # Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }  #notice the {} signals dict; [] list



#1.16 Filtering sequence elements
mylist = [1, 4, -5, 10, -7, 2, 3, -1] 
>>> [n for n in mylist if n > 0]
[1, 4, 10, 2, 3]
>>> [n for n in mylist if n < 0]
[-5, -7, -1]


#when filtering involves exceptions
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val): 
    try:
        x = int(val)
        return True 
    except ValueError:
        return False

ivals = list(filter(is_int, values)) print(ivals)
# Outputs ['1', '2', '-3', '4', '5']


addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False] 
>>> list(compress(addresses, more5))
['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
    


#1.15 Group Records by Field
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter 
from itertools import groupby
 
# Sort by the desired field first

rows.sort(key=itemgetter('date')) #must sort before b/c groupby only compares consecutive items

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')): 
    print(date)
    for i in items: 
        print(' ', i)

output:

07/01/2012
    {'date': '07/01/2012', 'address': '5412 N CLARK'}
    {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
07/02/2012
    {'date': '07/02/2012', 'address': '5800 E 58TH'}
    {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
    {'date': '07/02/2012', 'address': '1060 W ADDISON'}
07/03/2012
    {'date': '07/03/2012', 'address': '2122 N CLARK'}
07/04/2012
    {'date': '07/04/2012', 'address': '5148 N CLARK'}
    {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}


#1.14 sorting objects without native comparision

class user():
    def __init__(self, user_id):
        self.user_id = user_id

sorted(users, key=lambda u: u.user_id) OR
sorted(users, key=attrgetter('user_id')) uses attribute_getter vs item from below



#1.13 sorting list of dict w/ common key
from operator import itemgetter

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid')) print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

can be used with min,max as well in place for sorted

----
w/out itemgetter (small performance hit)
rows_by_fname = sorted(rows, key=lambda r: r['fname']) 
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))



#1.12 most frequent occurences
words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]
from collections import Counter 
word_counts = Counter(words)
top_three = word_counts.most_common(3) 
print(top_three)


>>> word_counts['not'] 1 #keeps occurences
>>> word_counts['eyes'] 8

>>> morewords = ['why','are','you','not','looking','in','my','eyes'] #add more words
>>> for word in morewords:
        word_counts[word] += 1

last above same as word_counts + counter(morewords); word_coutns already a counter class


# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


#1.10 removing dups, keeping order
def dedupe(items): #hashable items
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
        seen.add(item


use:
>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
 >>> list(dedupe(a))
[1, 5, 2, 9, 10]


def dedupe(items, key=None): #unhashable such as dicts
    seen = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
            yield item 
            seen.add(val)

use:
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}] 
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x']))
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


with open(somefile,'r') as f: #deletes duplicate lines in file
    for line in dedupe(f):
...



#calculations on dicts; min,max,sort
prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys())) # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys())) # max_price is (612.78, 'AAPL')


prices_sorted = sorted(zip(prices.values(), prices.keys())) # prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# (45.23, 'ACME'), (205.55, 'IBM'),
# (612.78, 'AAPL')]

#ordered dict values
from collections import OrderedDict
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d: 
    print(key, d[key])

from collections import defaultdict
# defaultdict auto-intiliazes 'list' as value structure; could use 'set' as well
d = defaultdict(list):
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

#initalization
d = defaultdict(list) 
for key, value in pairs: 
    d[key].append(value


#max min w/ heap
import heapq

portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

for stock in cheap:
    print(stock)



#simple *args example with unpacking
records = [
         ('foo', 1, 2),
         ('bar', 'hello'),
         ('foo', 3, 4),
    ]
def do_foo(x, y): 
    print('foo', x, y)
def do_bar(s): 
    print('bar', s)
for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)
"""