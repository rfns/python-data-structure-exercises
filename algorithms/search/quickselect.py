from algorithms.sorting.quicksort import do_hoare_partition


def findKthest(list: list[int], k: int) -> int:
    """Returns the kthest element from an array.

    Assuming that the following input is provided:

    ::
        input = [1,7,-3]
        k = 0
        quickselect.findKthest(input, k)

    Should return -3 because 0 represents the lowest and the lowest value found is -3.

    If you provide the highest index, it'll result the algorithm on returning the highest value found.
    """

    def search(start, end):
        if start == end:
            return list[start]

        pivot = do_hoare_partition(list, start, end)

        if pivot < k:
            return search(pivot + 1, end)
        if pivot > k:
            return search(start, pivot)

        return list[k]

    return search(0, len(list) - 1)
