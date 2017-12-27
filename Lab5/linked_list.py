# an AnyList is one of
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

# None --> AnyList
# takes in nothing and returns an empty List
def empty_list():
    return None

# AnyList int value --> AnyList
# places a value at the index position of the given list
def add(anyList, index, value, count = 0):
    if index < 0 or anyList == None and index > count:
        raise IndexError()
    if index == count:
        return Pair(value, anyList)
    return Pair(anyList.first, add(anyList.rest, index, value, count+1))

# AnyList --> int
# determines the number of elements currently in the list
def length(anyList):
    if anyList == None:
        return 0
    return 1 + length(anyList.rest)

# AnyList int --> value
# returns a value at the given index in the list
def get(anyList, index, count = 0):
    if index < 0 or anyList == None and index >= count:
        raise IndexError()
    if index == count:
        return anyList.first
    return get(anyList.rest, index, count + 1)

# AnyList int value --> AnyList
# replaces the element at the given index with the given value
def set(anyList, index, value, count = 0):
    if index < 0 or anyList == None and index >= count:
        raise IndexError()
    if index == count:
        return Pair(value, anyList.rest)
    return Pair(anyList.first, set(anyList.rest, index, value, count + 1))

# AnyList int --> (value, AnyList)
# removes the element at the given index and returns the removed element and the new List
def remove(anyList, index, count = 0):
    if index < 0 or anyList == None and index >= count:
        raise IndexError()
    if index == count:
        return (anyList.first, anyList.rest)
    return (remove(anyList.rest, index, count + 1)[0], Pair(anyList.first, remove(anyList.rest, index, count + 1)[1]))