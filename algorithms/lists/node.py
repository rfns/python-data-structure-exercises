from typing import Generic, TypeVar, Union

T = TypeVar("T")
NullableNode = Union["Node[T]", None]


class Node(Generic[T]):
    def __init__(self, value: T):
        self.next: NullableNode = None
        self.previous: NullableNode = None
        self.value = value

    def set_next(self, node: NullableNode):
        self.next = node

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_previous(self, node: NullableNode):
        self.previous = node

    def get_value(self) -> T:
        return self.value

    def connect(self, node: NullableNode):
        if node is not None:
            self.set_next(node)
            node.set_previous(self)

    def disconnect(self, node: NullableNode):
        if node is not None:
            self.set_next(None)
            node.set_previous(None)
