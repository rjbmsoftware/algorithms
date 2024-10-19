import unittest

from sort_utils import is_sorted


def counting_sort(values: list) -> list:
    """
    counting sort positive integer value implementation

    stable sort which returns a new list

    complexity
        time and space:
            O(n + k) where n is the number of elements and k is the range of values
    """
    already_sorted = len(values) <= 1
    if already_sorted:
        return values[:]

    # count the frequency of the values
    range_list = [0] * (determine_maximum_value(values) + 1)
    for value in values:
        range_list[value] += 1

    # set starting index by adding the current element to the next element
    for i in range(0, len(range_list) - 1):
        range_list[i + 1] += range_list[i]

    # shift the starting indexes along one as zero will always be in the lowest
    # index for an ascending sort
    for i in range(len(range_list) - 1, 0, -1):
        range_list[i] = range_list[i - 1]

    range_list[0] = 0

    # insert values into a new list
    sorted_list = [0] * len(values)

    for value in values:
        sorted_list[range_list[value]] = value
        range_list[value] += 1

    return sorted_list


def determine_maximum_value(values: list[int]) -> int:
    """
    Deliberately not using max to show complexity
    """
    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value

    return maximum


class CountingSortTest(unittest.TestCase):

    def test_single_value_list(self):
        values = [1]
        counting_sort(values)
        self.assertEqual(len(values), 1)
        self.assertTrue(values[0], 1)

    def test_two_value_list(self):
        values = [2, 1]
        values = counting_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2], actual {values}')

    def test_three_value_list(self):
        values = [3, 2, 1]
        values = counting_sort(values)
        self.assertTrue(is_sorted(values),
                        f'Expected [1, 2, 3], actual {values}')

    def test_max_to_min(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        values = counting_sort(values)
        self.assertTrue(is_sorted(values))

    def test_empty_is_sorted(self):
        values = []
        counting_sort(values)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        counting_sort(values)
        self.assertTrue(is_sorted(values))

    def test_same(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        values = counting_sort(values)
        self.assertTrue(is_sorted(values))


if __name__ == '__main__':
    unittest.main()
