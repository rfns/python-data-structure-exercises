from typing import Generic, TypeVar

from .linked_list import LinkedList, NullableValue
from .node import NullableNode

T = TypeVar("T")


class LinkedListIterator(Generic[T]):
    def __init__(self, list: "LinkedList", reverse=False):
        self.list = list
        self.tail_node: NullableNode = None
        self.reverse = reverse

    def next(self):
        if self.tail_node is None:
            self.tail_node = (
                self.list.first_node()
                if self.reverse is False
                else self.list.last_node()
            )
        else:
            self.tail_node = (
                self.tail_node.get_next()
                if self.reverse is False
                else self.tail_node.get_previous()
            )

        return self.tail_node is not None

    def get_value(self) -> NullableValue[T]:
        if self.tail_node is not None:
            return self.tail_node.get_value()
        return None

    def get_current(self) -> NullableNode:
        return self.tail_node
