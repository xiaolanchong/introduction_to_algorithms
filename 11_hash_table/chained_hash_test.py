import unittest
import random
from chained_hash import ChainedHash


def to_array(slist):
    def append(value):
        arr.append(value)
        return True
    arr = []
    slist.iterate(append)
    return arr


class TestSinglyLinkedList(unittest.TestCase):
    def testInsertion(self):
        htable = ChainedHash()
        htable.insert(11)
        htable.insert(33)
        htable.insert(102)
        htable.insert(101)

        self.assertTrue(htable.search(11))
        self.assertTrue(htable.search(33))
        self.assertTrue(htable.search(102))
        self.assertFalse(htable.has_collision)

        htable.delete(11)
        self.assertFalse(htable.search(11))

    def testCollision(self):
        htable = ChainedHash(True, 10)
        trial = 1
        while not htable.has_collision:
            htable.insert(random.randint(0, 10000))
            trial += 1

        self.assertLess(trial, 80)


if __name__ == '__main__':
    unittest.main()
