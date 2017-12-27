# a front represents the index of the front of the Queue's array
# a back represents the index of the back of the Queue's array

# a Queue consists of
# - an array
# - a front
# - a back
class Queue:
    def __init__(self, array, front, back):
        self.array = array  # a python list
        self.front = front  # a value
        self.back = back  # a value

    def __eq__(self, other):
        return type(other) == Queue and self.array == other.array and self.front == other.front and self.back == other.back

# None --> Queue
# return an empty queue
def empty_queue():
    return Queue([None] * 5000, 0, 0)

# Queue value --> Queue
# adds the given value to the end of the queue
def enqueue(queue, val):
    queue.array[queue.back] = val
    queue.back += 1
    return Queue(queue.array, queue.front, queue.back)

# Queue --> (element, Queue)
# removes the element at the front of the queue and returns a tuple of the element and the resulting list
def dequeue(queue):
    if queue.array[queue.front] is None:
        raise IndexError()
    remove = queue.array[queue.front]
    queue.array[queue.front] = None
    queue.front += 1
    return (remove, Queue(queue.array, queue.front, queue.back))

# Queue --> element
# returns the element at the front queue
def peek(queue):
    if queue.array[queue.front] is None:
        raise IndexError()
    return queue.array[queue.front]

# Queue --> int
# returns the number of elements in the queue
def size(queue, count = 0):
    for i in queue.array:
        if i is not None:
            count += 1
    return count

# Queue --> boolean
# returns True if the queue is empty and False otherwise
def is_empty(queue):
    for i in queue.array:
        if i is not None:
            return False
    return True

