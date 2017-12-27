# * Section 1 (Lists)

# * dd: NumList Data Definition
# a ListItem is one of
# - a NumList
# - a StrList

# a List is one of
# - NumList
# - a StrList

#a StrList is one of:
# - "empty" or
# Pair(first, rest)

# a NumList is one of
# - "empty"
# - Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first  #a ListItem
        self.rest = rest    # a List
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))


# * 1:
# numlist -> int
# function len(list) returns the number of values in a linked list
def len(strList, l = 0):
    if strList == 'empty':
        return l
    return len(strList.rest, l+1)

# * 2:
# numlist -> int
# function sum(numList) returns the sum of values in a linked list
def sum(numList):
    if (numList == 'empty'):
        return 0
    else:
        return numList.first + sum(numList.rest)
# * 3:
# numList, int -> int
# function count_greater_than(numList, thresh) returns the number of values in a list greater than the thresh value
def count_greater_than(numList, thresh, x = 0):
    if (numList == "empty"):
        return x
    else:
        if numList.first > thresh:
            return count_greater_than(numList.rest, thresh, x + 1)
        elif numList.first <= thresh:
            return count_greater_than(numList.rest, thresh, x)

# * 4:
#numlist, int -> int
# function find(numList, val) returns the position where int is located in the numList
def find(numList, val, pos = 0):
    if numList == "empty":
        return None
    if numList.first == val:
        return pos
    else:
        return find(numList.rest, val, pos +1)
# * 5:
# numlist -> list
# function sub_one_map(numList) takes numList and returns a newList where each value is smaller by one
def sub_one_map(numList):
    if numList == "empty":
        return "empty"
    return Pair(numList.first - 1, sub_one_map(numList.rest))

# * 6:
# numlist, int -> list
# function insert(numList, val) takes a value val and inserts it in its proper location in a sorted list.
def insert(numList, val):
    if numList == "empty":
        return numList
    if numList.first < val:
        return Pair(numList.first, insert(numList.rest, val))
    elif numList.first >= val:
        return Pair(val, Pair(numList.first, numList.rest))

# * Tests : the test case class for the list functions

import unittest
class TestCase(unittest.TestCase):

    def test_len(self):
        self.assertEqual(len("empty"), 0)
        self.assertEqual(len(Pair("cat", Pair("Dog", Pair("Cool", "empty")))), 3)
        self.assertEqual(len(Pair(4, 'empty')), 1)
        self.assertEqual(len(Pair(-5, Pair(-8, 'empty'))), 2)

    def test_sum(self):
        self.assertEqual(sum(Pair(1, Pair(3, Pair(8, Pair(0, "empty"))))), 12)
        self.assertEqual(sum("empty"), 0)
        self.assertEqual(sum(Pair(1, Pair(-101, "empty"))), -100)

    def test_count_greater_than(self):
        self.assertEqual(count_greater_than(Pair(1, Pair(3, Pair(8, Pair(0, "empty")))), 2), 2)
        self.assertEqual(count_greater_than(Pair(3, Pair(5, Pair(2, Pair(0, Pair(2, Pair(-5, "empty")))))), 1), 4)
        self.assertEqual(count_greater_than("empty", 3), 0)

    def test_find(self):
        self.assertEqual(find(Pair(1, Pair(3, Pair(8, Pair(0, "empty")))), 8), 2)
        self.assertEqual(find(Pair(3, Pair(5, Pair(2, Pair(0, Pair(2, Pair(-5, "empty")))))), 4), None)
        self.assertEqual(find('empty', 2), None)

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(Pair(2, "empty")), Pair(1, "empty"))
        self.assertEqual(sub_one_map(Pair(3, Pair(5, "empty"))), Pair(2, Pair(4, "empty")))
        self.assertEqual(sub_one_map("empty"), "empty")

    def test_insert(self):
        self.assertEqual(insert(Pair(3, Pair(5, Pair(9, "empty"))), 6), Pair(3, Pair(5, Pair(6, Pair(9, "empty")))))
        self.assertEqual(insert(Pair(0, Pair(2, Pair(7, 'empty'))), -1), Pair(-1, Pair(0, Pair(2, Pair(7, "empty")))))
        self.assertEqual(insert(Pair(2, "empty"), 2), Pair(2, Pair(2, "empty")))


if __name__ == '__main__':
    unittest.main()






