import unittest
from open_addressing_hash import OpenAddressingHash


class TestOpenAddressingHash(unittest.TestCase):
    def testInsertion(self):
        htable = OpenAddressingHash()
        self.assertTrue(htable.insert(11))
        self.assertTrue(htable.insert(33))
        self.assertTrue(htable.insert(102))
        self.assertTrue(htable.insert(101))

        self.assertTrue(htable.search(11))
        self.assertTrue(htable.search(33))
        self.assertTrue(htable.search(102))
        self.assertFalse(htable.search(88))

        htable.delete(11)
        self.assertFalse(htable.search(11))


if __name__ == '__main__':
    unittest.main()
