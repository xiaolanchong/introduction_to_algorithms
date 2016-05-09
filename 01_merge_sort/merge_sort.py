def merge_sort(arr):
    """Sorts the input array A with merge sorting algorithm"""
    copy_arr = arr.copy()
    merge_sort_range(copy_arr, 0, len(copy_arr) - 1)
    return copy_arr


def merge_sort_range(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_range(arr, p, q)
        merge_sort_range(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    arr_result = [0] * (r - p + 1)
    index_left = p
    index_right = q + 1
    index_final = 0
    while (index_left <= q and
           index_right <= r):
        if arr[index_left] <= arr[index_right]:
            arr_result[index_final] = arr[index_left]
            index_left += 1
        else:
            arr_result[index_final] = arr[index_right]
            index_right += 1
        index_final += 1

    if index_left <= q:
        arr_result[index_final:] = arr[index_left:(q + 1)]
    elif index_right <= r:
        arr_result[index_final:] = arr[index_right:(r + 1)]

    arr[p:r + 1] = arr_result
