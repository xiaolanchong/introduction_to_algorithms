
import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def testSimpleArray(self):
        input_arr = [10, -2, 3, 1, 101, 5]
        expected = [-2, 1, 3, 5, 10, 101]
        actual = merge_sort(input_arr)
        self.assertEqual(expected, actual)

    def testEmptyArray(self):
        input_arr = []
        expected = []
        actual = merge_sort(input_arr)
        self.assertEqual(expected, actual)

    def testSortedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        expected = input_arr
        actual = merge_sort(input_arr)
        self.assertEqual(expected, actual)

    def testReversedArray(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        input_arr = list(reversed(expected))
        actual = merge_sort(input_arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
