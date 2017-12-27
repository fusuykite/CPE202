#bst.py

# A BSTNodeRef is one of
# - None
# - A BSTNode
class BSTNode:
    def __init__(self, value, left, right):
        self.value = value # a value
        self.left = left # a BSTNodeRef
        self.right = right # a BSTNodeRef
    def __eq__(self, other):
        return (type(other) == BSTNode
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right)
    def __repr__(self,):
        return "BSTNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right)


# A BinarySearchTree represents a BSTNode along with a given comes_before ref
class BinarySearchTree:
    def __init__(self, comes_before, bst=None):
        self.bst = bst
        self.comes_before = comes_before
    def __eq__(self, other):
        return (type(other) == BinarySearchTree
                and self.bst == other.bst
                and self.comes_before == other.comes_before)
    def __repr__(self):
        return "BinarySearchTree({!r})".format(self.bst)

# BinarySearchTree -> boolean
# returns whether or not the given BinarySearchTree is empty or not
def is_empty(bst):
    return bst.bst == None

# BinarySearchTree value -> BinarySearchTree
# returns a BST with the value inserted into the list in the appropriate spot
def insert(bst, val):
    return BinarySearchTree(bst.comes_before, insert_helper(bst.bst, bst.comes_before, val))

# BSTNodeRef func value -> BSTNode
# returns a BSTNode with the value inserted into it
def insert_helper(bstnode, comes_before, val):
    if bstnode == None:
        return BSTNode(val, None, None)
    if comes_before(val, bstnode.value):
        return BSTNode(bstnode.value, insert_helper(bstnode.left, comes_before, val), bstnode.right)
    return BSTNode(bstnode.value, bstnode.left, insert_helper(bstnode.right, comes_before, val))

# BinarySearchTree value -> Boolean
# returns whether or not the passed value is in the BinarySearchTree
def lookup(bst, val):
    return lookup_helper(bst.bst, bst.comes_before, val)

# BSTNodeRef func value -> Boolean
# returns whether or not the passed value is in the BSTNodeRef
def lookup_helper(bstnode, comes_before, val):
    if bstnode == None:
        return False
    if comes_before(val, bstnode.value):
        return lookup_helper(bstnode.left, comes_before, val)
    elif comes_before(bstnode.value, val):
        return lookup_helper(bstnode.right, comes_before, val)
    else:
        return True

# BinarySearchTree value -> BinarySearchTree
# returns a BinarySearchTree with the passed value deleted from the BinarySearchTree
def delete(bst, val):
    if is_empty(bst):
        return bst
    return BinarySearchTree(bst.comes_before, delete_helper(bst.bst, bst.comes_before, val))

# BSTNodeRef fun value -> BSTNodeRef
# returns a BSTNodeRef with the passed value deleted
def delete_helper(bstnode, comes_before, val):
    if bstnode.value == val:
        if bstnode.left == None and bstnode.right == None:
            return None
        elif bstnode.left == None:
            return bstnode.right
        elif bstnode.right == None:
            return bstnode.left
        else:
            lowest = find_min(bstnode.right)
            return BSTNode(lowest, bstnode.left, delete_helper(bstnode.right, comes_before, lowest))
    if comes_before(val, bstnode.value):
        return BSTNode(bstnode.value, delete_helper(bstnode.left, comes_before, val), bstnode.right)
    return BSTNode(bstnode.value, bstnode.left, delete_helper(bstnode.right, comes_before, val))

# BSTNodeRef -> value
# returns the minimum value in a BSTNode
def find_min(bstnode):
    if bstnode.left == None:
        return bstnode.value
    return find_min(bstnode.left)

# BinarySearchTree -> Iterator
# returns an Iterator of the BinarySearchTree in prefix order
def prefix_iterator(bst):
    if bst.bst != None:
        yield bst.bst.value
        yield from prefix_iterator(BinarySearchTree(bst.comes_before, bst.bst.left))
        yield from prefix_iterator(BinarySearchTree(bst.comes_before, bst.bst.right))

# BinarySearchTree -> Iterator
# returns an Iterator of the BinarySearchTree in infix order
def infix_iterator(bst):
    if bst.bst != None:
        yield from infix_iterator(BinarySearchTree(bst.comes_before, bst.bst.left))
        yield bst.bst.value
        yield from infix_iterator(BinarySearchTree(bst.comes_before, bst.bst.right))

# BinarySearchTree -> Iterator
# returns an Iterator of the BinarySearchTree in postfix order
def postfix_iterator(bst):
    if bst.bst != None:
        yield from postfix_iterator(BinarySearchTree(bst.comes_before, bst.bst.left))
        yield from postfix_iterator(BinarySearchTree(bst.comes_before, bst.bst.right))
        yield bst.bst.value
