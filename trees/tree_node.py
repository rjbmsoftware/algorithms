from typing import Any, Optional, Self


class TreeNode:
    """
    Implementation of a binary tree with properties
    of left, right, and value which can be any.
    """

    def __init__(
        self,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
        value: Any = None,
    ) -> None:
        self._left = left
        self._right = right
        self._value = value

    @property
    def left(self) -> Optional[Self]:
        return self._left

    @left.setter
    def left(self, new_left_node: Optional[Self]) -> None:
        self._left = new_left_node

    @property
    def right(self) -> Optional[Self]:
        return self._right

    @right.setter
    def right(self, new_right_node: Optional[Self]) -> None:
        self._right = new_right_node

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any) -> None:
        self._value = new_value


class HeightNode(TreeNode):
    def __init__(
        self,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
        value: Any = None,
    ) -> None:
        super().__init__(left, right, value)
        self._height = 0

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        self._height = new_height
