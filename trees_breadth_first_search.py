from typing import Optional, Self, Any, List
import unittest


class TreeNode:
    def __init__(
        self,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
        value: Any = None,
    ) -> None:
        self._left = left
        self._right = right
        self._value = value

    def _get_left_node(self) -> Optional[Self]:
        return self._left

    def _set_left_node(self, new_left_node: Optional[Self]) -> None:
        self._left = new_left_node

    left = property(fget=_get_left_node, fset=_set_left_node)

    def _get_right_node(self) -> Optional[Self]:
        return self._right

    def _set_right_node(self, new_right_node: Optional[Self]) -> None:
        self._right = new_right_node

    right = property(fget=_get_right_node, fset=_set_right_node)

    def _get_value(self) -> Any:
        return self._value

    def _set_value(self, new_value: Any) -> None:
        self._value = new_value

    value = property(fget=_get_value, fset=_set_value)


def breadth_first_search(root_node: TreeNode, value: Any) -> List[TreeNode]:
    """
    Implementation of breadth first search on a binary tree
    """
    found_nodes = []
    queue = []

    queue.append(root_node)

    while queue:
        node = queue.pop(0)
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
        left = TreeNode(value=2)
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


if __name__ == "__main__":
    unittest.main()
