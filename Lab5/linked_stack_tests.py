import unittest
from linked_stack import *

class TestCase(unittest.TestCase):
    def test_empty_stack(self):
        list = None
        self.assertEqual(empty_stack(), list)

    def test_push(self):
        list_mt = None
        list1 = Pair(1, None)
        list2 = Pair(1, Pair(2, Pair(3, None)))
        new_list_mt = Pair(1, None)
        new_list1 = Pair(2, Pair(1, None))
        new_list2 = Pair(4, Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(push(list_mt, 1), new_list_mt)
        self.assertEqual(push(list1, 2), new_list1)
        self.assertEqual(push(list2, 4), new_list2)

    def test_pop(self):
        mtlist = None
        list1 = Pair(1, None)
        list2 = Pair(1, Pair(2, None))
        new1 = None
        new2 = Pair(2, None)

        self.assertEqual(pop(list1), (1, new1))
        self.assertEqual(pop(list2), (1, new2))
        self.assertRaises(IndexError, pop, mtlist)

    def test_peek(self):
        mtlist = None
        list1 = Pair(1, None)
        list2 = Pair(1, Pair(2, None))

        self.assertRaises(IndexError, peek, mtlist)
        self.assertEqual(peek(list1), 1)
        self.assertEqual(peek(list2), 1)

    def test_size(self):
        mtlist = None
        list1 = Pair(1, None)
        list2 = Pair(1, Pair(2, Pair(3, Pair(4, None))))

        self.assertEqual(size(mtlist), 0)
        self.assertEqual(size(list1), 1)
        self.assertEqual(size(list2), 4)

    def test_is_empty(self):
        mtlist = None
        list = Pair(1, Pair(2, None))

        self.assertTrue(is_empty(mtlist))
        self.assertFalse(is_empty(list))

if __name__ == '__main__':
    unittest.main()