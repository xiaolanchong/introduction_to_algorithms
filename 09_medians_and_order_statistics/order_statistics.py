import random


random.seed()


def order_statistics(arr, i):
    return randomized_select(arr, 0, len(arr) - 1, i)


def partition(arr, p, r):
    """Divides arr[p:r+1] into 2 parts, the partition item is the last item"""
    x = arr[r]
    i = p - 1
    # arr[k] <= x for k in [p..i]
    # arr[k] > x  for k in [i..j]
    # not processed yet if k in [j..r]
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def randomized_partition(arr, p, r):
    """Divides arr into 2 parts, the partition item is selected randomly"""
    rand_index = random.randint(p, r)
    arr[rand_index], arr[p] = arr[rand_index], arr[p]
    return partition(arr, p, r)


def randomized_select(arr, p, r, i):
    """Selects the i-th statistics from arr[p:r+1]"""
    if p > r:
        return None
    elif p == r:
        return arr[p]

    q = randomized_partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[k - 1]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    else:
        return randomized_select(arr, q + 1, r, i - k)
