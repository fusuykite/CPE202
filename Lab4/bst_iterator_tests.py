import unittest
from bst import *

def comes_before(v1, v2):
    return v1 < v2

class TestCases(unittest.TestCase):
    def test_prefix_iterator(self):
        a = BinarySearchTree(comes_before, BSTNode(4, BSTNode(2, None, None), BSTNode(6, None, None)))
        gen = prefix_iterator(a)
        self.assertEqual(next(gen), 4)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 6)

    def test_infix_iterator(self):
        a = BinarySearchTree(comes_before, BSTNode(4, BSTNode(2, None, None), BSTNode(6, None, None)))
        gen = infix_iterator(a)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 4)
        self.assertEqual(next(gen), 6)

    def test_postfix_iterator(self):
        a = BinarySearchTree(comes_before, BSTNode(4, BSTNode(2, None, None), BSTNode(6, None, None)))
        gen = postfix_iterator(a)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 4)

if __name__ == '__main__':
    unittest.main()
