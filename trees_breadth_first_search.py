from typing import Optional, Self, Any

class TreeNode:

    def __init__(self, left: Optional[Self] = None,
                 right: Optional[Self] = None,
                 value: Any = None) -> None:
        self._left = left
        self._right = right
        self._value = value

    def _get_left_node(self) -> Optional[Self]:
        return self._left

    def _set_left_node(self, new_left_node: Optional[Self]) -> None:
        self._left = new_left_node

    left = property(
        fget=_get_left_node,
        fset=_set_left_node
    )

    def _get_right_node(self) -> Optional[Self]:
        return self._right

    def _set_right_node(self, new_right_node: Optional[Self]) -> None:
        self._right = new_right_node

    right = property(
        fget=_get_right_node,
        fset=_set_right_node
    )

    def _get_value(self) -> Any:
        return self._value
    
    def _set_value(self, new_value: Any) -> None:
        self._value = new_value

    value = property(
        fget=_get_value,
        fset=_set_value
    )
