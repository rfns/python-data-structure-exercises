from typing import Generic, TypeVar, Union

from ..errors import IndexOutOfBoundsError
from .node import Node, NullableNode

T = TypeVar("T")
NullableValue = Union[T, None]


class LinkedList(Generic[T]):
    def __init__(self):
        self.tail_node: NullableNode[T] = None
        self.root_node: NullableNode[T] = None
        self.size: int = 0

    def decrease_size(self):
        if self.size < 0:
            return

        self.size -= 1

    def increase_size(self):
        self.size += 1

    def first_node(self):
        return self.root_node

    def last_node(self):
        return self.tail_node

    def get_size(self):
        return self.size

    def __get_iterator__(self, reverse: bool = False):
        from .iterator import LinkedListIterator

        return LinkedListIterator[T](self, reverse)

    def get_iterator(self):
        return self.__get_iterator__()

    def get_reverse_iterator(self):
        return self.__get_iterator__(reverse=True)

    def append_node(self, node: Node[T]):
        if self.root_node is None:
            self.update_head_node(node)
            self.update_tail_node(node)
        elif self.tail_node is not None:
            self.root_node.connect(self.tail_node)
            self.tail_node.connect(node)
            self.update_tail_node(node)

        self.increase_size()

        return True

    def append_value(self, value: T) -> bool:
        node = Node(value)
        return self.append_node(node)

    def update_head_node(self, node: NullableNode):
        self.root_node = node

    def update_tail_node(self, node: NullableNode):
        self.tail_node = node

    def find_node_at(self, index: int):
        if index < 0 or index >= self.get_size():
            raise IndexOutOfBoundsError()

        iterator = self.get_iterator()

        for i in range(self.get_size()):
            iterator.next()

            if i == index:
                break

        return iterator.get_current()

    def find_at(self, index: int) -> NullableValue[T]:
        returned_node = self.find_node_at(index)
        return returned_node.get_value() if returned_node is not None else None

    def insert_at(self, index: int, value: T):
        return self.insert_node_at(index, Node(value))

    def insert_node_at(self, index: int, node: Node):
        if index > self.get_size() - 1:
            return self.append_node(node)

        reference_node = self.find_node_at(index)
        if reference_node is None:
            return False

        previous_node = reference_node.get_previous()
        next_node = reference_node.get_next()

        if index == 0:
            node.connect(reference_node)
            reference_node.connect(next_node)
            self.update_head_node(node)
        elif previous_node is not None:
            if index == self.get_size() - 1:
                node.connect(reference_node)
                previous_node.connect(node)
                self.update_tail_node(reference_node)
            else:
                node.connect(reference_node)
                previous_node.connect(node)

        self.increase_size()

        return True

    def remove_at(self, index: int = 0) -> bool:
        reference_node = self.find_node_at(index)
        if reference_node is None:
            return False

        previous_node = reference_node.get_previous()
        next_node = reference_node.get_next()

        if index == 0:
            reference_node.disconnect(next_node)
            self.update_head_node(next_node)
        elif previous_node is not None:
            if index == self.get_size() - 1:
                previous_node.disconnect(reference_node)
                self.update_tail_node(previous_node)
            elif next_node is not None:
                previous_node.connect(next_node)

        self.decrease_size()

        return True

    def print(self):
        tail_node = self.root_node

        while tail_node is not None:
            print(tail_node.get_value())
            tail_node = tail_node.get_next()
