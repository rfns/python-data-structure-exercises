import unittest

from algorithms.search import quickselect


class TestQuickSelect(unittest.TestCase):
    def test_find_smallest_k(self):
        data = [1, 8, -2, 3, 6, 0, 10, -5, 3]
        self.assertEqual(quickselect.findKthest(data, 0), -5, "returns -5")

    def test_find_largest_k(self):
        data = [1, 8, -2, 3, 6, 0, 10, -5, 3]
        largestK = len(data) - 1
        self.assertEqual(quickselect.findKthest(data, largestK), 10, "returns 10")

    def test_find_first_kth_duplicate(self):
        data = [1, 8, -2, 3, 6, 6, 0, 10, -5, 3]
        kthest = 4
        self.assertEqual(quickselect.findKthest(data, kthest), 3, "returns 3")

    def test_enforces_lowest_value_if_kthest_lower_than_zero(self):
        data = [1, 8, -2, 3, 6, 6, 0, 10, -5, 3]
        kthest = -1

        self.assertEqual(quickselect.findKthest(data, kthest), -5, "returns -5")

    def test_enforces_highest_value_if_kthest_higher_than_max_length(self):
        data = [1, 8, -2, 3, 6, 6, 0, 10, -5, 3]
        kthest = 20

        self.assertEqual(quickselect.findKthest(data, kthest), 10, "returns 10")
