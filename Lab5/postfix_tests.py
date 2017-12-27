import unittest
from postfix import *

class TestPostfix(unittest.TestCase):
    def test00_interface(self):
        postfix_calc("1 1 +")

    def test(self):
        self.assertAlmostEqual(postfix_calc('1 2 + 4 *'), 12)
        self.assertAlmostEqual(postfix_calc('1 1 +'), 2)
        self.assertAlmostEqual(postfix_calc('10 5 + 5 / 3 * 10 *'), 90)
        self.assertAlmostEqual(postfix_calc('10 5 - 5 /'), 1)
        self.assertAlmostEqual(postfix_calc('4 5 + 2 /'), 4.5)
        self.assertAlmostEqual(postfix_calc("8"), 8.0)

if __name__ == "__main__":
    unittest.main()
