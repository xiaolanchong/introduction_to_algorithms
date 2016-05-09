
import unittest
from quicksort import quicksort, quicksort_randomized


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.sort_func = quicksort

    def testSimpleArray(self):
        input_arr = [10, -2, 3, 1, 101, 5]
        expected = [-2, 1, 3, 5, 10, 101]
        actual = self.sort_func(input_arr)
        self.assertEqual(expected, actual)

    def testEmptyArray(self):
        input_arr = []
        expected = []
        actual = self.sort_func(input_arr)
        self.assertEqual(expected, actual)

    def testSortedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        expected = input_arr
        actual = self.sort_func(input_arr)
        self.assertEqual(expected, actual)

    def testReversedArray(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        input_arr = list(reversed(expected))
        actual = self.sort_func(input_arr)
        self.assertEqual(expected, actual)

    def testArrayWithDuplicates(self):
        input_arr = [10, -2, 3, 1, 101, 3, 5]
        expected = [-2, 1, 3, 3, 5, 10, 101]
        actual = self.sort_func(input_arr)
        self.assertEqual(expected, actual)


class TestQuickSortRandomized(TestQuickSort):
    def setUp(self):
        self.sort_func = lambda x: quicksort_randomized(x, False)


class TestQuickSortRandomizedMedianOf3(TestQuickSort):
    def setUp(self):
        self.sort_func = lambda x: quicksort_randomized(x, True)

if __name__ == '__main__':
    unittest.main()
