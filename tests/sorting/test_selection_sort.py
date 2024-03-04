import unittest

from algorithms.sorting import selectionsort


class TestSelectionSort(unittest.TestCase):
    def test_order_matches_expected(self):
        data = [-9, 4, 1, -5, 3, 10, 3]
        expected = [-9, -5, 1, 3, 3, 4, 10]

        self.assertEqual(selectionsort.sort(data), expected, "returns the sorted list")
