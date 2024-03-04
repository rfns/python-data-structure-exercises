from math import floor


def search_recursive(collection, term, start=0, end=None):
    if end == None:
        end = len(collection)

    mid = floor((start + end) / 2)
    mid_value = collection[mid]

    if term == mid_value:
        return mid

    if mid == 0:
        return None

    if mid_value > term:
        end = mid
    elif mid_value < term:
        start = mid

    return search_recursive(collection, term, start, end)


def search_iterated(collection, term):
    start = 0
    end = len(collection)
    mid = floor((start + end) / 2)
    mid_value = collection[mid]

    while True:
        mid = floor((start + end) / 2)
        mid_value = collection[mid]

        if term == mid_value:
            return mid
        if mid == 0:
            return None

        if mid_value > term:
            end = mid
        elif mid_value < term:
            start = mid
