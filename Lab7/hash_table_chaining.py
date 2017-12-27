# hash_table_chaining.py

import linked_list


# a HashTable is an array-based implementation of a hash table
class HashTable:
    def __init__(self, size, items, table, collisions):
        self.size = size # an int
        self.items = items # an int
        self.table = table # a list
        self.collisions = collisions # an int

    def __eq__(self, other):
        return (type(other) == HashTable
                and self.size == other.size
                and self.items == other.items
                and self.table == other.table
                and self.collisions == other.collisions)

    def __repr__(self):
        return "HashTable({!r}, {!r}, {!r}, {!r})".format(self.size, self.items, self.table, self.collisions)

# none -> HashTable
# returns an empty HashTable of size 8
def empty_hash_table():
    return HashTable(8, 0, [None] * 8, 0)

# HashTable key AnyType -> HashTable
# inserts the item (with key) into the HashTable and returns the result
def insert(ht, key, item):
    index = hash(key) % ht.size
    if ht.table[index] != None:
        if insert_helper(ht.table[index], key, item):
            pass
        else:
            ht.collisions += 1
            ht.items += 1
            ht.table[index] = linked_list.add(ht.table[index], linked_list.length(ht.table[index]), (key, item))
    else:
        ht.table[index] = linked_list.add(ht.table[index], linked_list.length(ht.table[index]), (key, item))
        ht.items += 1
    if ht.items / ht.size > 1.5:
        new_table = HashTable(ht.size * 2, ht.items, [None] * (ht.size * 2), 0)
        for item in ht.table:
            if item != None:
                if linked_list.length(item) > 1:
                    for item_index in range(linked_list.length(item)):
                        new_index = hash(linked_list.get(item, item_index)[0]) % new_table.size
                        if new_table.table[new_index] != None:
                            new_table.collisions += 1
                            new_table.table[new_index] = linked_list.add(new_table.table[new_index], linked_list.length(new_table.table[new_index]), linked_list.get(item, item_index))
                        else:
                            new_table.table[new_index] = linked_list.Pair(linked_list.get(item, item_index), None)
                else:
                    new_index = hash(item.first[0]) % new_table.size
#                    if new_table.table[new_index] != None:
#                        if insert_helper(new_table.table[new_index], item.first[0], item.first[1]):
#                            pass
#                        else:
#                            collisions += 1
#                            new_table.table[new_index] = linked_list.Pair(item.first, None)
#                    else:
                    new_table.table[new_index] = linked_list.Pair(item.first, None)
        ht = new_table
    return ht

def insert_helper(anylist, key, item):
    if anylist == None:
        return False
    if anylist.first == (key, item):
        return True
    return insert_helper(anylist.rest, key, item)

# HashTable key -> AnyType
# returns the item at the given key
def get(ht, key):
    index = hash(key) % ht.size
    if ht.table[index] == None:
        raise LookupError
    if linked_list.length(ht.table[index]) > 1:
        for item_index in range(linked_list.length(ht.table[index])):
            itemref = linked_list.get(ht.table[index], item_index)
            if itemref[0] == key:
                return itemref[1]
        raise LookupError
    return ht.table[index].first[1]

# HashTable key -> HashTable
# removes the item at the given key and returns the remaining HashTable
def remove(ht, key):
    index = hash(key) % ht.size
    if ht.table[index] == None:
        raise LookupError
    if linked_list.length(ht.table[index]) > 1:
        for item_index in range(linked_list.length(ht.table[index])):
            itemref = linked_list.get(ht.table[index], item_index)
            if itemref[0] == key:
                ht.table[index] = linked_list.remove(ht.table[index], item_index)[1]
                ht.items -= 1
                return ht
        raise LookupError
    ht.table[index] = None
    ht.items -= 1
    return ht

# HashTable -> int
# returns the number of items in the hash table
def size(ht):
    return ht.items

# HashTable -> float
# returns the current load factor of the hash table
def load_factor(ht):
    return ht.items / ht.size

# HashTable -> int
# returns the number of collisions that have occured during insertions into the hash table
def collisions(ht):
    return ht.collisions
