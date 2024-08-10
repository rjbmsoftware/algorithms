import unittest
from typing import Optional

from tree_node import TreeNode


class BinarySearchTree:
    """
    Implementation of a binary search tree
    """

    def __init__(self, root: Optional[TreeNode] = None):
        self._root = root

    def insert(self, node: TreeNode, parent_node: Optional[TreeNode] = None) -> None:
        """
        If root node is None the new node will be root
        """
        if node is None:
            return

        if self._root is None:
            self._root = node
            return

        if parent_node is None:
            parent_node = self._root

        if node.value <= parent_node.value:
            if parent_node.left is None:
                parent_node.left = node
            else:
                self.insert(node, parent_node.left)
        else:
            self._root.right = node


class TestBinarySearchTree(unittest.TestCase):

    def test_empty_tree_adding_a_node_is_new_root(self):
        bst = BinarySearchTree()
        node = TreeNode()
        bst.insert(node)

        self.assertEqual(bst._root, node)

    def test_adding_nodes_with_values_less_than_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        less_than_root_node = TreeNode(value=32)
        bst.insert(less_than_root_node)
        self.assertEqual(root.left, less_than_root_node)

    def test_adding_nodes_with_values_equal_to_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        equal_to_root_node = TreeNode(value=64)
        bst.insert(equal_to_root_node)
        self.assertEqual(root.left, equal_to_root_node)

    def test_adding_nodes_with_values_more_than_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        greater_than_root_node = TreeNode(value=96)
        bst.insert(greater_than_root_node)
        self.assertEqual(root.right, greater_than_root_node)

    def test_minimum_value_is_left_most(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)

        less_than_root = TreeNode(value=32)
        bst.insert(less_than_root)

        less_than_left_root = TreeNode(value=16)
        bst.insert(less_than_left_root)

        self.assertEqual(root.left.left, less_than_left_root)


if __name__ == '__main__':
    unittest.main()
