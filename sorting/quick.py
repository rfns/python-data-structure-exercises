from copy import copy
from random import randint, sample


def hoare(working_list, low, high):
    # pivot_index = floor((low + high) / 2)
    pivot_index = randint(low, high)
    pivot_value = working_list[pivot_index]

    # Precisa aumentar a range porque os indices são calculados antes de realizar a aritmética.
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


def sort(unsorted_list, partion_scheme=hoare, immutable=False):
    working_list = unsorted_list
    if immutable is True:
        working_list = copy(unsorted_list)

    last_index = len(working_list) - 1

    def quicksort(start=0, end=last_index):
        if (end - start) <= 0:
            return

        offset = partion_scheme(working_list, start, end)

        quicksort(start, offset)
        quicksort(offset + 1, end)

    quicksort(0, last_index)

    return working_list


def main():
    # collection = sample(range(-100, 100), 199)
    collection = [1, 7, 2, 6, 1, 9, 15, 11, 3, 30, 21, -5, -3, 12]
    # collection = [1, 5, 3, 6, 4, 7, 2]
    # collection = [1, 7, 3, 5, 6]
    print(sort(collection, hoare, False))


#
#
main()
