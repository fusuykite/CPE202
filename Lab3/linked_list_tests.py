import unittest
from linked_list import *

list1 = Pair(3, Pair("tree", Pair(1.7, None)))

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        #temp_list = add(temp_list, 0, "Hello!")
        #length(temp_list)
        #get(temp_list, 0)
       # temp_list = set(temp_list, 0, "Bye!")
       # remove(temp_list, 0)


    def test_empy_list1(self):
        self.assertEqual(empty_list(), None)

    def test_add1(self):
        self.assertEqual(add(list1, 2, "new value"), Pair(3, Pair("tree", Pair("new value", Pair(1.7, None)))))

    def test_add2(self):
        self.assertRaises(IndexError, add, list1, 5, "nothing")

    def test_add3(self):
        self.assertEqual(add(Pair("value", None), 0, 3), Pair(3, Pair("value", None)))

    def test_add4(self):
        self.assertRaises(IndexError, add, list1, -5, "nothing")

    def test_length1(self):
        self.assertEqual(length(list1), 3)

    def test_get1(self):
        self.assertEqual(get(list1, 1), "tree")

    def test_get2(self):
        self.assertRaises(IndexError, get, list1, 4)

    def test_get3(self):
        self.assertRaises(IndexError, get, list1, -4)

    def test_set1(self):
        self.assertEqual(set(list1, 2, "new value"), Pair(3, Pair("tree", Pair("new value", None))))

    def test_set2(self):
        self.assertRaises(IndexError, set, list1, 4, "nothing")

    def test_set3(self):
        self.assertRaises(IndexError, set, list1, -4, "nothing")

    def test_remove1(self):
        self.assertEqual(remove(list1, 1), ("tree", Pair(3, Pair(1.7, None))))

    def test_remove2(self):
        self.assertRaises(IndexError, remove, list1, 4)

    def test_get_new_list1(self):
        self.assertRaises(IndexError, get_new_list, list1, -4)

    def test_get_new_list2(self):
        self.assertRaises(IndexError, get_new_list, Pair("Tree", None), 4)

    def test_repr1(self):
        self.assertEqual(Pair.__repr__(Pair("first", Pair("rest", "mt"))), "Pair('first', Pair('rest', 'mt'))")

if __name__ == '__main__':
    unittest.main()





