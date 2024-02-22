from copy import copy as copy_collection
from random import randint


def sort(original_collection):
    target = copy_collection(original_collection)
    bubble_index = len(target)

    while bubble_index is not 0:
        for current_index in range(1, bubble_index):
            previous_index = current_index - 1

            current_value = target[current_index]
            previous_value = target[previous_index]

            if previous_value > current_value:
                target[current_index] = previous_value
                target[previous_index] = current_value

        bubble_index -= 1

    return target


def main():
    collection = []
    # collection = [1, 7, 3, 6, 4, 0, 10]
    for _ in range(1000):
        collection.append(randint(0, 1000))

    sorted_collection = sort(collection)
    print(sorted_collection)


main()
