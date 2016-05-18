
from chained_hash import generate_hash_from_universal_set


class OpenAddressingHash:
    class Slot:
        def __init__(self, key):
            self.key = key

    occupied = Slot(None)

    def __init__(self):
        self.bits = 3
        self.hash_func = generate_hash_from_universal_set(self.bits)

        self.slots = [None for _ in range(2 ** self.bits)]
        self.filled = 0

    def rebuild(self):
        new_slots = [None for _ in range(2 * len(self.slots))]
        for slot in self.slots:
            if slot is not None and slot != OpenAddressingHash.occupied:
                self.insert(key)
        self.bits *= 2
        self.slots = new_slots

    def get_hash(self, key, step):
        h1 = self.hash_func(key, self.bits)
        if step > 0:
            h2 = 1 + key % (len(self.slots) - 1)
            h = (h1 + step * h2) % len(self.slots)
            return h
        else:
            return h1

    def insert(self, key):
        if self.get_load_factor() >= 0.9:
            self.rebuild()

        where = self.get_hash(key, 0)
        step = 1
        while step != len(self.slots):
            if self.slots[where] is None or self.slots[where] == OpenAddressingHash.occupied:
                self.slots[where] = OpenAddressingHash.Slot(key)
                self.filled += 1
                return True
            else:
                where = self.get_hash(key, step)
                step += 1

        raise RuntimeError("Hash table overflown")

    def get_load_factor(self):
        return self.filled / len(self.slots)

    def search(self, key):
        index = self.search_index(key)
        return index is not None

    def search_index(self, key):
        where = self.get_hash(key, 0)
        step = 1
        while step != len(self.slots):
            where_slot = self.slots[where]
            if where_slot is not None and \
               where_slot != OpenAddressingHash.occupied and\
               where_slot.key == key:
                return where
            elif where_slot is None:
                return None
            else:
                where = self.get_hash(key, step)
                step += 1
        return None

    def delete(self, key):
        index = self.search_index(key)
        if index is not None:
            self.slots[index] = OpenAddressingHash.occupied
            return True
        else:
            return False
