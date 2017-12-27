from linked_list import *

# Stack represents a linked list

# None --> Stack
# returns an empty stack
def empty_stack():
    return empty_list()

# Stack value --> Stack
# adds the given value to the top of the stack
def push(stack, val):
    return add(stack, 0, val)

# Stack --> (element, Stack)
# removes the top element of a stack and returns a tuple of the element and the resulting list
def pop(stack):
    return remove(stack, 0)

# Stack --> element
# returns the top element
def peek(stack):
    return get(stack, 0)

# Stack --> int
# returns the size of the stack
def size(stack):
    return length(stack)

# Stack --> boolean
# returns True if the stack is empty and False otherwise
def is_empty(stack):
    return stack is None