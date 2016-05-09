
import unittest
from binary_heap import BinaryHeap, heapsort


class TestBinaryHeap(unittest.TestCase):
    def testBinaryHeapOperations(self):
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        heap = BinaryHeap(arr)

        self.assertEqual(6, heap.left(3))
        self.assertEqual(7, heap.right(3))
        self.assertEqual(1, heap.parent(3))
        self.assertEqual(8, heap.get_item(4))
        self.assertEqual(len(arr), heap.heap_size())

    def testHeapBuilding(self):
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        heap = BinaryHeap(arr)
        expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        actual = heap.items

        self.assertEqual(expected, actual)

    def testSimpleArray(self):
        input_arr = [10, -2, 3, 1, 101, 5]
        expected = [-2, 1, 3, 5, 10, 101]
        actual = heapsort(input_arr)
        self.assertEqual(expected, actual)

    def testEmptyArray(self):
        input_arr = []
        expected = []
        actual = heapsort(input_arr)
        self.assertEqual(expected, actual)

    def testSortedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        expected = input_arr
        actual = heapsort(input_arr)
        self.assertEqual(expected, actual)

    def testReversedArray(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        input_arr = list(reversed(expected))
        actual = heapsort(input_arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
