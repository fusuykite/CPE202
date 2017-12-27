from priority_queue import *
import unittest

class TestCase(unittest.TestCase):
    def test_repr(self):
        list = Pair(1, Pair(2, Pair(3, None)))
        self.assertEqual(repr(list), 'Pair(1, Pair(2, Pair(3, None)))')

        pqueue = PQueue(comes_before, list)
        self.assertEqual(repr(pqueue), 'PQueue: Pair(1, Pair(2, Pair(3, None)))')

    def test_comes_before(self):
        self.assertTrue(comes_before(1, 2))
        self.assertFalse(comes_before(2, 1))

    def test_empty_pqueue(self):
        empty = PQueue(comes_before, None)
        self.assertEqual(empty_pqueue(comes_before), empty)

    def test_enqueue(self):
        empty = empty_pqueue(comes_before)
        newEmpty = PQueue(comes_before, Pair(1, None))

        queue1 = PQueue(comes_before, Pair(1, Pair(3, None)))
        newQueue1 = PQueue(comes_before, Pair(1, Pair(2, Pair(3, None))))

        queue2 = PQueue(comes_before, Pair(2, Pair(3, None)))
        newQueue2 = PQueue(comes_before, Pair(1, Pair(2, Pair(3, None))))

        queue3 = PQueue(comes_before, Pair(1, Pair(2, None)))
        newQueue3 = PQueue(comes_before, Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(enqueue(empty, 1), newEmpty)
        self.assertEqual(enqueue(queue1, 2), newQueue1)
        self.assertEqual(enqueue(queue2, 1), newQueue2)
        self.assertEqual(enqueue(queue3, 3), newQueue3)

    def test_dequeue(self):
        empty = empty_pqueue(comes_before)
        queue = PQueue(comes_before, Pair(0, Pair(1, Pair(2, Pair(3, None)))))
        newQueue = PQueue(comes_before, Pair(1, Pair(2, Pair(3, None))))

        self.assertEqual(dequeue(queue), (0, newQueue))
        self.assertRaises(IndexError, dequeue, empty)

    def test_peek(self):
        empty = empty_pqueue(comes_before)
        queue = PQueue(comes_before, Pair(1, Pair(2, None)))

        self.assertRaises(IndexError, peek, empty)
        self.assertEqual(peek(queue), 1)

    def test_size(self):
        empty = empty_pqueue(comes_before)
        queue1 = PQueue(comes_before, Pair(1, None))
        queue2 = PQueue(comes_before, Pair(1, Pair(2, None)))

        self.assertEqual(size(empty), 0)
        self.assertEqual(size(queue1), 1)
        self.assertEqual(size(queue2), 2)

    def test_is_empty(self):
        empty = empty_pqueue(comes_before)
        queue = PQueue(comes_before, Pair(1, Pair(2, None)))

        self.assertTrue(is_empty(empty))
        self.assertFalse(is_empty(queue))

if __name__ == '__main__':
    unittest.main()