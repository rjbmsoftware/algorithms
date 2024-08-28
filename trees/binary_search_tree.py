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

        Complexity
        Time:
            O(n) where n is the depth of the tree as we need to find the
            node first then find the minimum in the right subtree to swap
            the values over and remove the old minimum leaf node. For a
            balanced tree the best case this would be O(log n)
        Space:
            O(1) traversing the tree does not use more memory as it is an
            iterative solution
        """
        parent_node, child_node = self.find_parent_child_with_value(
            self._root, value)
        if parent_node is None or child_node is None:
            return

        child_has_children = child_node.left is not None or child_node.right is not None
        if child_has_children:

            child_has_two_children = child_node.left is not None and child_node.right is not None
            if child_has_two_children:
                # find the min value in the right tree
                min_parent = child_node
                min_child = child_node.left
                while min_child.left is not None:
                    min_parent = min_child
                    min_child = min_parent.left

                # remove the reference to the min child node, min child can have right child
                min_parent.left = min_child.right

                child_node.value = min_child.value
            else:
                if child_node.left is None:
                    new_child = child_node.right
                else:
                    new_child = child_node.left

                self.replace_child_with(parent_node, child_node, new_child)
        else:
            self.replace_child_with(parent_node, child_node, None)

    def replace_child_with(self, parent: TreeNode, child: TreeNode, replacement: Optional[TreeNode]) -> None:
        if parent.left == child:
            parent.left = replacement
        else:
            parent.right = replacement

    def in_order_traversal_values(self) -> list:
        """
        Returns a list of values in ascending order

        Complexity
        Time:
            0(n) as we visit every node in the tree
        Space:
            0(n) since we store each value and additional space
            worst case for a lopsided tree being the height O(h)
            best case is a balanced tree with h being the height
            of the tree O(log n)
        """
        values = []
        self._in_order_traversal(values, self._root)
        return values

    def _in_order_traversal(self, values: list, node: Optional[TreeNode]) -> None:
        if node is None:
            return

        self._in_order_traversal(values, node.left)
        values.append(node.value)
        self._in_order_traversal(values, node.right)


class TestBinarySearchTreeInOrderTraversalValues(unittest.TestCase):

    def test_empty_tree_empty_list(self):
        bst = BinarySearchTree()

        values = bst.in_order_traversal_values()

        self.assertFalse(values)

    def test_single_node_tree(self):
        value = 1
        bst = BinarySearchTree(TreeNode(value=value))

        values = bst.in_order_traversal_values()

        self.assertIsNotNone(values)
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0], value)

    def test_left_only_nodes(self):
        input_values = [4, 3, 2, 1]
        bst = BinarySearchTree()
        for i in input_values:
            bst.insert(TreeNode(value=i))
        input_values.sort()

        output_values = bst.in_order_traversal_values()
        self.assertEqual(input_values, output_values)

    def test_right_only_nodes(self):
        input_values = [1, 2, 3, 4]
        bst = BinarySearchTree()
        for i in input_values:
            bst.insert(TreeNode(value=i))

        output_values = bst.in_order_traversal_values()

        self.assertEqual(input_values, output_values)

    def test_left_right_left_right(self):
        input_values = [4, 2, 3, 1]
        bst = BinarySearchTree()
        for i in input_values:
            bst.insert(TreeNode(value=i))
        input_values.sort()

        output_values = bst.in_order_traversal_values()
        self.assertEqual(input_values, output_values)


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

    def test_remove_node_with_two_children(self):
        """
                    100
                        \
                        200
                        / \
                    150    300
                           / \
                        250   400
                        /
                     225
        """
        root = TreeNode(value=100)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=200))
        delete_value = 300
        bst.insert(TreeNode(value=delete_value))
        bst.insert(TreeNode(value=400))
        bst.insert(TreeNode(value=150))
        bst.insert(TreeNode(value=250))
        bst.insert(TreeNode(value=225))

        bst.delete_by_value(delete_value)

        self.assertEqual(root.right.right.value, 225)
        self.assertIsNone(root.right.right.left.left)

    def test_remove_node_with_two_children_min_node_has_right_child(self):
        """
                    100
                        \
                        200
                        / \
                    150    300
                            / \
                        250   400
                        /
                    225
                        \
                        237
        """
        root = TreeNode(value=100)
        bst = BinarySearchTree(root)
        bst.insert(TreeNode(value=200))
        delete_value = 300
        bst.insert(TreeNode(value=delete_value))
        bst.insert(TreeNode(value=400))
        bst.insert(TreeNode(value=150))
        bst.insert(TreeNode(value=250))
        bst.insert(TreeNode(value=225))
        bst.insert(TreeNode(value=237))

        bst.delete_by_value(delete_value)

        self.assertEqual(root.right.right.value, 225)
        self.assertEqual(root.right.right.left.left.value, 237)


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
