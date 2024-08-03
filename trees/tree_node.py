from typing import Any, Optional


class TreeNode:
    """
    Implementation of a binary tree with properties
    of left, right, and value which can be any.
    """
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
