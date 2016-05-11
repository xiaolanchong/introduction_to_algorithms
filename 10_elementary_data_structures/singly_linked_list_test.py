import unittest
from singly_linked_list import SinglyLinkedList


def to_array(slist):
    def append(value):
        arr.append(value)
        return True
    arr = []
    slist.iterate(append)
    return arr


class TestSinglyLinkedList(unittest.TestCase):
    def testInsertion(self):
        slist = SinglyLinkedList()
        tail = slist.insert_after(None, 10)
        slist.insert_after(None, 11)
        actual = to_array(slist)
        expected = [11, 10]
        self.assertEqual(expected, actual)

        slist.insert_after(tail, 12)
        actual = to_array(slist)
        expected = [11, 10, 12]
        self.assertEqual(expected, actual)

    def testDeletion(self):
        slist = SinglyLinkedList()
        tail = slist.insert_after(None, 13)
        slist.insert_after(None, 12)

        actual = to_array(slist)
        expected = [12, 13]
        self.assertEqual(expected, actual)

        slist.delete_after(tail)

        actual = to_array(slist)
        expected = [12, 13]
        self.assertEqual(expected, actual)

        slist.delete_after(slist.head)

        actual = to_array(slist)
        expected = [12]
        self.assertEqual(expected, actual)

    def testReverse(self):
        slist = SinglyLinkedList()
        slist.insert_after(None, 14)
        slist.insert_after(None, 13)
        slist.insert_after(None, 12)
        slist.insert_after(None, 11)

        slist.reverse()

        actual = to_array(slist)
        expected = [14, 13, 12, 11]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()