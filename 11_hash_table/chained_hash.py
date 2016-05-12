
import random


random.seed()


def knuth_hash(key, bits):
    """Gets the N most significant bits of the 32 bits value:
    the product of a and key, where a = 2^32 * (sqrt(5)-1)/2.
    The solution is proposed by D. Knuth"""
    a = 2654435769
    h = ((a * key) >> (32 - bits)) & ((1 << bits) - 1)
    return h


def generate_hash_from_universal_set(_):
    """"Randomly generates a hash function from the universal hash set"""
    p_arr = [1151, 7879, 23197, 85931]
    p = p_arr[-1]
    a = random.randint(0, p-1)
    b = random.randint(1, p-1)
    return lambda x, bits: ((a * x + b) % p) % (2 ** bits - 1)


class ChainedHash:
    """Hash table where collisions are resolved with chains (item lists)"""
    def __init__(self, hash_from_universal_set=True, bits=5):
        self.bits = bits
        self.buckets = list([] for _ in range(2 ** self.bits))
        self.hash_func = generate_hash_from_universal_set(self.bits) if hash_from_universal_set else knuth_hash
        self.size = 0
        self.has_collision = False

    def get_bucket(self, key):
        return self.hash_func(key, self.bits)

    def insert(self, key):
        self.size += 1
        bucket_num = self.get_bucket(key)
        bucket = self.buckets[bucket_num]
        if not self.has_collision and len(bucket):
            self.has_collision = True
        bucket.append(key)

    def search(self, key):
        bucket_num = self.get_bucket(key)
        bucket = self.buckets[bucket_num]
        for key_in_bucket in bucket:
            if key_in_bucket == key:
                return True
        return False

    def delete(self, key):
        bucket_num = self.get_bucket(key)
        bucket = self.buckets[bucket_num]
        for index, key_in_bucket in enumerate(bucket):
            if key_in_bucket == key:
                del bucket[index]
                return True
        return False
