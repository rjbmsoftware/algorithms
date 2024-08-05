import unittest
from typing import Any, List

from tree_node import TreeNode


def depth_first_search(node: TreeNode, value: Any) -> List[TreeNode]:
    """
    Implementation of depth first search on a binary tree

    Add the first node to the stack, pop from the stack
    checking for search value, add right node then left
    node to the stack if they exist as we searching depth
    left to right

    complexity
        time O(n) as we have to visit each node to find all nodes
        that contain search value

        space O(n) in the worst case as it is possible have a
        highly lopsided tree, for a balanced tree it would be
        O(log n) (the height of the tree)
    """
    found_nodes = []
    stack = []

    stack.append(node)

    while stack:
        working_node = stack.pop()

        if working_node.value == value:
            found_nodes.append(working_node)

        if working_node.right:
            stack.append(working_node.right)

        if working_node.left:
            stack.append(working_node.left)

    return found_nodes


class DepthFirstSearchTest(unittest.TestCase):
    def test_root_node_only_contains_search_value(self):
        set_value = 1
        root = TreeNode(value=set_value)

        search_results = depth_first_search(root, set_value)

        self.assertEqual(
            1, len(search_results), "Root is the only node and has the search value"
        )
        self.assertIn(root, search_results)

    def test_value_not_in_tree(self):
        set_value = 4
        root = TreeNode(TreeNode(value=1), TreeNode(value=2), 3)

        search_results = depth_first_search(root, set_value)

        self.assertFalse(search_results, "Search results should be empty")

    def test_search_value_found_once_in_left(self):
        set_value = 2
        left = TreeNode(value=set_value)
        root = TreeNode(left, TreeNode(value=3), 1)

        search_results = depth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(left, search_results)

    def test_search_value_found_once_in_right(self):
        set_value = 2
        right = TreeNode(value=2)
        root = TreeNode(TreeNode(value=3), right, 1)

        search_results = depth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(right, search_results)

    def test_multiple_results_found(self):
        set_value = 1
        left = TreeNode(value=set_value)
        right = TreeNode(value=set_value)
        root = TreeNode(left, right, set_value)

        search_results = depth_first_search(root, set_value)

        self.assertEqual(3, len(search_results))
        self.assertIn(right, search_results)
        self.assertIn(left, search_results)
        self.assertIn(root, search_results)

    def test_found_in_lop_sided_tree(self):
        set_value = 1
        root = TreeNode(value=0)
        root_left_child = TreeNode(value=0)
        root.left = root_left_child
        root_left_child_2 = TreeNode(value=0)
        root_left_child.left = root_left_child_2
        root_left_child_3 = TreeNode(value=set_value)
        root_left_child_2.left = root_left_child_3

        search_results = depth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(root_left_child_3, search_results)


if __name__ == "__main__":
    unittest.main()
