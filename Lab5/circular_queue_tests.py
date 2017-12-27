import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):


    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        test_queue = dequeue(test_queue)
        size(test_queue[1])
        is_empty(test_queue[1])

    def test_empty_queue(self):
        empty = [None] * 5000
        self.assertEqual(empty_queue(), Queue(empty, 0, 0))

    def test_enqueue(self):
        empty = Queue([None] * 5000, 0, 0)
        list1 = Queue([1] + [None] * 4999, 0, 1)
        list2 = Queue([1, 2, 3] + [None] * 4997, 0, 3)

        newempty = [1] + [None] * 4999
        newlist1 = [1, 2] + [None] * 4998
        newlist2 = [1, 2, 3, 4] + [None] * 4996

        self.assertEqual(enqueue(empty, 1), Queue(newempty, 0, 1))
        self.assertEqual(enqueue(list1, 2), Queue(newlist1, 0, 2))
        self.assertEqual(enqueue(list2, 4), Queue(newlist2, 0, 4))

    def test_dequeue(self):
        empty = Queue([None] * 5000, 0, 0)
        list1 = Queue([1] + [None] * 4999, 0, 1)
        list2 = Queue([1, 2, 3] + [None] * 4997, 0, 3)

        newlist1 = Queue([None] * 5000, 1, 1)
        newlist2 = Queue([None] + [2, 3] + [None] * 4997, 1, 3)

        self.assertEqual(dequeue(list1), (1, newlist1))
        self.assertEqual(dequeue(list2), (1, newlist2))
        self.assertRaises(IndexError, dequeue, empty)

    def test_peek(self):
        empty = Queue([None] * 5000, 0, 0)
        list1 = Queue([1] + [None] * 4999, 0, 1)
        list2 = Queue([1, 2, 3] + [None] * 4997, 0, 3)

        self.assertEqual(peek(list1), 1)
        self.assertEqual(peek(list2), 1)
        self.assertRaises(IndexError, peek, empty)

    def test_size(self):
        empty = Queue([None] * 5000, 0, 0)
        list1 = Queue([1] + [None] * 4999, 0, 1)
        list2 = Queue([1, 2, 3] + [None] * 4997, 0, 3)

        self.assertEqual(size(empty), 0)
        self.assertEqual(size(list1), 1)
        self.assertEqual(size(list2), 3)

    def test_is_empty(self):
        empty = Queue([None] * 5000, 0, 0)
        list = Queue([1, 2, 3] + [None] * 4997, 0, 3)
        self.assertTrue(is_empty(empty))
        self.assertFalse(is_empty(list))

if __name__ == "__main__":
    unittest.main()
