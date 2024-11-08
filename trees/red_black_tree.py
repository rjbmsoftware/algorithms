import unittest


class RedBlackTree:
    """
    Implementation of red black trees

    self balancing binary search tree
    not strictly height balanced like an AVL tree
    less rotations compared to AVL for faster inserts and deletes
    search can take longer as it is not strictly height balanced
    """

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, value) -> None:
        pass

    def delete(self, value) -> None:
        pass


class TestRedBlackTree(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
