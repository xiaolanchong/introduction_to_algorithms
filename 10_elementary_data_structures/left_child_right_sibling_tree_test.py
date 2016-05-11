
import unittest
from left_child_right_sibling_tree import LeftChildRightSiblingTree


class StringConverter:
    def __init__(self):
        self.level = 0
        self.str_tree = ''
        self.first_child = True

    def visit_start(self, node):
        self.level += 1
        self.str_tree += str(node.value) + ' ['
        self.first_child = True

    def visit_end(self, node):
        self.level -= 1
        self.str_tree += ']'

    def visit_leaf(self, node):
        if not self.first_child:
            self.str_tree += ', '
        else:
            self.first_child = False
        self.str_tree += str(node.value)


def to_string(tree):
    visitor = StringConverter()
    tree.iterate(visitor)
    return visitor.str_tree


class TestLeftChildRightSiblingTree(unittest.TestCase):
    def testInsertion(self):
        tree = LeftChildRightSiblingTree()
        root = tree.insert_child(None, 5)
        ch1 = tree.insert_child(root, 17)
        tree.insert_sibling(ch1, 18)

        actual = to_string(tree)
        expected = '5 [17, 18]'
        self.assertEqual(expected, actual)

        tree.insert_child(ch1, 22)
        tree.insert_child(ch1, 25)

        actual = to_string(tree)
        expected = '5 [17 [22, 25], 18]'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
