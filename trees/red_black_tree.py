from typing import Self
import unittest
from enum import StrEnum, auto


class Colour(StrEnum):
    RED = auto()
    BLACK = auto()


class ColourNode:

    def __init__(self, value, colour, left_node: Self | None = None, right_node: Self | None = None):
        self._value = value
        self._colour: Colour = colour
        self._left_node: ColourNode = left_node
        self._right_node: ColourNode = right_node

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
    def left(self) -> Self | None:
        return self._left_node

    @left.setter
    def left(self, new_left):
        self._left_node = new_left

    @property
    def right(self) -> Self | None:
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
         1. if tree is empty create new black node as the root node
         2. if tree is not empty create a new red leaf node
        """
        if self.root is None:
            self.root = ColourNode(value, Colour.BLACK)
            return

        new_node = ColourNode(value, Colour.RED)
        working_node = self.root

        while working_node:
            if working_node.value >= value:
                if working_node.left is None:
                    working_node.left = new_node
                    break

                working_node = working_node.left
            else:
                if working_node.right is None:
                    working_node.right = new_node
                    break

                working_node = working_node.right

    def delete(self, value) -> None:
        pass


class TestRedBlackTree(unittest.TestCase):

    def test_insert_root_node_only(self):
        tree = RedBlackTree()
        tree.insert(10)
        self.assertEqual(tree.root.colour, Colour.BLACK)

    def test_insert_second_node_red(self):
        tree = RedBlackTree()

        child_value = 18
        tree.insert(10)
        tree.insert(child_value)

        root = tree.root
        self.assertEqual(root.colour, Colour.BLACK)
        self.assertEqual(root.right.colour, Colour.RED)
        self.assertEqual(root.right.value, child_value)


if __name__ == "__main__":
    unittest.main()
