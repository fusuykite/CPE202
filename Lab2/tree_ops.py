# * Section 2 (Trees)

# * dd: NumTree Data Definition

# a familyTree is one of
# - "mt"
# - a Person

class Person:
    def __init__(self, name, mom, dad):
        self.name = name    # a string
        self.mom = mom      # a familyTree
        self.dad = dad      # a familyTree
    def __eq__(self, other):
        return (type(other) == Person) and \
               self.name == other.name and \
               self.mom == other.mom and \
               self.dad == other.dad
    def __repr__(self):
        return "Pair({!r}, {!r}, {!r})".format(self.name, self.mom, self.dad)

# * 1:
# familyTree -> int
# the size(familyTree) function takes a familyTree and returns the number elements in the tree
def size(familyTree):
    if familyTree == "mt":
        return 0
    else:
        return size(familyTree.mom) + 1 + size(familyTree.dad)

# * 2:
#familyTree -> int
# the num_leaves(familyTree) function takes a familyTree and returns the number of leaves(mom/dad both "unk")
def num_leaves(familyTree):
    if familyTree == "mt":
        return 0
    else:
        if familyTree.name != "mt" and familyTree.mom == "mt" and familyTree.dad == "mt":
            return 1
        else:
            return num_leaves(familyTree.mom) + num_leaves(familyTree.dad)
# * 3:
#familyTree -> int
# the sum(familyTree) function takes a familyTree and returns the sum of the values in the familyTree
def sum(familyTree):
    if familyTree == 'mt':
        return 0
    return familyTree.name + sum(familyTree.mom) + sum(familyTree.dad)

# * 4:


# * 5:
def has_triple(familyTree):
    if familyTree == 'mt':
        return False
    if familyTree.mom != 'mt' and familyTree.mom.name == 3 * familyTree.name:
        return True
    if familyTree.dad != 'mt' and familyTree.dad.name == 3 * familyTree.name:
        return True
    return has_triple(familyTree.mom) == True or has_triple(familyTree.dad) == True


# * 6:
# familyTree -> familyTree
# the sub_one_map(familyTree) function returns a new tree with each value smaller by one
def sub_one_map(familyTree):
    if familyTree == "mt":
        return "mt"
    return Person(familyTree.name - 1, sub_one_map(familyTree.mom), sub_one_map(familyTree.dad))

# * Tests : the test case class for the tree functions



import unittest
class TestCase(unittest.TestCase):
    #tree1 = 'mt'
    #tree2 = Person(4, Person(8, "mt", "mt"), Person(9, 'mt', 'mt'))
    #tree3 = Person(9, Person(15, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))
    #tree4 = Person(2, "mt", "mt")


    def test_find_elements(self):
        self.assertEqual(size('mt'), 0)
        self.assertEqual(size(Person(4, Person(8, "mt", "mt"), Person(9, 'mt', 'mt'))), 3)
        self.assertEqual(size(Person(9, Person(15, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))), 5)
        self.assertEqual(size(Person(2, "mt", "mt")), 1)
        self.assertEqual(size(Person(4, Person(-20, 'mt', 'mt'), Person(-13, 'mt', 'mt'))), 3)

    def test_num_leaves(self):
        self.assertEqual(num_leaves("mt"), 0)
        self.assertEqual(num_leaves(Person(4, Person(8, "mt", "mt"), Person(9, 'mt', 'mt'))), 2)
        self.assertEqual(num_leaves
            (Person(9, Person(15, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))), 2)
        self.assertEqual(num_leaves(Person(2, "mt", "mt")), 1)
        self.assertEqual(num_leaves(Person(4, Person(-20, 'mt', 'mt'), Person(-13, 'mt', 'mt'))), 2)

    def test_sum(self):
        self.assertEqual(sum("mt"), 0)
        self.assertEqual(sum(Person(4, Person(8, "mt", "mt"), Person(9, 'mt', 'mt'))), 21)
        self.assertEqual(sum
            (Person(9, Person(15, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))), 65)
        self.assertEqual(sum(Person(2, "mt", "mt")), 2)
        self.assertEqual(sum(Person(4, Person(-20, 'mt', 'mt'), Person(-13, 'mt', 'mt'))), -29)

    def test_has_triple(self):
        self.assertEqual(has_triple(Person(4, Person(12, "mt", "mt"), Person(9, 'mt', 'mt'))), True)
        self.assertEqual(has_triple("mt"), False)
        self.assertEqual(has_triple(Person(2, "mt", "mt")), False)
        self.assertEqual(has_triple
                         (Person(9, Person(27, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))),
                         True)
        self.assertEqual(has_triple(Person(4, Person(-20, 'mt', 'mt'), Person(-13, 'mt', 'mt'))), False)

    def test_sub_one_map(self):
        self.assertEqual(sub_one_map(Person(2, "mt", "mt")), Person(1, "mt", "mt"))
        self.assertEqual(sub_one_map(Person(9, Person(15, "mt", Person(6, "mt", "mt")), Person(17, Person(18, "mt", "mt"), "mt"))), Person(8, Person(14, "mt", Person(5, "mt", "mt")), Person(16, Person(17, "mt", "mt"), "mt")))
        self.assertEqual(sub_one_map('mt'), 'mt')
        self.assertEqual(sub_one_map(Person(4, Person(-20, 'mt', 'mt'), Person(-13, 'mt', 'mt'))), Person(3, Person(-21, 'mt', 'mt'), Person(-14, 'mt', 'mt')))

if __name__ == '__main__':
    unittest.main()
