#linked_list.py

# An AnyList is one of
# - a Pair
# - None
class Pair:
    def __init__(self, first, rest):
        self.first = first # A value
        self.rest = rest # An AnyList
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))


# none -> AnyList
# returns None
def empty_list():
    return None

# AnyList int val -> AnyList
# returns a list with the value put in at the passed index
def add(anylist, index, value, s=0):
    if index < 0:
        raise IndexError
    if anylist == None:
        if index > s:
            raise IndexError
        return Pair(value, None)
    if index == s:
        return Pair(value, Pair(anylist.first, anylist.rest))
    return Pair(anylist.first, add(anylist.rest, index, value, s+1))

# AnyList -> int
# returns the number of elements currently in the list
def length(anylist, l=0):
    if anylist == None:
        return l
    return length(anylist.rest, l+1)

# AnyList int -> val
# returns the value at 'index' position of the list
def get(anylist, index, v=0):
    if index < 0:
        raise IndexError
    if anylist == None:
        if index >= v:
            raise IndexError
    if v == index:
        return anylist.first
    return get(anylist.rest, index, v+1)

# AnyList int val -> AnyList
# returns an AnyList with the value at the passed index is replaced with the passed value
def set(anylist, index, value, v=0):
    if index < 0:
        raise IndexError
    if anylist == None:
        if index >= v:
            raise IndexError
    if v == index:
        return Pair(value, anylist.rest)
    return Pair(anylist.first, set(anylist.rest, index, value, v+1))

# AnyList int -> AnyList
# returns an AnyList with the value at the given index removed
def remove(anylist, index, v=0):
    if index < 0:
        raise IndexError
    if anylist == None:
        if index >= v:
            raise IndexError
    if v == index:
        return (anylist.first, anylist.rest)
    temp = remove(anylist.rest, index, v+1)
    return (temp[0], Pair(anylist.first, temp[1]))

# an Iterator is an iterator over a linked_list
class Iterator:
    def __init__(self, lst):
        self.lst = lst # an AnyList
    def __eq__(self, other):
        return type(other) == Iterator and self.lst == other.lst
    def __repr__(self):
        return "Iterator({!r})".format(self.lst)

# AnyList -> Iterator
# raturns an Iterator made out of an AnyList
def object_iterator(anylist):
    return Iterator(anylist)

# Iterator -> Boolean
# returns True if there is another value to return from the iterated list.
def has_next(itr):
    if itr.lst == None:
        return False
    return True

# Iterator -> value
# returns the next value in the iteration sequence
def next(itr):
    if type(itr) == Pair:
        itr = object_iterator(itr)
    if has_next(itr):
        f = itr.lst.first
        itr.lst = itr.lst.rest
        return f
    raise StopIteration

# AnyList -> value
# iterates through the list, yielding each value
def yield_iterator(anylist):
    if anylist != None:
        yield anylist.first
        yield from yield_iterator(anylist.rest)
