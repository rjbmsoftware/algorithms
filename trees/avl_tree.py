from collections import deque
from typing import Optional
import unittest

from tree_node import HeightNode


class AVLTree:
    """
    Implementation of the Adelson-Velsky and Landis self balancing binary search tree
    """

    def __init__(self, root: Optional[HeightNode] = None):
        self._root = root

    @property
    def root(self) -> Optional[HeightNode]:
        return self._root

    def insert(self, node: HeightNode) -> None:
        if self._root is None:
            self._root = node
            self._root.height = 1
            return

        self._insert(node, self._root)

    def _insert(self, node: HeightNode, parent_node: HeightNode) -> None:
        if node.value <= parent_node.value:
            if parent_node.left is None:
                parent_node.left = node
            else:
                self._insert(node, parent_node.left)
        else:
            if parent_node.right is None:
                parent_node.right = node
            else:
                self._insert(node, parent_node.right)

        node.height = self.node_height(node)
        parent_node.height = self.node_height(parent_node)

        self.balance_single_layer(parent_node)

    def balance_single_layer(self, node: HeightNode) -> None:
        """
        Applies the needed rotation to balance the subtree from the given node

        Complexity
            Time: O(1)
            Space: O(1)

        We only check the direct child heights and swap values if needed
        """
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        balance_factor = right_height - left_height

        if -1 <= balance_factor <= 1:
            return

        if balance_factor > 1:
            self._left_rotation(node)
        else:
            self._right_rotation(node)

    def contains(self, value) -> bool:
        """
        Finds the value in the AVL tree, True for the value exists
        False otherwise

        Complexity
            Time: O(log n) as the AVL is always balanced the worst case is a leaf node
                  and the height of a balanced tree is log n where n is the amount of
                  nodes
            Space: O(1) constant time as this is in an iterative solution
        """
        node = self._root
        while node:
            if node.value == value:
                return True
            if value > node.value:
                node = node.right
            else:
                node = node.left

        return False

    def _left_rotation(self, node: HeightNode):
        """
        Performs a left rotation

        Pull the right node up and the parent becomes the left child
        if the child has a left node that will become the new nodes
        right child
        """
        if node.right is None:
            return

        new_left_child = HeightNode(node.left, node.right.left, node.value)
        node.value = node.right.value
        node.left = new_left_child
        node.right = node.right.right

        new_left_child.height = self.node_height(new_left_child)
        node.height = self.node_height(node)

    def _right_rotation(self, node: HeightNode):
        """
        Performs a right rotation

        Pull the left node up and the parent becomes the right child
        if the child has a right node that will become the new nodes
        left child
        """
        if node.left is None:
            return

        new_right_child = HeightNode(node.left.right, node.right, node.value)
        node.value = node.left.value
        node.right = new_right_child
        node.left = node.left.left

        new_right_child.height = self.node_height(new_right_child)
        node.height = self.node_height(node)

    def node_height(self, node: Optional[HeightNode]) -> int:
        """
        the maximum value of the children heights plus one
        """
        if not node:
            return 0

        return max(
            node.left.height if node.left else 0,
            node.right.height if node.right else 0
        ) + 1

    def delete(self, value) -> None:
        if self._root is None or self.contains(value) is False:
            return

        self._delete(value, None, self._root)

    def _delete(self, value, parent: Optional[HeightNode], node: Optional[HeightNode]) -> None:
        if node is None:
            return

        if node.value == value:
            self._remove(parent, node)

            if parent:
                parent.height = self.node_height(parent)
        else:
            child = node.left if node.value > value else node.right
            self._delete(value, node, child)

        if parent:
            self.balance_single_layer(parent)

    def _remove(self, parent: Optional[HeightNode], node: HeightNode) -> None:
        node_is_childless = node.left is None and node.right is None
        if node_is_childless:
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self._root = None
            return

        node_has_left_child_only = node.left and node.right is None
        if node_has_left_child_only:
            if parent:
                parent.value = node.value
                parent.left = None
                parent.height = self.node_height(parent)
            else:
                self._root = self._root.left
                self._root.height = self.node_height(self._root)
            return

        node_has_right_child_only = node.left is None and node.right
        if node_has_right_child_only:
            if parent:
                parent.value = node.value
                parent.right = None
                parent.height = self.node_height(parent)
            else:
                self._root = self._root.right
                self._root.height = self.node_height(self._root)
            return

        node_has_two_children = node.left and node.right
        if node_has_two_children:
            minimum_value = self.min_value(node.right)
            self.delete(minimum_value)
            node.value = minimum_value

    def min_value(self, node: HeightNode) -> any:
        if node is None:
            raise ValueError('node must have a value')

        while node.left:
            node = node.left

        return node.value


