import unittest
from array_stack import *

class TestCase(unittest.TestCase):
    def test_empty_stack(self):
        list = List([None]*10, 0, 10)
        self.assertEqual(empty_stack(), list)

    def test_push(self):
        mtlist = List([None]*10, 0, 10)
        list1 = List([1]+[None]*9, 1, 10)
        list2 = List([1, 2, 3] + [None]*7, 3, 10)
        newmt = List([1]+[None]*9, 1, 10)
        newlist1 = List([2,1]+[None]*8, 2, 10)
        newlist2 = List([4, 1, 2, 3]+[None]*6, 4, 10)

        self.assertEqual(push(mtlist, 1), newmt)
        self.assertEqual(push(list1, 2), newlist1)
        self.assertEqual(push(list2, 4), newlist2)

    def test_pop(self):
        mtlist = List([None] * 10, 0, 10)
        list1 = List([1] + [None] * 9, 1, 10)
        list2 = List([1, 2, 3] + [None] * 7, 3, 10)
        newlist1 = List([None]*10, 0, 10)
        newlist2 = List([2, 3]+[None] * 8, 2, 10)

        self.assertEqual(pop(list1), (1, newlist1))
        self.assertEqual(pop(list2), (1, newlist2))
        self.assertRaises(IndexError, pop, mtlist)

    def test_peek(self):
        mtlist = List([None] * 10, 0, 10)
        list1 = List([1] + [None] * 9, 1, 10)
        list2 = List([1, 2, 3] + [None] * 7, 3, 10)

        self.assertRaises(IndexError, peek, mtlist)
        self.assertEqual(peek(list1), 1)
        self.assertEqual(peek(list2), 1)

    def test_size(self):
        mtlist = List([None] * 10, 0, 10)
        list1 = List([1] + [None] * 9, 1, 10)
        list2 = List([1, 2, 3] + [None] * 7, 3, 10)

        self.assertEqual(size(mtlist), 0)
        self.assertEqual(size(list1), 1)
        self.assertEqual(size(list2), 3)

    def test_is_empty(self):
        mtlist = List([None] * 10, 0, 10)
        list = List([1, 2, 3] + [None] * 7, 3, 10)

        self.assertTrue(is_empty(mtlist))
        self.assertFalse(is_empty(list))

if __name__ == '__main__':
    unittest.main()