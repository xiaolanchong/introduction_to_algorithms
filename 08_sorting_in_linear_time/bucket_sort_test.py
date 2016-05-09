import unittest
from bucket_sort import bucket_sort


class TestCountingSort(unittest.TestCase):
    def testSimpleArray(self):
        input_arr = [0x13, 0x62, 0x21, 0x1f, 0x62, 0x1160, 0xd]
        expected = [0x1160, 0x21, 0x62, 0x62, 0x13, 0xd, 0x1f]
        actual = counting_sort(input_arr, 16, lambda x: x & 0xf)
        self.assertEqual(expected, actual)


class TestRadixSort(unittest.TestCase):
    def setUp(self):
        self.min = -200
        self.max = 300
        self.bucket_number = 10

    def call_bucket_sort(self, arr):
        return bucket_sort(arr, self.min, self.max, self.bucket_number)

    def testSimpleArray(self):
        input_arr = [10, 202, 3, 1, -101, 5, 101]
        expected = sorted(input_arr)
        actual = self.call_bucket_sort(input_arr)
        self.assertEqual(expected, actual)

    def testEmptyArray(self):
        input_arr = []
        expected = []
        actual = self.call_bucket_sort(input_arr)
        self.assertEqual(expected, actual)

    def testSortedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        expected = input_arr
        actual = self.call_bucket_sort(input_arr)
        self.assertEqual(expected, actual)

    def testReversedArray(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        input_arr = list(reversed(expected))
        actual = self.call_bucket_sort(input_arr)
        self.assertEqual(expected, actual)

    def testArrayWithDuplicates(self):
        input_arr = [10, 202, 3, 1, 101, 3, 5]
        expected = sorted(input_arr)
        actual = self.call_bucket_sort(input_arr)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
