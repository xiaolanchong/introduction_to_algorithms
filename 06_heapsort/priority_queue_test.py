import unittest
import operator
from binary_heap import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.key = operator.itemgetter(0)

    def testPriorityQueueOperations(self):
        queue = PriorityQueue([], self.key)
        task1 = (6, 'task1')
        task2 = (16, 'task2')
        task3 = (8, 'task3')
        queue.insert(task1)

        queue.insert(task2)
        self.assertEqual(task2, queue.maximum())

        queue.insert(task3)
        self.assertEqual(task2, queue.maximum())

        queue.extract_maximum()
        self.assertEqual(task3, queue.maximum())

        queue.extract_maximum()
        self.assertEqual(task1, queue.maximum())


if __name__ == '__main__':
    unittest.main()