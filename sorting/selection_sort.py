import unittest

from sort_utils import is_sorted


def selection_sort(values: list) -> None:
    """
    selection sort implementation

    complexity
        time:
            O(n^2) where n is the number of elements in the list as we loop over the remaining part
            of the list each time to find the smallest element
        space:
            O(1) as it is an in place algorithm

    1. find the smallest element in the list
    2. swap the first element with the smallest value
    3. loop through the remainder of the list swapping the smallest element of the remaining list
       into the relevant index
    """
    for i in range(0, len(values)):
        smallest_index = smallest_value_index(values, i)
        swap(values, i, smallest_index)


def smallest_value_index(values: list, first_index: int) -> int:
    minimum_value = values[first_index]
    minimum_index = first_index

    for i in range(first_index, len(values)):
        if values[i] < minimum_value:
            minimum_value = values[i]
            minimum_index = i

    return minimum_index


def swap(values, first_index: int, second_index: int) -> None:
    swap_value = values[first_index]
    values[first_index] = values[second_index]
    values[second_index] = swap_value


class SelectionSortTest(unittest.TestCase):

    def test_empty_list(self):
        values = []
        selection_sort(values)
        self.assertEqual(values, [])

    def test_single_value_list(self):
        values = [1]
        selection_sort(values)
        self.assertEqual(len(values), 1)
        self.assertTrue(values[0], 1)

    def test_two_value_list(self):
        values = [2, 1]
        selection_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2], actual {values}')

    def test_three_value_list(self):
        values = [3, 2, 1]
        selection_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2, 3], actual {values}')

    def test_max_to_min(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_sort(values)
        self.assertTrue(is_sorted(values))

    def test_empty_is_sorted(self):
        values = []
        selection_sort(values)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        selection_sort(values)
        self.assertTrue(is_sorted(values))

    def test_same(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        selection_sort(values)
        self.assertTrue(is_sorted(values))


if __name__ == "__main__":
    unittest.main()
