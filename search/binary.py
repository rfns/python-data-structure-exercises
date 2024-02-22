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


def main():
    collection = []
    for value in range(1000000):
        collection.append(value)
    # collection = [1, 5, 8, 9, 13, 17, 20, 26, 23]

    print(search_recursive(collection, 500))
    print(search_iterated(collection, 672))


main()
