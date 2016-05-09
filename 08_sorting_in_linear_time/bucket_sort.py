
import math
from itertools import chain


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] >= key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key


def bucket_sort(a_arr, a, b, n):
    assert(a < b)
    assert(n > 2)

    def bucket_map(value):
        return math.floor(n * (value - a) / (b - a))

    b_arr = list([] for _ in range(n))

    for item in a_arr:
        bucket_number = bucket_map(item)
        b_arr[bucket_number].append(item)

    for item in b_arr:
        insertion_sort(item)

    return list(chain.from_iterable(b_arr))
