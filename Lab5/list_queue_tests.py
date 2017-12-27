import unittest
from list_queue import *

class TestCase(unittest.TestCase):
    def test_empty_queue(self):
        empty = Queue(None, None)
        self.assertEqual(empty_queue(), empty)

    def test_enqueue(self):
        empty = Queue(None, None)
        q1 = Queue(None, Pair(1, None))
        q2 = Queue(None, Pair(1, Pair(2, Pair(3, None))))

        newempty = Queue(None, Pair(1, None))
        new1 = Queue(None, Pair(2, Pair(1, None)))
        new2 = Queue(None, Pair(4, Pair(1, Pair(2, Pair(3, None)))))

        self.assertEqual(enqueue(empty, 1), newempty)
        self.assertEqual(enqueue(q1, 2), new1)
        self.assertEqual(enqueue(q2, 4), new2)

    def test_dequeue(self):
        empty = Queue(None, None)
        q1 = Queue(Pair(1, None), Pair(1, None))
        q2 = Queue(Pair(1, Pair(2, Pair(3, None))), Pair(1, Pair(2, Pair(3, None))))
        q3 = Queue(None, Pair(1, Pair(2, Pair(3, None))))

        list = empty_list()
        for i in range(50):
            list = add(list, 0, i)

        q4 = Queue(list, None)

        new_list = empty_list()
        for i in range(49):
            new_list = add(new_list, 0, i)

        new4 = Queue(new_list, None)
        new1 = Queue(None, Pair(1, None))
        new2 = Queue(Pair(2, Pair(3, None)), Pair(1, Pair(2, Pair(3, None))))
        new3 = Queue(Pair(2, Pair(1, None)), Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(dequeue(q1), (1, new1))
        self.assertEqual(dequeue(q2), (1, new2))
        self.assertEqual(dequeue(q3), (3, new3))
        self.assertEqual(dequeue(q4), (49, new4))
        self.assertRaises(IndexError, dequeue, empty)

    def test_peek(self):
        empty = Queue(None, None)
        q1 = Queue(Pair(1, None), Pair(1, None))
        q2 = Queue(Pair(1, Pair(2, Pair(3, None))), Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(peek(enqueue(enqueue(enqueue(empty_queue(), 3), 2), 1)), 3)
        self.assertRaises(IndexError, peek, empty)
        self.assertEqual(peek(q1), 1)
        self.assertEqual(peek(q2), 1)

    def test_size(self):
        empty = Queue(None, None)
        q1 = Queue(Pair(1, None), Pair(1, None))
        q2 = Queue(Pair(1, Pair(2, Pair(3, None))), Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(size(enqueue(enqueue(enqueue(empty_queue(), 3), 2), 1)), 3)
        self.assertEqual(size(empty), 0)
        self.assertEqual(size(q1), 2)
        self.assertEqual(size(q2), 6)

    def test_is_empty(self):
        empty = Queue(None, None)
        q1 = Queue(Pair(1, None), Pair(1, None))

        self.assertTrue(is_empty(empty))
        self.assertFalse(is_empty(q1))

if __name__ == '__main__':
    unittest.main()