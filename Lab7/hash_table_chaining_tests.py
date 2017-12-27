# hash_table_chaining_tests.py
import unittest
from hash_table_chaining import *
from linked_list import Pair

class TestCase(unittest.TestCase):
    def test_eq_repr(self):
        a = empty_hash_table()
        b = empty_hash_table()
        self.assertEqual(repr(a), repr(b))
        self.assertEqual(a, b)

    def test_empty_hash_table(self):
        a = empty_hash_table()
        self.assertEqual(a, HashTable(8, 0, [None] * 8, 0))

    def test_insert(self):
        a = empty_hash_table()
        a = insert(a, 0, 'test')
        self.assertEqual(a, HashTable(8, 1, [Pair((0, 'test'), None), None, None, None, None, None, None, None], 0))
        a = insert(a, 8, 'another test')
        self.assertEqual(a, HashTable(8, 2, [Pair((0, 'test'), Pair((8, 'another test'), None)), None, None, None, None, None, None, None], 1))
        a = insert(a, 8, 'another test')
        self.assertEqual(a, HashTable(8, 2, [Pair((0, 'test'), Pair((8, 'another test'), None)), None, None, None, None, None, None, None], 1))
        a = insert(a, 1, 'refrigerator')
        self.assertEqual(a, HashTable(8, 3, [Pair((0, 'test'), Pair((8, 'another test'), None)), Pair((1, 'refrigerator'), None), None, None, None, None, None, None], 1))
        a = insert(a, 2, 'a')
        a = insert(a, 10, 'b')
        a = insert(a, 3, 'c')
        a = insert(a, 11, 'd')
        a = insert(a, 4, 'e')
        a = insert(a, 12, 'f')
        a = insert(a, 5, 'g')
        a = insert(a, 13, 'h')
        a = insert(a, 6, 'i')
        a = insert(a, 14, 'j')
        self.assertEqual(a, HashTable(16, 13, [Pair((0, 'test'), None), Pair((1, 'refrigerator'), None), Pair((2, 'a'), None), Pair((3, 'c'), None), Pair((4, 'e'), None), Pair((5, 'g'), None), Pair((6, 'i'), None), None, Pair((8, 'another test'), None), None, Pair((10, 'b'), None), Pair((11, 'd'), None), Pair((12, 'f'), None), Pair((13, 'h'), None), Pair((14, 'j'), None), None], 0))
        b = empty_hash_table()
        b = insert(b, 0, 'a')
        b = insert(b, 16, 'b')
        b = insert(b, 32, 'c')
        b = insert(b, 1, 'd')
        b = insert(b, 2, 'e')
        b = insert(b, 10, 'f')
        b = insert(b, 3, 'g')
        b = insert(b, 11, 'h')
        b = insert(b, 4, 'i')
        b = insert(b, 12, 'j')
        b = insert(b, 5, 'k')
        b = insert(b, 13, 'l')
        b = insert(b, 6, 'm')
        self.assertEqual(b, HashTable(16, 13, [Pair((0, 'a'), Pair((16, 'b'), Pair((32, 'c'), None))), Pair((1, 'd'), None), Pair((2, 'e'), None), Pair((3, 'g'), None), Pair((4, 'i'), None), Pair((5, 'k'), None), Pair((6, 'm'), None), None, None, None, Pair((10, 'f'), None), Pair((11, 'h'), None), Pair((12, 'j'), None), Pair((13, 'l'), None), None, None], 2))       

    def test_get(self):
        a = empty_hash_table()
        a = insert(a, 0, 'a')
        a = insert(a, 8, 'b')
        a = insert(a, 1, 'c')
        self.assertEqual(get(a, 0), 'a')
        self.assertEqual(get(a, 8), 'b')
        self.assertEqual(get(a, 1), 'c')
        with self.assertRaises(LookupError):
            get(a, 16)
        with self.assertRaises(LookupError):
            get(a, 4)

    def test_remove(self):
        a = empty_hash_table()
        a = insert(a, 0, 'a')
        a = insert(a, 8, 'b')
        a = insert(a, 1, 'c')
        a = insert(a, 9, 'd')
        self.assertEqual(remove(a, 8), HashTable(8, 3, [Pair((0, 'a'), None), Pair((1, 'c'), Pair((9, 'd'), None)), None, None, None, None, None, None], 2))
        self.assertEqual(remove(a, 0), HashTable(8, 2, [None, Pair((1, 'c'), Pair((9, 'd'), None)), None, None, None, None, None, None], 2))
        with self.assertRaises(LookupError):
            remove(a, 17)
        with self.assertRaises(LookupError):
            remove(a, 2)

    def test_size(self):
        a = empty_hash_table()
        self.assertEqual(size(a), 0)

    def test_load_factor(self):
        a = empty_hash_table()
        a = insert(a, 0, 'a')
        a = insert(a, 1, 'b')
        a = insert(a, 2, 'c')
        a = insert(a, 3, 'd')
        a = insert(a, 4, 'e')
        a = insert(a, 5, 'f')
        a = insert(a, 6, 'g')
        a = insert(a, 7, 'h')
        self.assertEqual(load_factor(a), 1)

    def test_collisions(self):
        a = empty_hash_table()
        self.assertEqual(collisions(a), 0)


if __name__ == '__main__':
    unittest.main()
