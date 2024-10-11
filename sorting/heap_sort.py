import unittest

from sort_utils import is_sorted


def heap_sort(values: list) -> None:
    # TODO: implement
    # sift up
    # sift down
    # extract min
    # tree heap
    # parent (i) is i / 2
    # left child (i) 2*i
    # right child is 2*i + 1
    pass


def max_heapify(values: list, parent_index: int) -> None:
    """
    Swaps the values of parent_index and children to ensure the parent is of greater value than the
    direct children
    """
    parent_outside_list_bounds = 0 < parent_index > len(values) - 1
    if parent_outside_list_bounds:
        return

    # off by one to allow for zero based lists
    left_child_index = parent_index * 2 + 1
    right_child_index = parent_index * 2 + 2

    if left_child_index < len(values) and right_child_index < len(values):
        if values[left_child_index] > values[right_child_index]:
            largest_child_index = left_child_index
        else:
            largest_child_index = right_child_index
    elif left_child_index < len(values):
        largest_child_index = left_child_index
    elif right_child_index < len(values):
        largest_child_index = right_child_index
    else:
        return  # leaf

    if values[parent_index] < values[largest_child_index]:
        values[parent_index], values[largest_child_index] = values[largest_child_index], values[parent_index]
        max_heapify(values, largest_child_index)


def build_max_heap(values: list) -> None:
    for i in range(len(values) // 2 - 1, -1, -1):
        max_heapify(values, i)


class HeapSortTest(unittest.TestCase):
    pass


class BuildMaxHeapTest(unittest.TestCase):
    def test_sifting_down(self):
        values = [1, 2, 3, 4, 5, 6]
        build_max_heap(values)
        self.assertEqual(values, [6, 5, 3, 4, 2, 1])


class MaxHeapifyTest(unittest.TestCase):

    def test_zero_parent_left_child_is_largest(self):
        values = [1, 3, 2]
        max_heapify(values, 0)
        self.assertEqual(values, [3, 1, 2])

    def test_zero_parent_right_child_is_largest(self):
        values = [1, 2, 3]
        max_heapify(values, 0)
        self.assertEqual(values, [3, 2, 1])

    def test_zero_parent_is_largest(self):
        values = [3, 2, 1]
        max_heapify(values, 0)
        self.assertEqual(values, [3, 2, 1])

    def test_parent_left_child_is_largest(self):
        values = [1, 2, 3, 5, 4]
        max_heapify(values, 1)
        self.assertEqual(values, [1, 5, 3, 2, 4])

    def test_parent_right_child_is_largest(self):
        values = [1, 2, 3, 4, 5]
        max_heapify(values, 1)
        self.assertEqual(values, [1, 5, 3, 4, 2])

    def test_parent_is_largest(self):
        values = [1, 5, 3, 4, 2]
        max_heapify(values, 1)
        self.assertEqual(values, [1, 5, 3, 4, 2])

    def test_parent_invalid_index(self):
        values = [1, 2, 3]
        max_heapify(values, 99)
        self.assertEqual(values, [1, 2, 3])

    def test_left_child_invalid_index(self):
        values = [1, 2, 3]
        max_heapify(values, 2)
        self.assertEqual(values, [1, 2, 3])

    def test_right_child_invalid_index(self):
        values = [1, 2, 3, 4]
        max_heapify(values, 1)
        self.assertEqual(values, [1, 4, 3, 2])



if __name__ == "__main__":
    unittest.main()
