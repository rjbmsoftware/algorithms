from typing import TypeVar
import unittest


T = TypeVar('T')


def linear_search(values: list[T | None], target_value: T) -> int | None:
    """
    Iterative implementation of linear search

    if the value is found within values then the index is returned otherwise None

    complexity
        time:
            O(n) where n is the number of elements in the list
        space:
            O(1) as it is an iterative implementation where the elements are compared
    """

    for index, value in enumerate(values):
        if value == target_value:
            return index

    return None


class LinearSearchTest(unittest.TestCase):

    def test_value_contained_within_values(self):
        values = [3, 2, 1]
        found_index = linear_search(values, 1)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 2)

    def test_value_not_contained_within_values(self):
        values = [3, 2, 1]
        found_index = linear_search(values, 99)
        self.assertIsNone(found_index)

    def test_values_empty_returns_none(self):
        found_index = linear_search([], 'test')
        self.assertIsNone(found_index)

    def test_none_values_in_list(self):
        values = ['a', None, 'c']
        found_index = linear_search(values, 'c')
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 2)

    def test_none_values_in_list_searching_for_none(self):
        values = ['a', None, 'c']
        found_index = linear_search(values, None)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 1)


if __name__ == '__main__':
    unittest.main()