class TestAVLTreeInsert(unittest.TestCase):

    def test_basic_bst_inserts(self):
        avl_tree = AVLTree()

        avl_tree.insert(HeightNode(value=64))
        avl_tree.insert(HeightNode(value=32))
        avl_tree.insert(HeightNode(value=128))

        root = avl_tree.root
        self.assertEqual(root.value, 64)
        self.assertEqual(root.left.value, 32)
        self.assertEqual(root.right.value, 128)

    def test_node_height_increases_as_right_children_increase(self):
        avl_tree = AVLTree()

        avl_tree.insert(HeightNode(value=64))
        avl_tree.insert(HeightNode(value=128))

        root = avl_tree.root
        self.assertEqual(root.height, 2)
        self.assertEqual(root.right.height, 1)

    def test_node_height_increases_as_left_children_increase(self):
        avl_tree = AVLTree()
        avl_tree.insert(HeightNode(value=32))
        avl_tree.insert(HeightNode(value=16))

        root = avl_tree.root
        self.assertEqual(root.height, 2)
        self.assertEqual(root.left.height, 1)

    def test_balance_on_insert(self):
        avl_tree = AVLTree()

        avl_tree.insert(HeightNode(value=64))
        avl_tree.insert(HeightNode(value=32))
        avl_tree.insert(HeightNode(value=16))

        root = avl_tree.root
        self.assertEqual(root.left.value, 16)
        self.assertEqual(root.left.height, 1)

        self.assertEqual(root.value, 32)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.right.value, 64)
        self.assertEqual(root.right.height, 1)

    def test_left_rotation(self):
        root = HeightNode(value=64)
        root.height = 3

        root.right = HeightNode(value=128)
        root.right.height = 2

        root.right.right = HeightNode(value=256)
        root.right.right.height = 1

        AVLTree().balance_single_layer(root)

        self.assertEqual(root.left.value, 64)
        self.assertEqual(root.left.height, 1)

        self.assertEqual(root.value, 128)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.right.value, 256)
        self.assertEqual(root.right.height, 1)

    def test_right_rotation(self):
        root = HeightNode(value=64)
        root.height = 3

        root.left = HeightNode(value=32)
        root.left.height = 2

        root.left.left = HeightNode(value=16)
        root.left.left.height = 1

        AVLTree().balance_single_layer(root)

        self.assertEqual(root.left.value, 16)
        self.assertEqual(root.left.height, 1)

        self.assertEqual(root.value, 32)
        self.assertEqual(root.height, 2)

        self.assertEqual(root.right.value, 64)
        self.assertEqual(root.right.height, 1)


class TestAVLSearch(unittest.TestCase):

    def test_search_empty_tree_is_none(self):
        avl_tree = AVLTree()
        contains_value = avl_tree.contains(1)
        self.assertFalse(contains_value)

    def test_search_value_is_root(self):
        value = 10
        avl_tree = AVLTree(HeightNode(value=value))
        contains_value = avl_tree.contains(value)
        self.assertTrue(contains_value)

    def test_value_in_right_branch(self):
        """
                3
             1     5
           0   2 4   6
        """
        value = 6
        avl_tree = AVLTree()
        for i in range(7):
            avl_tree.insert(HeightNode(value=i))

        contains_value = avl_tree.contains(value)
        self.assertTrue(contains_value)

    def test_value_in_left_branch(self):
        """
                3
             1     5
           0   2 4   6
        """
        value = 0
        avl_tree = AVLTree()
        for i in range(7):
            avl_tree.insert(HeightNode(value=i))

        contains_value = avl_tree.contains(value)
        self.assertTrue(contains_value)


class TestAVLDelete(unittest.TestCase):

    def test_delete_value_from_empty_tree(self):
        avl_tree = AVLTree()
        avl_tree.delete(1)
        self.assertIsNone(avl_tree.root)

    def test_delete_value_from_single_value_tree(self):
        value = 1
        avl_tree = AVLTree(HeightNode(value=value))
        avl_tree.delete(value)
        self.assertIsNone(avl_tree.root)

    def test_delete_root_value_with_right_node(self):
        value_one = 1
        value_two = 2
        avl_tree = AVLTree(HeightNode(value=value_one))
        avl_tree.insert(HeightNode(value=value_two))

        avl_tree.delete(value_one)

        self.assertEqual(avl_tree.root.value, value_two)
        self.assertEqual(avl_tree.root.height, 1)

    def test_delete_root_value_with_left_node(self):
        value_one = 32
        value_two = 16
        avl_tree = AVLTree(HeightNode(value=value_one))
        avl_tree.insert(HeightNode(value=value_two))

        avl_tree.delete(value_one)

        self.assertEqual(avl_tree.root.value, value_two)
        self.assertEqual(avl_tree.root.height, 1)

    def test_delete_root_value_with_two_children(self):
        value_one = 32
        value_two = 16
        value_three = 64
        avl_tree = AVLTree(HeightNode(value=value_one))
        avl_tree.insert(HeightNode(value=value_two))
        avl_tree.insert(HeightNode(value=value_three))

        avl_tree.delete(32)

        self.assertEqual(avl_tree.root.value, value_three)

    def test_find_min_value_subtree(self):
        minimum = 0
        avl_tree = AVLTree()
        for i in range(minimum, 7):
            avl_tree.insert(HeightNode(value=i))

        minimum_actual = avl_tree.min_value(avl_tree.root)

        self.assertEqual(minimum, minimum_actual)

    def test_height_updated(self):
        """
                3
               / \
              1   5
             / \\ / \
            0  2  4 6
        """
        minimum = 0
        avl_tree = AVLTree()
        for i in range(minimum, 7):
            avl_tree.insert(HeightNode(value=i))

        avl_tree.delete(0)
        avl_tree.delete(2)

        self.assertEqual(avl_tree.root.left.height, 1)


def print_tree(tree: AVLTree) -> None:
    queue = deque()
    queue.append(tree.root)
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    unittest.main()
