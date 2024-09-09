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


if __name__ == "__main__":
    unittest.main()
