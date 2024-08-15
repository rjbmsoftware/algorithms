import unittest
from typing import Any, Optional

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

        Complexity
        Time: O(n) in the worst case for an unbalanced tree,
                O(log n) in the best/average case for a balanced tree.
        Space: O(h) where h is the height of the tree.
                In the worst case, this is O(n), and in the best case (balanced tree),
                it is O(log n).
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

    def find_node_by_value(self, value: Any) -> Optional[TreeNode]:
        """
        Find the first TreeNode with the value matching the value argument
        """
        if value is None or self._root is None:
            return

        working_node = self._root
        while working_node is not None:
            if working_node.value is None or working_node.value == value:
                break

            if working_node.value:
                if value <= working_node.value:
                    working_node = working_node.left
                else:
                    working_node = working_node.right

        return working_node

    def delete(self, node: TreeNode) -> None:
        pass


class TestBinarySearchTreeFind(unittest.TestCase):

    def test_value_is_None_None_returned(self):
        bst = BinarySearchTree(TreeNode(64))
        self.assertEqual(bst.find_node_by_value(None), None)

    def test_empty_tree_returns_None(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_node_by_value(64), None)

    def test_root_node_contains_value(self):
        search_value = 64
        root = TreeNode(value=search_value)
        bst = BinarySearchTree(root)
        search_result = bst.find_node_by_value(search_value)
        self.assertIsNotNone(search_result)
        self.assertEqual(search_result.value, search_value)

    def test_node_found_left_left(self):
        search_value = 16
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=32))
        bst.insert(TreeNode(value=search_value))
        search_result = bst.find_node_by_value(search_value)
        self.assertIsNotNone(search_result)
        self.assertEqual(search_result.value, search_value)

    def test_node_found_right_right(self):
        search_value = 256
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=128))
        bst.insert(TreeNode(value=search_value))
        search_result = bst.find_node_by_value(search_value)
        self.assertIsNotNone(search_result)
        self.assertEqual(search_result.value, search_value)



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
