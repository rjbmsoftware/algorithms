import unittest

from sort_utils import is_sorted


def heap_sort(values: list) -> None:
    """
    heap sort implementation initial recursive implementation

    complexity
        time: O(n log n) where n is the number of elements in the list, n time to build the
        initial max heap as we have to visit each element, swap the last child with the maximum
        element at position zero to the end, calling max heapify to sift the lowest value down so
        the heap is valid which log n time so O(n log n)

        space: O(log n) where n is the number of elements in the list as it is a recursive
        implementation, max heapify recurses down the list tree, the amount of layers is log n
    """

    build_max_heap(values)

    for i in range(len(values) - 1, 0, -1):
        extract_max(values, i)
        max_heapify(values, 0, i - 1)


def max_heapify(values: list, parent_index: int, end_index=None) -> None:
    """
    Swaps the values of parent_index and children to ensure the parent is of greater value than the
    direct children
    """

    # off by one to allow for zero based lists
    left_child_index = parent_index * 2 + 1
    right_child_index = left_child_index + 1

    largest = parent_index

    if end_index is None:
        end_index = len(values) - 1

    if left_child_index <= end_index and values[left_child_index] > values[largest]:
        largest = left_child_index

    if right_child_index <= end_index and values[right_child_index] > values[largest]:
        largest = right_child_index

    if largest != parent_index:
        values[parent_index], values[largest] = values[largest], values[parent_index]
        max_heapify(values, largest, end_index)


def build_max_heap(values: list) -> None:
    for i in range(len(values) // 2 - 1, -1, -1):
        max_heapify(values, i)


def extract_max(values: list, end_index: int) -> None:
    values[0], values[end_index] = values[end_index], values[0]


class HeapSortTest(unittest.TestCase):

    def test_empty_is_sorted(self):
        values = []
        heap_sort(values)
        self.assertTrue(is_sorted(values))

    def test_single_value_list(self):
        values = [1]
        heap_sort(values)
        self.assertEqual(len(values), 1)
        self.assertTrue(values[0], 1)

    def test_two_value_list(self):
        values = [2, 1]
        heap_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2], actual {values}')

    def test_three_value_list(self):
        values = [3, 2, 1]
        heap_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2, 3], actual {values}')

    def test_max_to_min(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        heap_sort(values)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        heap_sort(values)
        self.assertTrue(is_sorted(values))

    def test_same(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        heap_sort(values)
        self.assertTrue(is_sorted(values))


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
