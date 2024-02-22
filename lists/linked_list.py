class IndexOutOfBoundsError(Exception):
    def __init__(self):
        super().__init__("Index to search is out of bounds.")


class Node:
    def __init__(self, val):
        self.next: Node | None = None
        self.previous: Node | None = None
        self.value = val

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_previous(self, node):
        self.previous = node

    def get_value(self):
        return self.value

    def connect(self, node):
        if node is not None:
            self.set_next(node)
            node.set_previous(self)

    def disconnect(self, node):
        if node is not None:
            self.set_next(None)
            node.set_previous(None)


class LinkedList:
    def __init__(self):
        self.tail_node = None
        self.root_node = None
        self.size = 0

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

    def get_iterator(self):
        return LinkedListIterator(self)

    def get_reverse_iterator(self):
        return LinkedListIterator(self, True)

    def append_node(self, node: Node):
        if self.root_node is None:
            self.update_head_node(node)
            self.update_tail_node(node)
        elif self.tail_node is not None:
            self.tail_node.connect(node)
            self.update_tail_node(node)

        self.increase_size()

        return True

    def append_value(self, val):
        node = Node(val)
        self.append_node(node)

    def update_head_node(self, node):
        self.root_node = node

    def update_tail_node(self, node):
        self.tail_node = node

    def find_node_at(self, at_index) -> Node | None:
        if at_index < 0 or at_index > self.get_size():
            raise IndexOutOfBoundsError()

        iterator = self.get_iterator()

        for i in range(self.get_size()):
            iterator.next()

            if i == at_index:
                break

        return iterator.get_current()

    def find_at(self, at_index):
        return_value = self.find_node_at(at_index)
        return return_value.get_value() if return_value is not None else None

    def insert_at(self, at_index, value):
        return self.insert_node_at(at_index, Node(value))

    def insert_node_at(self, at_index, node):
        if at_index > self.get_size() - 1:
            return self.append_node(node)

        reference_node = self.find_node_at(at_index)
        if reference_node is None:
            return False

        previous_node = reference_node.get_previous()
        next_node = reference_node.get_next()

        if at_index == 0:
            node.connect(reference_node)
            reference_node.connect(next_node)
            self.update_head_node(node)
        elif previous_node is not None:
            if at_index == self.get_size() - 1:
                node.connect(reference_node)
                previous_node.connect(node)
                self.update_tail_node(reference_node)
            else:
                node.connect(reference_node)
                previous_node.connect(node)

        self.increase_size()

        return True

    def remove_at(self, at_index=0):
        reference_node = self.find_node_at(at_index)
        if reference_node is None:
            return None

        previous_node = reference_node.get_previous()
        next_node = reference_node.get_next()

        if at_index == 0:
            reference_node.disconnect(next_node)
            self.update_head_node(next_node)
        elif previous_node is not None:
            if at_index == self.get_size() - 1:
                previous_node.disconnect(reference_node)
                self.update_tail_node(previous_node)
            elif next_node is not None:
                previous_node.connect(next_node)

        self.decrease_size()

    def print(self):
        tail_node = self.root_node

        while tail_node is not None:
            print(tail_node.get_value())
            tail_node = tail_node.get_next()


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


def init():
    list = LinkedList()
    list.append_value(1)  # 0
    list.append_value(2)  # 1
    list.append_value(3)  # 2

    list.print()
    print("-----")

    list.remove_at(1)
    list.insert_at(0, 10)

    iterator = list.get_iterator()

    while iterator.next():
        print(iterator.get_value())


init()
