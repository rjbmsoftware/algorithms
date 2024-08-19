import unittest
from typing import Any, Optional, Tuple

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

        Complexity
        Time: O(n) in the worst case for an unbalanced tree,
              O(log n) for a balanced tree

        Space: O(1) the implementation is iterative and does not depend
               on previous values
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

    def find_parent_child_with_value(self, subtree_root: TreeNode, search_value: Any) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        """
        Returns two variables parent and child TreeNodes
        """
        if subtree_root.value is None:
            raise ValueError("subtree root cannot have a None value")

        if search_value <= subtree_root.value:
            child = subtree_root.left
        else:
            child = subtree_root.right

        if child is None:
            return subtree_root, child

        if child.value is not None and child.value == search_value:
            return subtree_root, child

        return self.find_parent_child_with_value(child, search_value)

    def delete_by_value(self, value: Any) -> None:
        """
        Deletes the first found node with value
        """
        parent_node, child_node = self.find_parent_child_with_value(
            self._root, value)
        if parent_node is None or child_node is None:
            return

        # if both child children are None remove the node
        if child_node.left is None and child_node.right is None:
            if parent_node.left == child_node:
                parent_node.left = None
            else:
                parent_node.right = None

        if child_node.left is not None and child_node.right is not None:
            raise NotImplementedError(
                'not implement removal with both children yet!')

        # if child has a single child remove the node assigning
        # the parent child the correct grand child
        if child_node.left is None:
            new_child = child_node.right
        else:
            new_child = child_node.left

        if parent_node.left == child_node:
            parent_node.left = new_child
        else:
            parent_node.right = new_child



class TestBinarySearchTreeDelete(unittest.TestCase):

    def test_value_not_in_tree_no_errors_raised(self):
        bst = BinarySearchTree(TreeNode(value=64))
        bst.delete_by_value(32)
        root = bst.find_node_by_value(64)
        self.assertIsNotNone(root)

    def test_remove_childless_left_node(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=32))
        bst.delete_by_value(32)
        self.assertIsNone(root.left)

    def test_remove_childless_right_node(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=128))
        bst.delete_by_value(128)
        self.assertIsNone(root.right)

    def test_remove_left_node_with_left_child(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        delete_value = 32
        bst.insert(TreeNode(value=delete_value))
        bst.insert(TreeNode(value=16))
        bst.delete_by_value(delete_value)
        self.assertEqual(root.left.value, 16)

    def test_remove_left_node_with_right_child(self):
        root = TreeNode(value=64)
        bst = BinarySearchTree(root)
        delete_value = 32
        bst.insert(TreeNode(value=delete_value))
        bst.insert(TreeNode(value=48))
        bst.delete_by_value(delete_value)
        self.assertEqual(root.left.value, 48)


class TestBinarySearchTreeFindParentWithChildValue(unittest.TestCase):

    def test_child_left_child_node_has_value(self):
        search_value = 32
        root = TreeNode(value=64)
        left = TreeNode(value=search_value)
        bst = BinarySearchTree(root)
        bst.insert(left)
        parent, child = bst.find_parent_child_with_value(root, search_value)
        self.assertEqual(root, parent)
        self.assertEqual(child, left)

    def test_child_right_child_node_has_value(self):
        search_value = 128
        root = TreeNode(value=64)
        right = TreeNode(value=search_value)
        bst = BinarySearchTree(root)
        bst.insert(right)
        parent, child = bst.find_parent_child_with_value(root, search_value)
        self.assertEqual(root, parent)
        self.assertEqual(child, right)

    def test_child_node_has_value_where_parent_is_not_root(self):
        search_value = 48
        root = TreeNode(value=64)
        root_left_child = TreeNode(value=32)
        root_left_right_child = TreeNode(value=search_value)
        bst = BinarySearchTree(root)
        bst.insert(root_left_child)
        bst.insert(root_left_right_child)
        parent, child = bst.find_parent_child_with_value(root, search_value)
        self.assertEqual(parent, root_left_child)
        self.assertEqual(child, root_left_right_child)


class TestBinarySearchTreeFind(unittest.TestCase):

    def test_value_is_none_none_returned(self):
        bst = BinarySearchTree(TreeNode(64))
        self.assertEqual(bst.find_node_by_value(None), None)

    def test_empty_tree_returns_none(self):
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
