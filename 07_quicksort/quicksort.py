
import random


def quicksort(arr):
    """Sorts the input array with quick (classic Hoar's) sorting algorithm"""
    copy_arr = arr.copy()
    quicksort_range(copy_arr, 0, len(copy_arr) - 1)
    return copy_arr


def partition(arr, p, r):
    """Hoar's partition routine"""
    x = arr[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if arr[j] <= x:
                break

        while True:
            i += 1
            if arr[i] >= x:
                break

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j


def quicksort_range(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort_range(arr, p, q)
        quicksort_range(arr, q + 1, r)


# Randomized quick sorting

def get_random_index(_, p, r):
    return random.randint(p, r)


def get_median_of_3_index(arr, p, r):
    """Gets the median of 3 randomly selected distinct elements of the array"""
    if r == p or r == p + 1:
        return r

    first = random.randint(p, r)
    second = random.randint(p, r)
    third = random.randint(p, r)

    while second == first or second == third:
        second = random.randint(p, r)

    while third == first or third == second:
        third = random.randint(p, r)

    if arr[first] < arr[second]:
        if arr[second] < arr[third]:
            return second
        elif arr[first] < arr[third]:
            return third
        else:
            return first
    else:
        if arr[first] < arr[third]:
            return first
        elif arr[second] < arr[third]:
            return third
        else:
            return second


def quicksort_randomized(arr, is_median_of_3):
    """Sorts the input array with quick (classic Hoar's) sorting algorithm with a randomized enhancement"""
    copy_arr = arr.copy()
    get_partition_index_func = get_median_of_3_index if is_median_of_3 else get_random_index
    quicksort_range_randomized(copy_arr, 0, len(copy_arr) - 1, get_partition_index_func)
    return copy_arr


def partition_randomized(arr, p, r, get_partition_index_func):
    """Same as the partition routine above, but the partition item is selected by the given routine"""
    rand_index = get_partition_index_func(arr, p, r)
    arr[rand_index], arr[p] = arr[rand_index], arr[p]
    return partition(arr, p, r)


def quicksort_range_randomized(arr, p, r, get_partition_index_func):
    if p < r:
        q = partition_randomized(arr, p, r, get_partition_index_func)
        quicksort_range_randomized(arr, p, q, get_partition_index_func)
        quicksort_range_randomized(arr, q + 1, r, get_partition_index_func)