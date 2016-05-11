

class DoublyLinkedList:
    """Doubly linked list with a sentined at the beginning"""
    class Node:
        def __init__(self, value, prev_item, next_item):
            self.value = value
            self.prev = prev_item
            self.next = next_item

    def __init__(self):
        self.nil = DoublyLinkedList.Node(None, None, None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert_beginning(self, value):
        old_next = self.nil.next
        new_node = DoublyLinkedList.Node(value, self.nil, self.nil.next)
        self.nil.next = new_node
        old_next.prev = new_node

    def delete(self, node):
        assert(node != self.nil)
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def search(self, value):
        item = self.begin()
        while item != self.end():
            if item.value == value:
                return item
            item = item.next
        return None

    def begin(self):
        """Gets a reference to the 1st list item"""
        return None if self.nil.next == self.nil else self.nil.next

    def end(self):
        """Gets a reference to the item after the last one of the list (sentinel)"""
        return self.nil

