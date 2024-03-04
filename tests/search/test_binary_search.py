import unittest

from algorithms.search import binary


class TestIterativeBinarySearch(unittest.TestCase):
    def test_find_match_if_exists(self):
        data = [-20, -10, 0, 1, 6, 8, 10, 40, 100, 250, 300, 500]

        self.assertEqual(
            binary.search_iterated(data, data[2]), 2, "returns the 2nd index"
        )
        self.assertEqual(
            binary.search_iterated(data, data[6]), 6, "returns the 6th index"
        )
        self.assertEqual(
            binary.search_iterated(data, data[9]), 9, "returns the 9th index"
        )

    def test_returns_none_if_no_match(self):
        data = [1, 6, 8, 10, 40, 100, 250, 300, 500]

        self.assertEqual(binary.search_iterated(data, -2), None, "returns None")


class TestRecursiveBinarySearch(unittest.TestCase):
    def test_find_match_if_exists(self):
        data = [-20, -10, 0, 1, 6, 8, 10, 40, 100, 250, 300, 500]

        self.assertEqual(
            binary.search_recursive(data, data[2]), 2, "returns the 2nd index"
        )
        self.assertEqual(
            binary.search_recursive(data, data[6]), 6, "returns the 6th index"
        )
        self.assertEqual(
            binary.search_recursive(data, data[9]), 9, "returns the 9th index"
        )

    def test_returns_none_if_no_match(self):
        data = [1, 6, 8, 10, 40, 100, 250, 300, 500]

        self.assertEqual(binary.search_recursive(data, -2), None, "returns None")
