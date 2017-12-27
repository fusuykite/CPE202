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
