import unittest
from typing import Any, List, Optional
from collections import deque


class TreeNode:
    def __init__(
        self,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
        value: Any = None,
    ) -> None:
        self._left = left
        self._right = right
        self._value = value

    @property
    def left(self) -> Optional["TreeNode"]:
        return self._left

    @left.setter
    def left(self, new_left_node: Optional["TreeNode"]) -> None:
        self._left = new_left_node

    @property
    def right(self) -> Optional["TreeNode"]:
        return self._right

    @right.setter
    def right(self, new_right_node: Optional["TreeNode"]) -> None:
        self._right = new_right_node

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        self._value = new_value


def breadth_first_search(root_node: TreeNode, value: Any) -> List[TreeNode]:
    """
    Implementation of breadth first search on a binary tree
    """
    found_nodes = []
    queue = deque()

    queue.append(root_node)

    while queue:
        node = queue.popleft()
        if node and node.value == value:
            found_nodes.append(node)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return found_nodes


class BreadthFirstSearchTest(unittest.TestCase):
    def test_root_node_only_contains_search_value(self):
        set_value = 1
        root = TreeNode(value=set_value)

        search_results = breadth_first_search(root, set_value)

        self.assertEqual(
            1, len(search_results), "Root is the only node and has the search value"
        )
        self.assertIn(root, search_results)

    def test_value_not_in_tree(self):
        set_value = 4
        root = TreeNode(TreeNode(value=1), TreeNode(value=2), 3)

        search_results = breadth_first_search(root, set_value)

        self.assertFalse(search_results, "Search results should be empty")

    def test_search_value_found_once_in_left(self):
        set_value = 2
        left = TreeNode(value=set_value)
        root = TreeNode(left, TreeNode(value=3), 1)

        search_results = breadth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(left, search_results)

    def test_search_value_found_once_in_right(self):
        set_value = 2
        right = TreeNode(value=2)
        root = TreeNode(TreeNode(value=3), right, 1)

        search_results = breadth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(right, search_results)

    def test_multiple_results_found(self):
        set_value = 1
        left = TreeNode(value=set_value)
        right = TreeNode(value=set_value)
        root = TreeNode(left, right, set_value)

        search_results = breadth_first_search(root, set_value)

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

        search_results = breadth_first_search(root, set_value)

        self.assertEqual(1, len(search_results))
        self.assertIn(root_left_child_3, search_results)


if __name__ == "__main__":
    unittest.main()
