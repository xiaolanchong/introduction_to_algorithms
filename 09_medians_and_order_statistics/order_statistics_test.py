import unittest
from order_statistics import order_statistics


class TestOrderStatistics(unittest.TestCase):
    def testSimpleArray(self):
        input_arr = [10, 202, 3, 1, -101, 5, 101]
        statistics_number = 3
        expected = sorted(input_arr)[statistics_number - 1]
        actual = order_statistics(input_arr, statistics_number)
        self.assertEqual(expected, actual)

    def testEmptyArray(self):
        input_arr = []
        self.assertIsNone(order_statistics(input_arr, 0))
        self.assertIsNone(order_statistics(input_arr, 3))

    def testSortedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        statistics_number = 4
        expected = input_arr[statistics_number - 1]
        actual = order_statistics(input_arr, statistics_number)
        self.assertEqual(expected, actual)

    def testReversedArray(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        input_arr_reversed = list(reversed(input_arr))
        statistics_number = 4
        expected = input_arr[statistics_number - 1]
        actual = order_statistics(input_arr_reversed, statistics_number)
        self.assertEqual(expected, actual)

    def testArrayWithDuplicates(self):
        input_arr = [10, 202, 3, 1, 101, 3, 5]
        statistics_number = 4
        expected = sorted(input_arr)[statistics_number - 1]
        actual = order_statistics(input_arr, statistics_number)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()