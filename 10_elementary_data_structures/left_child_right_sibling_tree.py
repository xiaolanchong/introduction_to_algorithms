
class LeftChildRightSiblingTree:
    class Node:
        def __init__(self, parent, value):
            self.parent = parent
            self.left_child = None
            self.right_sibling = None
            self.value = value

    def __init__(self):
        self.root = None

    def insert_child(self, parent, value):
        if parent is None:
            new_node = LeftChildRightSiblingTree.Node(None, value)
            self.root = new_node
            return new_node
        elif parent.left_child is None:
            new_node = LeftChildRightSiblingTree.Node(parent, value)
            parent.left_child = new_node
            return new_node
        else:
            return self.insert_sibling(parent.left_child, value)

    def insert_sibling(self, node, value):
        assert(node is not None)
        new_node = LeftChildRightSiblingTree.Node(node.parent, value)
        where = node
        while where.right_sibling is not None:
            where = where.right_sibling
        where.right_sibling = new_node
        return node

    def iterate(self, visitor):
        LeftChildRightSiblingTree.iterate_in_depth(self.root, visitor)

    @staticmethod
    def iterate_in_depth(node, visitor):
        if node.left_child is not None:
            visitor.visit_start(node)
            LeftChildRightSiblingTree.iterate_in_depth(node.left_child, visitor)
            visitor.visit_end(node)
        else:
            visitor.visit_leaf(node)

        if node.right_sibling is not None:
            LeftChildRightSiblingTree.iterate_in_depth(node.right_sibling, visitor)
