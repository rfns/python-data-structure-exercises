from copy import copy
from math import floor
from random import randint


def do_hoare_partition(working_list, low, high):
    pivot_index = floor((low + high) / 2)
    # pivot_index = randint(low, high)
    pivot_value = working_list[pivot_index]

    # Must include boundaries as they get increased/decreased before the actual check.
    left_cursor_index = low - 1
    right_cursor_index = high + 1

    while True:
        left_cursor_index += 1
        right_cursor_index -= 1

        while working_list[left_cursor_index] < pivot_value:
            left_cursor_index += 1

        while working_list[right_cursor_index] > pivot_value:
            right_cursor_index -= 1

        if left_cursor_index >= right_cursor_index:
            return right_cursor_index

        working_list[left_cursor_index], working_list[right_cursor_index] = (
            working_list[right_cursor_index],
            working_list[left_cursor_index],
        )


def sort(collection: list, immutable=False) -> list:
    working_list = collection
    if immutable is True:
        working_list = copy(collection)

    last_index = len(working_list) - 1

    def quicksort(start=0, end=last_index):
        if (end - start) <= 0:
            return

        offset = do_hoare_partition(working_list, start, end)

        quicksort(start, offset)
        quicksort(offset + 1, end)

    quicksort(0, last_index)

    return working_list
