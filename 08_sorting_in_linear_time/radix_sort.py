

def radix_sort(arr):
    """"""
    copy_arr = arr.copy()
    bits_in_digit = 4
    max_bits = 32
    for digit_number in range(0, max_bits // bits_in_digit + 1):
        copy_arr = radix_digit_sort(copy_arr, bits_in_digit, digit_number)
    return copy_arr


def radix_digit_sort(arr, bits_in_digit, digit_number):
    def get_key(item):
        return (item >> (bits_in_digit * digit_number)) & (2 ** bits_in_digit - 1)
    return counting_sort(arr, 2 ** bits_in_digit, get_key)


class HelperArrayItem:
    def __init__(self):
        self.elements_not_greater = 0
        self.same_key_items = []

    def __repr__(self):
        return '({}, {})'.format(self.elements_not_greater, self.same_key_items)


def counting_sort(a_arr, a_arr_max, key_func):
    b_arr = [0] * len(a_arr)
    c_arr = [HelperArrayItem() for _ in range(a_arr_max)]

    for a_item in a_arr:
        key_to_sort = key_func(a_item)
        c_arr[key_to_sort].same_key_items.append(a_item)
        c_arr[key_to_sort].elements_not_greater += 1

    for i in range(1, len(c_arr)):
        c_arr[i].elements_not_greater += c_arr[i - 1].elements_not_greater

    for a_arr_item in a_arr[::-1]:
        key_to_sort = key_func(a_arr_item)
        where_to_place = c_arr[key_to_sort].elements_not_greater
        b_arr[where_to_place - 1] = c_arr[key_to_sort].same_key_items.pop()
        c_arr[key_to_sort].elements_not_greater -= 1

    return b_arr
