import unittest

from search import linear


class TestLinearSearch(unittest.TestCase):
    def test_search_should_return_index_if_match(self):
        self.assertEquals(linear.search(["My", "First", "Python", "Test"], "Python"), 2)

    def test_search_should_return_none_if_no_match(self):
        self.assertEquals(linear.search(["find", "me", "here"], "not"), None)

    def test_search_should_raise_type_error_exception_if_first_arg_is_not_list(self):
        self.assertRaises(linear.search("not a list", "value to search"), TypeError)
