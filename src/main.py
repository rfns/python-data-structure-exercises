from playground import run_search_algorithms, run_sort_algorithms


def start(unsorted_array):
    run_searching_algorithms()
    run_sorting_algorithms()


def run_search_algorithms(array_to_search):
    print(f"Search in array: {array_to_search}")

    match = linear_search.search(array_to_search)
    print(f"Term found: {match}")


if __name__ == "__main__":
    start([6, 4, 1, 9])
