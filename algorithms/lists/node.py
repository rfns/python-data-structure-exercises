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
