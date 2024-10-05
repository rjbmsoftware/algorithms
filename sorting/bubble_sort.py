import unittest

from sort_utils import is_sorted


def bubble_sort(values: list) -> None:
    """
    sorts ascending

    in place sort

    complexity
        time: n squared
        space: n 

    implementation of the bubble sort algorithm
    that will work on any type that can be
    compared with <>== that
    """
    for i in range(1, len(values)):
        for j in range(len(values) - i):
            next_index = j + 1
            if values[j] > values[next_index]:
                values[j], values[next_index] = values[next_index], values[j]

    return values


class BubbleSortTest(unittest.TestCase):

    def test_max_to_min(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort(values)
        self.assertTrue(is_sorted(values))

    def test_empty_is_sorted(self):
        values = []
        bubble_sort(values)
        self.assertTrue(is_sorted(values))

    def test_already_sorted(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bubble_sort(values)
        self.assertTrue(is_sorted(values))

    def test_same(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bubble_sort(values)
        self.assertTrue(is_sorted(values))


if __name__ == "__main__":
    unittest.main()
