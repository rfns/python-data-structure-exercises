from copy import copy as copy_collection
from random import randint


def sort(original_collection):
    target = copy_collection(original_collection)
    cursor_position = 0
    collection_length = len(target)

    while cursor_position < collection_length:
        lowest_value_index = cursor_position
        lowest_value = None

        for i in range(cursor_position, collection_length):
            current_value = target[i]
            if lowest_value is None or current_value < lowest_value:
                lowest_value_index = i
                lowest_value = current_value

        cursor_value = target[cursor_position]

        target[cursor_position] = lowest_value
        target[lowest_value_index] = cursor_value

        cursor_position += 1

    return target


def main():
    collection = []
    for _ in range(1000):
        collection.append(randint(0, 1000))

    sorted_collection = sort(collection)
    print(sorted_collection)


main()
