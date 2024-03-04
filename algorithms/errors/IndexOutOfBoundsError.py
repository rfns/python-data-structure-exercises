class IndexOutOfBoundsError(Exception):
    def __init__(self):
        super().__init__("Index to search is out of bounds.")
