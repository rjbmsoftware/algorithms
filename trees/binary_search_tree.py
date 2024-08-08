import unittest
from typing import Optional

from tree_node import TreeNode


class BinarySearchTree:
    """
    Implementation of a binary search tree
    """

    def __init__(self, root: Optional[TreeNode] = None):
        self._root = root

    def insert(self, node: TreeNode) -> None:
        """
        If root node is None the new node will be root
        """
        if node is None:
            return

        if self._root is None:
            self._root = node


class TestBinarySearchTree(unittest.TestCase):

    def test_empty_tree_adding_a_node_is_new_root(self):
        bst = BinarySearchTree()
        node = TreeNode()
        bst.insert(node)


if __name__ == '__main__':
    unittest.main()
