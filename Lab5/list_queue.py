from linked_list import *

# a Queue consists of 2 AnyLists
class Queue:
    def __init__(self, early = None, late = None):
        self.early = early  # a List
        self.late = late  # a List
    def __eq__(self, other):
        return type(other) == Queue and self.early == other.early and self.late == other.late

# None --> Queue
# returns an empty Queue
def empty_queue():
    return Queue(empty_list(), empty_list())

# Queue value --> Queue
# adds a given value to the queue
def enqueue(queue, val):
    return Queue(queue.early, add(queue.late, 0, val))

# Queue --> (value, Queue)
# removes an element at the beginning of the queue and returns a tuple containing the element and the resulting Queue
def dequeue(queue):
    if queue.early is None:
        if queue.late is None:
            raise IndexError()
        new_early = reverse(queue.late)
        return (new_early.first, Queue(new_early.rest, queue.late))
    return (queue.early.first, Queue(queue.early.rest, queue.late))

# List --> List
# reverses the list
def reverse(list, new_list = None):
    if list is None:
        return new_list
    new_list = Pair(list.first, new_list)
    return reverse(list.rest, new_list)

# Queue --> element
# returns the element at the beginning of the queue
def peek(queue):
    if queue.early is None:
        if queue.late is None:
            raise IndexError()
        new_early = reverse(queue.late)
        return new_early.first
    return queue.early.first

# Queue --> int
# returns the number of elements in the queue
def size(queue):
    len1 = length(queue.early)
    len2 = length(queue.late)
    return len1 + len2

# Queue --> boolean
# returns True if the queue is empty, False otherwise
def is_empty(queue):
    return queue == Queue(empty_list(), empty_list())

