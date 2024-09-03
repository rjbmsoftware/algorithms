from typing import Optional
import unittest

from tree_node import HeightNode


class AVLTree:
    """
    Implementation of the Adelson-Velsky and Landis self balancing binary search tree
    """

    def __init__(self, root: Optional[HeightNode] = None):
        self._root = root

    def insert(self, node: HeightNode) -> None:
        if self._root is None:
            self._root = node
            return

        self._insert(node, self._root)

    def _insert(self, node: HeightNode, parent_node: HeightNode):
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


class TestAVLTreeInsert(unittest.TestCase):

    def test_basic_bst_inserts(self):
        root = HeightNode(value=64)
        avl_tree = AVLTree()

        avl_tree.insert(root)
        avl_tree.insert(HeightNode(value=32))
        avl_tree.insert(HeightNode(value=128))

        self.assertEqual(avl_tree._root.value, 64)
        self.assertEqual(root.left.value, 32)
        self.assertEqual(root.right.value, 128)


if __name__ == "__main__":
    unittest.main()
