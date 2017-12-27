import unittest
from bst import *

def comes_before(v1, v2):
    return v1 < v2

class TestCases(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(BinarySearchTree(comes_before, None)), 'BinarySearchTree(None)')
        self.assertEqual(repr(BSTNode(4, None, None)), 'BSTNode(4, None, None)')

    def test_is_empty(self):
        a = BinarySearchTree(comes_before, None)
        b = BinarySearchTree(comes_before, BSTNode(4, None, None))
        
        self.assertTrue(is_empty(a))
        self.assertFalse(is_empty(b))

    def test_insert(self):
        a = BinarySearchTree(comes_before, None)
        b = BinarySearchTree(comes_before, BSTNode(4, None, None))
        c = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, BSTNode(0, None, None), None), BSTNode(7, None, None)))
        d = BinarySearchTree(comes_before, BSTNode(6, None, BSTNode(12, None, None)))
        
        ares = BinarySearchTree(comes_before, BSTNode(6, None, None))
        bres = BinarySearchTree(comes_before, BSTNode(4, None, BSTNode(7, None, None)))
        bres_1 = BinarySearchTree(comes_before, BSTNode(4, BSTNode(3, None, None), None))
        cres = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, BSTNode(0, None, None), BSTNode(2, None, None)), BSTNode(7, None, None)))
        dres = BinarySearchTree(comes_before, BSTNode(6, None, BSTNode(12, None, BSTNode(15, None, None))))
        
        self.assertEqual(insert(a, 6), ares)
        self.assertEqual(insert(b, 7), bres)
        self.assertEqual(insert(b, 3), bres_1)
        self.assertEqual(insert(c, 2), cres)
        self.assertEqual(insert(d, 15), dres)

    def test_lookup(self):
        a = BinarySearchTree(comes_before, None)
        b = BinarySearchTree(comes_before, BSTNode(4, None, None))
        c = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, BSTNode(0, None, None), None), BSTNode(7, None, None)))
        d = BinarySearchTree(comes_before, BSTNode(6, None, BSTNode(12, None, None)))
        
        self.assertFalse(lookup(a, 8))
        self.assertTrue(lookup(b, 4))
        self.assertFalse(lookup(b, 2))
        self.assertTrue(lookup(c, 4))
        self.assertTrue(lookup(c, 7))
        self.assertTrue(lookup(c, 0))
        self.assertTrue(lookup(c, 1))
        self.assertFalse(lookup(c, 14))
        self.assertTrue(lookup(d, 6))
        self.assertTrue(lookup(d, 12))
        self.assertFalse(lookup(d, 69))

    def test_delete(self):
        a = BinarySearchTree(comes_before, None)
        b = BinarySearchTree(comes_before, BSTNode(4, None, None))
        c = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, BSTNode(0, None, None), None), BSTNode(7, None, None)))
        d = BinarySearchTree(comes_before, BSTNode(6, None, BSTNode(12, None, None)))
        e = BinarySearchTree(comes_before, BSTNode(5, BSTNode(3, None, BSTNode(4, None, None)), None))

        bres = BinarySearchTree(comes_before, None)
        cres = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, None, None), BSTNode(7, None, None)))
        cres_1 = BinarySearchTree(comes_before, BSTNode(4, BSTNode(0, None, None), BSTNode(7, None, None)))
        cres_2 = BinarySearchTree(comes_before, BSTNode(4, BSTNode(1, BSTNode(0, None, None), None), None))
        cres_3 = BinarySearchTree(comes_before, BSTNode(7, BSTNode(1, BSTNode(0, None, None), None), None))
        eres = BinarySearchTree(comes_before, BSTNode(5, BSTNode(4, None, None), None))
        
        self.assertEqual(delete(a, 9), a)
        self.assertEqual(delete(b, 4), bres)
        self.assertEqual(delete(c, 0), cres)
        self.assertEqual(delete(c, 1), cres_1)
        self.assertEqual(delete(c, 7), cres_2)
        self.assertEqual(delete(c, 4), cres_3)
        self.assertEqual(delete(e, 3), eres)
    
    def test_find_min(self):
        a = BSTNode(4, BSTNode(3, BSTNode(2, None, None), None), None)
        self.assertEqual(find_min(a), 2)
if __name__ == '__main__':
    unittest.main()
