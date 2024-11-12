import unittest
from enum import StrEnum, auto


class Colour(StrEnum):
    RED = auto()
    BLACK = auto()


class ColourNode:

    def __init__(self, value, colour, left_node, right_node):
        self._value = value
        self._colour: Colour = colour
        self._left_node = left_node
        self._right_node = right_node

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour: Colour):
        self._colour = colour

    @property
    def value(self) -> Colour:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left_node

    @left.setter
    def left(self, new_left):
        self._left_node = new_left

    @property
    def right(self):
        return self._right_node

    @right.setter
    def right(self, new_right):
        self._right_node = new_right


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
    def root(self) -> ColourNode:
        return self._root

    @root.setter
    def root(self, node: ColourNode) -> None:
        self._root = node

    def insert(self, value) -> None:
        """
        Rules
         1. if tree is empty create new node as root node with the colour black
        """
        if self.root is None:
            self.root = ColourNode(value, Colour.BLACK, None, None)

    def delete(self, value) -> None:
        pass


class TestRedBlackTree(unittest.TestCase):

    def test_insert_root_node_only(self):
        tree = RedBlackTree()
        tree.insert(10)
        self.assertEqual(tree.root.colour, Colour.BLACK)


if __name__ == "__main__":
    unittest.main()
