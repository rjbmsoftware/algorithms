from typing import TypeVar
import unittest

T = TypeVar('T')


def ranged_binary_search(values: list[T], value: T, start_index: int, end_index: int) -> int | None:
    while start_index <= end_index:
        working_index = (end_index - start_index) // 2 + start_index

        value_found = values[working_index] == value
        if value_found:
            return working_index

        search_second_half = values[working_index] < value
        if search_second_half:
            start_index = working_index + 1
        else:
            end_index = working_index - 1

    return None


def exponential_search(values: list[T], value: T) -> int | None:
    """
    Searches the values for value returning the index in the list of the found value otherwise None,
    values must be sorted

    This search is useful over binary search where the values are more likely to be at the beginning
    of the list

    1. find the range the value may reside in by exponentially increasing the range from the
       beginning of the list
    2. use binary search on the range of values the value is likely to be in

    complexity
        time:
            O(log n) where n is the number of elements in values the exponential search doubles the
            search range each iteration then the binary search on that range is 0(log i) where i is
            the range given.
        space:
            O(1) space as it is an iterative solution with the state being limited to a few
            variables for index tracking.
    """

    if not values:
        return None

    if len(values) == 1:
        if values[0] == value:
            return 0
        else:
            return None

    start_index = 0
    end_index = 1

    while start_index < end_index:

        value_found = values[start_index] == value
        if value_found:
            return start_index

        value_may_exist_within_range = values[start_index] <= value <= values[end_index]
        if value_may_exist_within_range:
            return ranged_binary_search(values, value, start_index, end_index)

        start_index = end_index
        end_index *= 2

        if end_index >= len(values):
            end_index = len(values) - 1

    return None


class ExponentialSearchTest(unittest.TestCase):

    def test_contains_value(self):
        values = [1, 2, 3, 4, 5]
        value = 3
        found_index = exponential_search(values, value)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 2)

    def test_contains_value_first(self):
        values = [1, 2, 3, 4, 5]
        value = 1
        found_index = exponential_search(values, value)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 0)

    def test_contains_value_last(self):
        values = [1, 2, 3, 4, 5]
        value = 5
        found_index = exponential_search(values, value)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 4)

    def test_contains_value_larger_list(self):
        values = [i for i in range(0, 200)]
        value = 150
        found_index = exponential_search(values, value)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 150)

    def test_does_not_contain_value(self):
        values = [1, 2, 3, 4, 5]
        value = 99
        found_index = exponential_search(values, value)
        self.assertIsNone(found_index)

    def test_small_list_contains_value(self):
        values = [1]
        value = 1
        found_index = exponential_search(values, value)
        self.assertEqual(found_index, 0)

    def test_small_list_does_not_contain_value(self):
        values = [1]
        value = 2
        found_index = exponential_search(values, value)
        self.assertIsNone(found_index)

    def test_empty_list(self):
        values = []
        value = 1
        found_index = exponential_search(values, value)
        self.assertIsNone(found_index)


if __name__ == '__main__':
    unittest.main()
