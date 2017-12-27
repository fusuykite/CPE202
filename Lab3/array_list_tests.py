import unittest
from array_list import *




class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty_list(self):
        self.assertEqual(empty_list(), List([], 0))

    def test_add1(self):
        self.assertEqual(add(List([1, 3, 6, 14], 4), 2, 10), List([1, 3, 10, 6, 14], 5))

    def test_add2(self):
        self.assertRaises(IndexError, add, List([1, 3, 6, 14], 4), 5, 0)

    def test_length1(self):
        self.assertEqual(length(List([1, 3, 6, 14], 4)), 4)

    def test_length2(self):
        self.assertEqual(length(List([], 0)), 0)

    def test_get1(self):
        self.assertEqual(get(List([1, 3, 6, 14], 4), 2), 6)

    def test_get2(self):
        self.assertRaises(IndexError, get, List([1, 3, 6, 14], 4), -4)

    def test_set1(self):
        self.assertEqual(set(List([1, 3, 6, 14], 4), 1, 2), List([1, 2, 6, 14], 4))

    def test_set2(self):
        self.assertRaises(IndexError, set, List([1, 3, 6, 14], 4), 4, 7)

    def test_remove1(self):
        self.assertEqual(remove(List([1, 3, 6, 14], 4), 2), (6 ,List([1, 3, 14], 3)))

    def test_remove2(self):
        self.assertRaises(IndexError, remove, List([1, 3, 6, 14], 4), 5)

    def test_repr1(self):
        self.assertEqual(List.__repr__(List([1, 3, 6, 14], 4)), "List([1, 3, 6, 14], 4)")




if __name__ == '__main__':
    unittest.main()
