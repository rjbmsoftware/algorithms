import unittest

from sort_utils import is_sorted


def quick_sort(values: list, start_index: int, end_index: int) -> None:
    """
    inplace quick sort implementation
    indexes are inclusive

    complexity
        time n log n
        space log n

    1. call partition on list
    2. output from partition is our partition point
    3. call quick sort on both halves

    lists that has a length less than or equal to one are sorted
    """
    if start_index >= end_index:
        return

    partition_point = partition(values, start_index, end_index)

    quick_sort(values, start_index, partition_point - 1)
    quick_sort(values, partition_point + 1, end_index)


def partition(values: list, start_index: int, end_index: int) -> int:
    """
    sort the array into two halves, less than or equal to 
    the pivot value and greater than the pivot value
    returning the pivot index, in place.

    high value is the end of the array
    swap the pivot value into the split point between the
    low high halves.
    """
    i = start_index - 1
    pivot_value = values[end_index]

    for j in range(start_index, end_index):
        if values[j] <= pivot_value:
            i += 1
            values[i], values[j] = values[j], values[i]

    values[i + 1], values[end_index] = values[end_index], values[i + 1]
    return i + 1


class QuickSortTest(unittest.TestCase):

    def test_partition_is_the_end_value_moved_to_the_centre(self):
        values = [8, 7, 3, 2, 4]
        partition(values, 0, len(values) - 1)
        self.assertEqual(values[2], 4)

    def test_even_length(self):
        values = [4, 3, 2, 1]
        quick_sort(values, 0, len(values) - 1)
        self.assertTrue(is_sorted(values))

    def test_odd_length(self):
        values = [5, 4, 3, 2, 1]
        quick_sort(values, 0, len(values) - 1)
        self.assertTrue(is_sorted(values))

    def test_single_value_list(self):
        values = [0]
        quick_sort(values, 0, len(values) - 1)
        self.assertTrue(is_sorted(values))

    def test_empty_is_sorted(self):
        values = []
        quick_sort(values, 0, 0)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        quick_sort(values, 0, len(values) - 1)
        self.assertTrue(is_sorted(values))


if __name__ == '__main__':
    unittest.main()
