import unittest

from algorithms.lists import Node
from algorithms.trees import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def test_constructor_wraps_value_on_a_node(self):
        value = 10
        tree = BinaryTree(value)

        self.assertIs(isinstance(tree.get_root_node(), Node) is True, True)

    def test_cannot_accept_non_integer_values(self):
        with self.assertRaises(TypeError):
            tree = BinaryTree()
            tree.insert("cannot accept this.")  # pyright: ignore

            self.assertIs(isinstance(tree.get_root_node(), Node) is False, True)

    def test_insert(self):
        tree = BinaryTree()
        value = 10

        self.assertTrue(tree.insert(value), "returns True if value is inserted.")
        self.assertTrue(
            isinstance(tree._root_node, Node) is True,
            "make sure the node is really inserted.",
        )
