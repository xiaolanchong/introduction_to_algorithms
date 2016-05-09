

class BinaryHeap:
    """"Binary heap is an array with the item property:
        For each i in 1..heap size the following is true:
        the element with index i (called the parent) is greater than
        those with indices 2*i (the left child) and 2*i+1 (the right child).
        Both of the children may not exist."""
    def __init__(self, items=[], key=lambda x: x):
        """items - initial heap items,
           key - function to extract the item key to compare items with each other"""
        self.items = []
        self.size = 0
        self.key = key
        self.build_heap(items)

    def parent(self, index):
        """Gets the index of the parent.
        Note: index starts with 1."""
        parent_index = index // 2
        return parent_index

    def left(self, index):
        """Gets the index of the left child of the node with the given index.
        Note: index starts with 1."""
        return 2 * index

    def right(self, index):
        """Gets the index of the left child of the node with the given index.
        Note: index starts with 1."""
        return self.left(index) + 1

    def get_item(self, index):
        """Gets the item with the given index.
           Note: index starts with 1."""
        if index > self.heap_size():
            raise IndexError('{0} is out range [1..{1}]', index, self.heap_size())
        return self.items[index - 1]

    def heap_size(self):
        """Gets the size of the heap - the number of actual elements stored in self.items"""
        return self.size

    def exchange_items(self, first, second):
        """Exchange 2 elements with the given indices in the heap.
           Note: indices start with 1."""
        self.items[first - 1], self.items[second - 1] = self.items[second - 1], self.items[first - 1]

    def heapify(self, index):
        """Ensures the heap order is preserved for the item with the given and all greater indices"""
        l = self.left(index)
        r = self.right(index)

        index_key = self.key(self.get_item(index))
        if l <= self.heap_size() and self.key(self.get_item(l)) > index_key:
            largest = l
        else:
            largest = index
        largest_key = self.get_item(largest)
        if r <= self.heap_size() and self.key(self.get_item(r)) > largest_key:
            largest = r

        if largest != index:
            self.exchange_items(largest, index)
            self.heapify(largest)

    def build_heap(self, items):
        """"Builds the heap from the given list"""
        self.items = items
        self.size = len(items)
        for i in range(self.heap_size() // 2, 0, -1):
            self.heapify(i)


class PartialBinaryHeap(BinaryHeap):
    def __init__(self, arr, key):
        """arr - initial heap items,
           key - function to extract the item key to compare items with each other"""
        super().__init__(arr, key)

    def decrease_size(self):
        """Decrease the size of the heap"""
        self.size -= 1

    def increase_size(self):
        """Increases the size of the heap with None item"""
        if len(self.items) == self.size:
            self.items.append(None)
        self.size += 1

    def set_item(self, index, value):
        """Sets the value of the item with the given index.
           Nte: index starts with 1."""
        if index > self.heap_size():
            raise IndexError('{0} is out range [1..{1}]', index, self.heap_size())
        self.items[index - 1] = value


class PriorityQueue(PartialBinaryHeap):
    def __init__(self, arr, key):
        """arr - initial heap items,
           key - function to extract the item key to compare items with each other"""
        super().__init__(arr, key)

    def insert(self, item):
        """Inserts a new element in the queue"""
        self.increase_size()
        i = self.heap_size()
        while i > 1 and self.key(self.get_item(self.parent(i))) < self.key(item):
            self.set_item(i, self.get_item(self.parent(i)))
            i = self.parent(i)
        self.set_item(i, item)

    def maximum(self):
        """"Gets the max element (with the most priority) of the heap"""
        if self.heap_size() == 0:
            raise RuntimeError('No element in the heap')
        return self.get_item(1)

    def extract_maximum(self):
        """"Pops the max element of the queue"""
        max_item = self.maximum()
        last_item = self.get_item(self.heap_size())
        self.set_item(1, last_item)
        self.decrease_size()
        self.heapify(1)
        return max_item


def heapsort(arr):
    """Sorts the given array by ascending order and returns its sorted copy. E.g. [10, 1, 3] -> [1, 3, 10]"""
    heap = PartialBinaryHeap(arr, lambda x: x)
    for i in range(heap.heap_size(), 1, -1):
        heap.exchange_items(1, i)
        heap.decrease_size()
        heap.heapify(1)
    return heap.items
