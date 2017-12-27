import sys
sys.setrecursionlimit(6000)

# a Priority Queue has
# - a comes_before function
# - a linked list
class PQueue:
    def __init__(self, func, list):
        self.func = func  # comes_before function
        self.list = list  # a linked list
    def __eq__(self, other):
        return type(other) == PQueue and self.func == other.func and self.list == other.list
    def __repr__(self):
        return ('PQueue: %r' % (self.list))

# a linked list is one of
# - None
# - a Pair
class Pair:
    def __init__(self, first, rest):
        self.first = first  # any value
        self.rest = rest  # a Pair
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.rest)

# val val --> boolean
# determines if the first argument should come before the second in the priority ordering
def comes_before(a, b):
    return a < b

# func --> PriorityQueue
# returns an empty Priority Queue
def empty_pqueue(func):
    return PQueue(func, None)

# PriorityQueue val --> PriorityQueue
# adds the given value to the queue in the appropriate position
def enqueue(pqueue, val):
    return PQueue(pqueue.func, enqueue_helper(pqueue.list, pqueue.func, val))

# LinkedList func val --> LinkedList
# returns a linked list with the value inserted in the appropriate position
def enqueue_helper(list, func, val):
    if list is None:
        return Pair(val, None)
    if func(val, list.first) is True:
        return Pair(val, list)
    return Pair(list.first, enqueue_helper(list.rest, func, val))

# PriorityQueue --> (val, PriorityQueue)
# removes the element at the beginning of the Priority Queue
def dequeue(pqueue):
    if pqueue.list is None:
        raise IndexError()
    return (pqueue.list.first, PQueue(pqueue.func, pqueue.list.rest))

# PriorityQueue --> element
# returns the element at the beginning of the queue
def peek(pqueue):
    if pqueue.list is None:
        raise IndexError
    return pqueue.list.first

# PriorityQueue --> int
# returns the number of elements in the Priority Queue
def size(pqueue):
    return size_helper(pqueue.list)

# Linked List --> int
# returns the number of elements in a linked list
def size_helper(list, count = 0):
    if list is None:
        return count
    count += 1
    return size_helper(list.rest, count)

# PriorityQueue --> boolean
# returns True if the queue is empty, False otherwise
def is_empty(pqueue):
    return pqueue.list is None