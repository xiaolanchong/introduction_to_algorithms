import unittest
import random
from chained_hash import ChainedHash


class TestChainedHash(unittest.TestCase):
    def testInsertion(self):
        htable = ChainedHash()
        htable.insert(11)
        htable.insert(33)
        htable.insert(102)
        htable.insert(101)

        self.assertTrue(htable.search(11))
        self.assertTrue(htable.search(33))
        self.assertTrue(htable.search(102))
        self.assertFalse(htable.search(1012))

        self.assertTrue(htable.delete(11))
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
