import unittest
from doubly_linked_list import DoublyLinkedList


def to_array(slist):
    arr = []
    item = slist.begin()
    while item != slist.end():
        arr.append(item.value)
        item = item.next
    return arr


class TestDoublyLinkedList(unittest.TestCase):
    def testInsertion(self):
        dlist = DoublyLinkedList()
        dlist.insert_beginning(10)
        dlist.insert_beginning(11)

        expected = [11, 10]
        actual = to_array(dlist)
        self.assertEqual(expected, actual)

        dlist.insert_beginning(12)

        actual = to_array(dlist)
        expected = [12, 11, 10]
        self.assertEqual(expected, actual)

    def testDeletionAndSearch(self):
        dlist = DoublyLinkedList()
        dlist.insert_beginning(10)
        dlist.insert_beginning(11)
        dlist.insert_beginning(16)
        dlist.insert_beginning(13)

        found = dlist.search(11)
        self.assertEqual(found.value, 11)

        dlist.delete(found)

        actual = to_array(dlist)
        expected = [13, 16, 10]
        self.assertEqual(expected, actual)

        found = dlist.search(11)
        self.assertIsNone(found)

if __name__ == '__main__':
    unittest.main()