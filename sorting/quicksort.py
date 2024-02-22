class Sort:
    def _quicksort(self, array: list, low: int, high: int) -> None:
        if low < high:
            pivot = self._partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)

    def _partition(self, array: list, low: int, high: int) -> int:
        pivot = array[(high + low) // 2]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]

    def sort(self, array: list) -> list:
        self._quicksort(array, 0, len(array) - 1)
        return array


arr = [1, 7, 2, 6, 1, 9, 15, 11, 3, 30, 21, -5, -3, 12]
Sort().sort(arr)

print(arr)
