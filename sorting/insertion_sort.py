import unittest

from sort_utils import is_sorted


def insertion_sort(values: list) -> None:
    """
    insertion sort implementation

    sorts comparable items in ascending order

    complexity:
        time:
            worst case is when the list is in the reverse order of the sort O(n^2)
            best is O(n) for an already sorted array
            average O(n^2), 
        space:
            insertion sort is in place O(1)

        1. loop through the array
        2. start with the second element noting the value
        3. loop backwards through the array shifting values along if they are greater
        4. insert stored value at the final position

        shifting is better than swapping here as we halve the amount of writes
    """
    for working_index in range(1, len(values)):
        current_value = values[working_index]
        backwards_index = working_index
        while backwards_index > 0 and values[backwards_index - 1] > current_value:
            values[backwards_index] = values[backwards_index - 1]
            backwards_index -= 1
        values[backwards_index] = current_value


class InsertionSortTest(unittest.TestCase):

    def test_empty_list(self):
        values = []
        insertion_sort(values)
        self.assertEqual(values, [])

    def test_single_value_list(self):
        values = [1]
        insertion_sort(values)
        self.assertEqual(len(values), 1)
        self.assertTrue(values[0], 1)

    def test_two_value_list(self):
        values = [2, 1]
        insertion_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2], actual {values}')

    def test_three_value_list(self):
        values = [3, 2, 1]
        insertion_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2, 3], actual {values}')

    def test_max_to_min(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(values)
        self.assertTrue(is_sorted(values))

    def test_empty_is_sorted(self):
        values = []
        insertion_sort(values)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        insertion_sort(values)
        self.assertTrue(is_sorted(values))

    def test_same(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        insertion_sort(values)
        self.assertTrue(is_sorted(values))


if __name__ == "__main__":
    unittest.main()
