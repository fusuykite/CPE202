import unittest
from linked_list import *

class TestCases(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Iterator(None)), 'Iterator(None)')

    def test_object_iterator(self):
        a = Pair(4, Pair(6, Pair(9, None)))
        ares = Iterator(Pair(4, Pair(6, Pair(9, None))))
        self.assertEqual(object_iterator(a), ares)
    
    def test_has_next(self):
        a = Iterator(Pair(4, Pair(6, Pair(9, None))))
        b = Iterator(None)
        self.assertTrue(has_next(a))
        self.assertFalse(has_next(b))

    def test_next(self):
        a = Iterator(Pair(4, Pair(6, Pair(9, None))))
        self.assertEqual(next(a), 4)
        self.assertEqual(next(a), 6)
        self.assertEqual(next(a), 9)
        with self.assertRaises(StopIteration):
            next(a)


if __name__ == '__main__':
    unittest.main()
