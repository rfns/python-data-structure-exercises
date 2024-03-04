from .linked_list import LinkedList
from .node import Node


class LinkedListIterator:
    def __init__(self, list: LinkedList, reverse=False):
        self.list = list
        self.tail_node: Node | None = None
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

    def get_value(self) -> str:
        if self.tail_node is not None:
            return self.tail_node.get_value()
        return ""

    def get_current(self) -> Node | None:
        return self.tail_node
