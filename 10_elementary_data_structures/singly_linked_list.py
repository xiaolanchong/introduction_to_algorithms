

class SinglyLinkedList:
    class Node:
        def __init__(self, value, next_item):
            self.next = next_item
            self.value = value

    def __init__(self):
        self.head = None

    def insert_after(self, where, value):
        if where is None:
            new_node = SinglyLinkedList.Node(value, self.head)
            self.head = new_node
        else:
            new_node = SinglyLinkedList.Node(value, where.next)
            where.next = new_node
        return new_node

    def delete_after(self, where):
        if where is None:
            if self.head is not None:
                self.head = self.head.next
        elif where.next is not None:
            where.next = where.next.next

    def iterate(self, func):
        p = self.head
        while p is not None:
            if not func(p.value):
                return
            p = p.next

    def reverse(self):
        new_head = None
        head = self.head
        while head is not None:
            next_item = head.next
            head.next = new_head
            new_head = head
            head = next_item

        self.head = new_head

