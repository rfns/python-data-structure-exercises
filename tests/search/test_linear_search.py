import unittest

from algorithms.search import linear


class TestLinearSearch(unittest.TestCase):
    def test_search_should_return_index_if_match(self):
        self.assertEqual(linear.search(["My", "First", "Python", "Test"], "Python"), 2)

    def test_search_should_return_first_matching_index_if_not_exclusive(self):
        self.assertNotEqual(
            linear.search(
                [
                    "My",
                    "First",
                    "Python",
                    "Python",
                    "Test",
                ],
                "Python",
            ),
            3,
        )

    def test_search_should_return_none_if_no_match(self):
        self.assertEqual(linear.search(["find", "me", "here"], "not"), None)

    def test_search_should_raise_type_error_exception_if_first_arg_is_not_list(self):
        self.assertRaises(TypeError, lambda _: linear.search("not a list", "value to search"))  # type: ignore


if __name__ == "__main__":
    unittest.main()
