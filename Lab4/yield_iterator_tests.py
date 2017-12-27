import unittest
from linked_list import Pair
from linked_list import yield_iterator

class TestCases(unittest.TestCase):
    def test_yield_iterator(self):
        gen = yield_iterator(Pair(3, Pair(6, Pair(9, Pair(14, None)))))
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 9)
        self.assertEqual(next(gen), 14)


if __name__ == '__main__':
    unittest.main()
