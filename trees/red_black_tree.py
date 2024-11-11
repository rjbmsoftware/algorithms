import unittest
from enum import StrEnum, auto


class Colour(StrEnum):
    RED = auto()
    BLACK = auto()


class ColourNode:

    def __init__(self, value, colour, left_node, right_node):
        self.value = value
        self.colour: Colour = colour
        self.left_node = left_node
        self.right_node = right_node

    @property
    def colour(self):
        return self.colour

    @colour.setter
    def colour(self, colour: Colour):
        self.colour = colour

    @property
    def value(self) -> Colour:
        return self.value

    @value.setter
    def value(self, value):
        self.value = value

    @property
    def left(self):
        return self.left

    @left.setter
    def left(self, new_left):
        self.left = new_left


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
