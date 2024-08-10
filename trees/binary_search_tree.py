import unittest
from typing import Optional

from tree_node import TreeNode


class BinarySearchTree:
    """
    Implementation of a binary search tree
    """

    def __init__(self, root: Optional[TreeNode] = None):
        self._root = root

    def insert(self, node: TreeNode, subtree_root: Optional[TreeNode] = None) -> None:
        """
        If root node is None the new node will be root
        """
        if node is None:
            return

        if self._root is None:
            self._root = node
            return

        if subtree_root is None:
            subtree_root = self._root

        if node.value <= subtree_root.value:
            if subtree_root.left is None:
                subtree_root.left = node
            else:
                self.insert(node, subtree_root.left)
        else:
            if subtree_root.right is None:
                subtree_root.right = node
            else:
                self.insert(node, subtree_root.right)


class TestBinarySearchTreeInsert(unittest.TestCase):

    def test_empty_tree_adding_a_node_is_new_root(self):
        bst = BinarySearchTree()
        bst.insert(TreeNode(value=64))

        self.assertEqual(bst._root.value, 64)

    def test_adding_nodes_with_values_less_than_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=32))
        self.assertEqual(root.left.value, 32)

    def test_adding_nodes_with_values_equal_to_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=64))
        self.assertEqual(root.left.value, 64)

    def test_adding_nodes_with_values_more_than_root(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=96))
        self.assertEqual(root.right.value, 96)

    def test_minimum_value_is_left_most(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=32))
        bst.insert(TreeNode(value=16))

        self.assertEqual(root.left.left.value, 16)

    def test_maximum_value_is_right_most(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=96))
        bst.insert(TreeNode(value=128))

        self.assertEqual(root.right.right.value, 128)

    def test_wiggle_values(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=32))
        bst.insert(TreeNode(value=48))

        self.assertEqual(root.left.right.value, 48)


if __name__ == '__main__':
    unittest.main()
