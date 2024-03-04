from typing import Any

from ..lists.node import Node


def wrap_value(value: int):
    if isinstance(value, Node) is True:
        return value

    return Node(value)


class BinaryTree:
    def __init__(self, root: Node | int | None = None) -> None:
        self._root_node = None

        if isinstance(root, int):
            self.insert(root)

    def get_root_node(self):
        return self._root_node

    def insert(self, value: int) -> bool:
        if isinstance(value, int) is not True:
            raise TypeError("Tree can only accept integer values.")

        self._root_node = wrap_value(value)
        return True
