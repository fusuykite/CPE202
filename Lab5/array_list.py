# an array is a built in Python llist
# a size is an int that represents the current number of elements inside an array
# a capacity is an int that represents the maximum number of elements that can be stored inside an array

# a List contains
# - an array
# - a size
# - a capacity
class List:
    def __init__(self, array, size, capacity):
        self.array = array  # an array
        self.size = size  # an int
        self.capacity = capacity  # an int
    def __eq__(self, other):
        return type(other) == List and self.array == other.array and self.size == other.size and self.capacity == other.capacity
    def __repr__(self):
        return "List(%r, %r, %r)" %(self.array, self.size, self.capacity)

# None --> List
# takes in nothing and returns an empty List
def empty_list():
    return List([None]*10, 0, 10)

# List --> int
# takes in a list and returns the number of elements inside the list
def length(list):
    return list.size

#  List int any -> List
#  adds an item to an exisiting list at a certain index
def add(list1, index, any):
    if index > list1.size or index < 0:
        raise IndexError()
    if list1.size >= list1.capacity:
        newlist = List([None] * (2 * list1.capacity), list1.size, list1.capacity * 2)
        for i in range(list1.capacity + 1):
            if i < index:
                newlist.array[i] = list1.array[i]
            elif i == index:
                newlist.array[i] = any
                newlist.size += 1
                while newlist.size >= newlist.capacity:
                     newlist.capacity = newlist.capacity * 10
                     newlist.array = newlist.array + [None] * 100
            elif i > index:
                newlist.size = list1.size + 1
                newlist.array[i] = list1.array[i - 1]
        newlist.size = list1.size + 1
        return newlist
    else:
        current_index = index
        to_add = any
        while list1.array[current_index] != None:
            temp = list1.array[current_index]
            list1.array[current_index] = to_add
            to_add = temp
            current_index += 1
        list1.array[current_index] = to_add
        list1.size += 1
        return list1

# List int --> value
# determines which element is at the given index
def get(list, index):
    if index < 0  or index >= list.size:
        raise IndexError()
    return list.array[index]

# List int value --> List
# replaces the element at the given index with the given value
def set(list, index, value):
    if index < 0 or (list.array == [None] and index >= list.size):
        raise IndexError()
    newlist = [None] * (list.capacity)
    for i in range(list.size):
        newlist[i] = list.array[i]
    newlist[index] = value
    return List(newlist, list.size, list.capacity)

# List int --> (value, List)
# removes the element at the given index and returns the removed element and the new List
def remove(list, index):
    if index < 0 or index >= list.size:
        raise IndexError()

    newlist = [None] * (list.capacity)

    for i in range(list.size-1):
        if i == index:
            newlist[i] = list.array[i+1]
        elif i < index:
            newlist[i] = list.array[i]
        else:
            newlist[i] = list.array[i+1]
    return (list.array[index], List(newlist, list.size - 1, list.capacity))
